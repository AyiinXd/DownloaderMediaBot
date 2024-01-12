import os
from configparser import ConfigParser
from typing import Optional, Union

from fipper import Client

from bot.tools import Downloader


parser = ConfigParser()
parser.read('ayiin.ini')
apiId = parser.getint('config', 'apiId')
apiHash = parser.get('config', 'apiHash')
bearerToken = parser.get('config', 'bearerToken')
token = parser.get('config', 'tokenBot')


class Robot(Client):
    def __init__(self):
        super().__init__(
            name=self.__class__.__name__.capitalize(),
            api_id=apiId,
            api_hash=apiHash,
            bot_token=token
        )

        self.config = ConfigParser().read('ayiin.ini')
        self.baseUrl = lambda x, z: f'https://api.downloader.blue/v2/{x}?url={z}'
        self.dl = Downloader(bearerToken)

    async def start(self):
        try:
            await self.start()
        except BaseException as e:
            print('ERROR: ' + e)
            exit(1)
        print('Robot Activated')
