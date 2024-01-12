import requests
from typing import Union

from .interface import tiktokInterface


class Tiktok():
    def __init__(self, bearerToken):
        self.bearerToken = bearerToken

    def tiktokDl(self, url: str) -> Union[tiktokInterface, str]:
        res = requests.get(
            url,
            headers={'Authorization': f'Bearer {self.bearerToken}'}
        )
        if res.status_code == 200:
            json: tiktokInterface = res.json()
            return json
        else:
            return 'Failed'
