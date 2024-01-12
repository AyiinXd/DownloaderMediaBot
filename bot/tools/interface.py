from typing import List, Union


tiktokInterface: dict = {
    "status": str,
    "result": {
        "type": str,
        "id": str,
        "createTime": int,
        "description": str,
        "hashtag": List[Union[str, str], str],
        "duration": str,
        "author": {
            "uid": str,
            "username": str,
            "nickname": str,
            "signature": str,
            "region": str,
            "avatarThumb": List[Union[str, str], str],
            "avatarMedium": List[Union[str, str], str],
            "url": str
        },
        "statistics": {
            "playCount": int,
            "downloadCount": int,
            "shareCount": int,
            "commentCount": int,
            "likeCount": int,
            "favoriteCount": int,
            "forwardCount": int,
            "whatsappShareCount": int,
            "loseCount": int,
            "loseCommentCount": int
        },
        "video": List[Union[str, str], str],
        "cover": List[Union[str, str], str],
        "dynamicCover": List[Union[str, str], str],
        "originCover": List[Union[str, str], str],
        "music": {
            "id": int,
            "title": str,
            "author": str,
            "album": str,
            "playUrl": List[Union[str, str], str],
            "coverLarge": List[Union[str, str], str],
            "coverMedium": List[Union[str, str], str],
            "coverThumb": List[Union[str, str], str],
            "duration": int
        }
    }
}
