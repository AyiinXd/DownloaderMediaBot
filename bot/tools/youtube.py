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


class Youtube():
    def __init__(self, bearerToken):
        self.bearerToken = bearerToken

    def youtubeDl(self, url: str):
        res = requests.get(
            url,
            headers={'Authorization': f'Bearer {self.bearerToken}'}
        )
        if res.status_code == 200:
            return res.json()
        else:
            return res.json()

    def converter(self, url, filename):
        response = requests.get(url)
        with open(filename, "wb") as f:
            f.write(response.content)
            return filename
