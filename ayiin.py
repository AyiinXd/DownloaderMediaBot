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

from os import getenv
from dotenv import load_dotenv

load_dotenv()


apiId: int = getenv("API_ID", 6)
apiHash: str = getenv("API_HASH", "")
botToken: str = getenv("BOT_TOKEN", "")

# Generate Token with Command python3 -m generate
bearerToken: str = getenv("BEARER_TOKEN", "")

# Support and Update
channel: str = getenv("CHANNEL", "")
group: str = getenv("GROUP", "")
