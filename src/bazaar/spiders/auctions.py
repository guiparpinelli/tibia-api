from scrapy import http
from scrapy import Spider


class CurrentAuctions(Spider):
    name = "auctions"
    start_urls = [
        "https://www.tibia.com/charactertrade/?subtopic=currentcharactertrades"
    ]

    def parse(self, response: http.Response):
        pass
