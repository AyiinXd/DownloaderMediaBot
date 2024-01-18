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

import requests


class Tiktok():
    def __init__(self, bearerToken):
        self.bearerToken = bearerToken

    def tiktokDl(self, url: str):
        res = requests.get(
            url,
            headers={'Authorization': f'Bearer {self.bearerToken}'}
        )
        if res.status_code == 200:
            result = res.json()['result']
            author = result['author']
            statistics = result['statistics']
            music = result['music']
            try:
                dur = result['duration']
                duration = f'{dur} detik'
            except KeyError:
                duration = 'unknown'
            data = {
                "type": result['type'],
                "id": result['id'],
                "createTime": result['createTime'],
                "description": result['description'],
                "hashtag": result['hashtag'],
                "duration": duration,
                "author": {
                    "uid": author['uid'],
                    "username": author['username'],
                    "nickname": author['nickname'],
                    "signature": author['signature'],
                    "region": author['region'],
                    "avatarThumb": author['avatarThumb'],
                    "avatarMedium": author['avatarMedium'],
                    "url": author['url']
                },
                "statistics": {
                    "playCount": statistics['playCount'],
                    "downloadCount": statistics['downloadCount'],
                    "shareCount": statistics['shareCount'],
                    "commentCount": statistics['commentCount'],
                    "likeCount": statistics['likeCount'],
                    "favoriteCount": statistics['favoriteCount'],
                    "forwardCount": statistics['forwardCount'],
                    "whatsappShareCount": statistics['whatsappShareCount'],
                    "loseCount": statistics['loseCount'],
                    "loseCommentCount": statistics['loseCommentCount']
                },
                "video": result['video'],
                "cover": result['cover'],
                "dynamicCover": result['dynamicCover'],
                "originCover": result['originCover'],
                "music": {
                    "id": music['id'],
                    "title": music['title'],
                    "author": music['author'],
                    "album": music['album'],
                    "playUrl": music['playUrl'],
                    "coverLarge": music['coverLarge'],
                    "coverMedium": music['coverMedium'],
                    "coverThumb": music['coverThumb'],
                    "duration": music['duration']
                }
            }
            return data
        else:
            return 'Failed'
