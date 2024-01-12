from traceback import format_exc

from fipper import filters, idle
from fipper.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from bot import ayiin, loop


async def index():
    try:
        await ayiin.start()
    except:
        print(format_exc())
        exit(0)
    print('Downloader Media Activated')
    await idle()


@ayiin.on_message(filters.command('start') & filters.private)
async def startBot(_, m: Message):
    user = m.from_user
    await ayiin.send_message(
        chat_id=user.id,
        text=f'Hello {user.mention}'
    )

if __name__ == '__main__':
    try:
        loop.run_until_complete(index())
    except:
        print(format_exc())
        exit(0)
    print('Downloader Media Stoped, Bye!!!')
