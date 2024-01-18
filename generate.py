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

import asyncio
import requests

name = input("\nBerikan Nama Anda: ")


async def main():
    res = requests.post(f'https://api.downloader.blue/v2/auth?name={name}')
    json = res.json()
    if res.status_code == 201:
        print("\n[ INFO ] - INI ADALAH TOKEN ANDA, SALIN TOKEN ANDA, JANGAN PERNAH MEMBERIKAN TOKEN INI KEPADA SIAPAPUN!!!\n")
        print(f"\n[ TOKEN ] - {json['token']}\n")
    else:
        print(f"\n[ ERROR ] -> {json}\n")


asyncio.run(main())
