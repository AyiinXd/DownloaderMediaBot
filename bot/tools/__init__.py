from .tiktok import Tiktok
from .youtube import Youtube


class Downloader(Tiktok, Youtube):
    def __init__(self, bearerToken):
        super().__init__(bearerToken)
