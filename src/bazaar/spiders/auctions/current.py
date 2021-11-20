from dataclasses import asdict

from scrapy import Spider
from scrapy.http.response.html import HtmlResponse

from bazaar.spiders.auctions.helpers import parse_head
from bazaar.spiders.auctions.helpers import parse_items


class CurrentAuctions(Spider):
    name = "auctions"
    start_urls = [
        "https://www.tibia.com/charactertrade/?subtopic=currentcharactertrades"
    ]

    def parse(self, response: HtmlResponse):
        for auction in response.css(".Auction"):
            head = parse_head(auction)
            items = parse_items(auction)

            yield {**asdict(head), **asdict(items)}
