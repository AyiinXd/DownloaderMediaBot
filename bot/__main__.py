# ===========================================================
#             Copyright (C) 2023-present AyiinXd
# ===========================================================
# ||                                                       ||
# ||              _         _ _      __  __   _            ||
# ||             / \  _   _(_|_)_ __ \ \/ /__| |           ||
# ||            / _ \| | | | | | '_ \ \  // _` |           ||
# ||           / ___ \ |_| | | | | | |/  \ (_| |           ||
# ||          /_/   \_\__, |_|_|_| |_/_/\_\__,_|           ||
# ||                  |___/                                ||
# ||                                                       ||
# ===========================================================
# Appreciating the work of others is not detrimental to you
# ===========================================================

import os
import sys
from traceback import format_exc

from pyrogram import filters, idle
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup, Message

from ayiin import channel, group
from bot import ayiin, loop


textStart = '''
**Hello {mention}**

Saya Adalah {nameBot} yang berfungsi untuk mendownload video tiktok tanpa watermark

**Perintah yang tersedia :**
    /tiktok url
    /youtube url
'''

textThumbnailYoutube = '''
**Informasi**

**Judul :** {judul}
**Durasi :** {durasi} detik
**Channel :** [{name}]({channel})
'''


async def index():
    if "downloads" not in os.listdir():
        os.mkdir("downloads")
    try:
        await ayiin.start()
    except:
        print(f'[ ERROR ] - {format_exc()}')
        return
    print('[ INFO ] - Downloader Media Activated')
    await idle()


@ayiin.on_message(filters.command('start') & filters.private)
async def startBot(_, m: Message):
    user = m.from_user
    await ayiin.send_message(
        chat_id=m.chat.id,
        text=textStart.format(mention=user.mention, nameBot=ayiin.me.mention),
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text='Group',
                        url=group
                    ),
                    InlineKeyboardButton(
                        text='Channel',
                        url=channel
                    )
                ]
            ]
        )
    )


@ayiin.on_message(filters.command(['tiktok', 'youtube']))
async def startBot(_, m: Message):
    user = m.from_user
    if (len(m.command) < 2):
        return await m.reply(f'Silahkan berikan perintah /{m.command[0]} url')
    url = m.command[1]
    if (m.command[0] == 'tiktok'):
        apiUrl = ayiin.baseUrl(f'tiktok?url={url}')
        data = ayiin.xd.tiktokDl(apiUrl)
        if data != 'Failed':
            hashtag: list = data['hashtag']
            await ayiin.send_video(
                chat_id=m.chat.id,
                video=data['video'][0],
                caption=f'''
**NickName:** {data['author']['nickname']}
**UserName:** {data['author']['username']}
**Duration:** {data['music']['duration']} detik
**Description:** {data['description']}
**Hashtag:** {" ".join(f'#{x}' for x in hashtag)}
''',
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                text="Follow",
                                url=data['author']['url']
                            )
                        ]
                    ]
                )
            )
            return
        print(f'[ ERROR ] - {data}')
        return
    if m.command[0] == 'youtube':
        apiUrl = ayiin.baseUrl(f'youtube?type=video&url={url}')
        data = ayiin.xd.youtubeDl(apiUrl)
        thumbnails = data['result']['details']['thumbnails']
        index = len(thumbnails) - 1
        thumb = ayiin.xd.converter(
            thumbnails[index]['url'],
            './downloads/thumbnail.jpg'
        )
        text = textThumbnailYoutube.format(
            judul=data['result']['details']['title'],
            durasi=data['result']['details']['lengthSeconds'],
            name=data['result']['details']['author']['name'],
            channel=data['result']['details']['ownerProfileUrl']
        )
        urlJson = ayiin.getUrl(user.id)
        urlJson.append(url)
        ayiin.db[user.id] = urlJson
        num = len(urlJson) - 1
        await ayiin.send_photo(
            chat_id=m.chat.id,
            photo=thumb,
            caption=text,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text='Audio',
                            callback_data=f'yt_audio {user.id} {num}'
                        ),
                        InlineKeyboardButton(
                            text='Video',
                            callback_data=f'yt_video {user.id} {num}'
                        )
                    ]
                ]
            )
        )
        os.remove('./downloads/thumbnail.jpg')
        return
    await ayiin.send_message(
        chat_id=m.chat.id,
        text=textStart.format(mention=user.mention, nameBot=ayiin.me.mention),
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text='Group',
                        url=group
                    ),
                    InlineKeyboardButton(
                        text='Channel',
                        url=channel
                    )
                ]
            ]
        )
    )


@ayiin.on_callback_query(filters.regex(r'yt_(audio|video) (.*)'))
async def callbackYoutube(_, cb: CallbackQuery):
    cmd = cb.data.split(' ')
    num = int(cmd[2])
    user = cb.from_user
    arrayUrl = ayiin.getUrl(int(cmd[1]))
    try:
        url = arrayUrl[num]
    except IndexError:
        return await cb.answer("Link Sudah pernah diunduh.")
    if user.id != int(cmd[1]):
        return await cb.answer("Ini bukan untuk anda.", show_alert=True)
    if len(arrayUrl) == 0:
        return await cb.answer("Anda belum memiliki daftar apapun untuk diunduh.", show_alert=True)
    types = cmd[0].split('_')[1]
    ext = 'mp3' if types == 'audio' else 'mp4'
    apiUrl = ayiin.baseUrl(f'youtube?type={types}&url={url}')
    data = ayiin.xd.youtubeDl(apiUrl)
    audio = ayiin.xd.converter(
        data['result']['mediaUri'],
        f'./downloads/{data["result"]["details"]["title"]}.{ext}'
    )
    if types == 'audio':
        await ayiin.send_audio(
            chat_id=cb.message.chat.id,
            audio=audio
        )
    if types == 'video':
        await ayiin.send_video(
            chat_id=cb.message.chat.id,
            video=audio
        )
    try:
        arrayUrl.pop(num)
    except:
        pass
    os.remove(f'./downloads/{data["result"]["details"]["title"]}.{ext}')


if __name__ == '__main__':
    try:
        loop.run_until_complete(index())
    except:
        print(f'[ ERROR ] - {format_exc()}')
        sys.exit()
    print('\n[ EXIT ] - Downloader Media Stoped, Bye!!!')
