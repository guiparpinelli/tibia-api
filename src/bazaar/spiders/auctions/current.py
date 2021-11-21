import parse
from scrapy import Spider
from scrapy.http.response.html import HtmlResponse
from scrapy.selector import Selector

LEVEL_VOCATION_GENDER = parse.compile(
    "Level: {level} | Vocation: {vocation} | {gender} | World:"
)


class CurrentAuctions(Spider):
    name = "auctions"
    start_urls = [
        "https://www.tibia.com/charactertrade/?subtopic=currentcharactertrades"
    ]

    def parse(self, response: HtmlResponse):
        results = (
            response.css(".PageNavigation")
            .xpath(".//div[contains(@style, 'right')]/b/text()")
            .get()
        )
        total_results = results.removeprefix("» Results: ")  # noqa

        for auction in response.css(".Auction"):
            character = auction.css(".AuctionHeader::text").get()
            lvl_voc_gen = LEVEL_VOCATION_GENDER.search(character)
            auction_url = auction.css(".AuctionCharacterName").xpath("./a/@href").get()
            name, world = auction.css(".AuctionHeader").css("a::text").getall()
            outfit = auction.css(".AuctionOutfit").xpath("./img/@src").get()

            items = parse_items(auction)
            args = auction.css(".Entry::text").getall()
            start, end, _ = auction.css(".ShortAuctionDataValue::text").getall()
            current_bid = auction.css(".ShortAuctionDataValue").css("b::text").get()

            yield dict(
                **lvl_voc_gen.named,
                name=name,
                world=world,
                outfit=outfit,
                auction_url=auction_url,
                items_display=items,
                sale_arguments=args,
                start=start,
                end=end,
                current_bid=current_bid,
            )


def parse_items(auction: Selector):
    items = auction.css(".AuctionItemsViewBox")
    items_imgs = items.xpath("./div/img/@src").getall()
    if not items_imgs:
        return dict(items=[])

    items_titles = list(
        filter(
            lambda x: x != "(no item for display selected)",
            items.xpath("./div/@title").getall(),
        )
    )

    return [dict(img=img, title=title) for img, title in zip(items_imgs, items_titles)]
