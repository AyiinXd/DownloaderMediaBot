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

from typing import Dict, Optional

from pyrogram import Client

from ayiin import apiHash, apiId, bearerToken, botToken
from bot.tools import Downloader


class Robot(Client):
    def __init__(self):
        super().__init__(
            name=self.__class__.__name__.capitalize(),
            api_id=apiId,
            api_hash=apiHash,
            bot_token=botToken
        )

        self.baseUrl = lambda x: f'https://api.downloader.blue/v2/{x}'
        self.xd = Downloader(bearerToken)
        self.db: Optional[Dict] = {}

    async def start(self):
        try:
            await super().start()
            print('[ INFO ] - Robot Activated')
        except BaseException as e:
            print(f'[ ERROR ] - {e}')
            return

    def getUrl(self, user) -> list:
        try:
            data = self.db[user]
            return data
        except KeyError:
            return []
