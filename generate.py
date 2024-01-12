import asyncio
import requests

name = input("\nEnter Your Name: ")


async def main():
    res = requests.post(f'https://api.downloader.blue/v2/auth?name={name}')
    json = res.json()
    if res.status_code == 200:
        print("\nINI ADALAH TOKEN ANDA, SALIN TOKEN ANDA, JANGAN PERNAH MEMBERIKAN TOKEN INI KEPADA SIAPAPUN!!!\n")
        print(f"\n{json['token']}\n")
    else:
        print(f"\n[ ERROR ] -> {json['message']}\n")


asyncio.run(main())
