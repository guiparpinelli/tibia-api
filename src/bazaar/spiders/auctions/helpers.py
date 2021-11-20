from scrapy.selector import Selector

from bazaar.spiders.auctions.models import AuctionHead
from bazaar.spiders.auctions.models import Item
from bazaar.spiders.auctions.models import Items


def parse_head(auction: Selector) -> AuctionHead:
    auction_url = auction.css(".AuctionCharacterName").xpath("./a/@href").get()
    name, world = auction.css(".AuctionHeader").css("a::text").getall()
    outfit = auction.css(".AuctionOutfit").xpath("./img/@src").get()

    header = auction.css(".AuctionHeader::text").get().split("|")
    level = header[0].split(":")[1].strip()
    vocation = header[1].split(":")[1].strip()
    sex = header[2].strip()

    return AuctionHead(name, level, vocation, sex, world, outfit, auction_url)


def format_item_title(title: str) -> str:
    return title.split("\n")[0].lower()


def parse_items(auction: Selector) -> Items:
    items = auction.css(".AuctionItemsViewBox")
    items_imgs = items.xpath("./div/img/@src").getall()
    if not items_imgs:
        return Items()

    items_titles = list(
        filter(
            lambda x: x != "(no item for display selected)",
            items.xpath("./div/@title").getall(),
        )
    )

    return Items(
        [
            Item(img, format_item_title(title))
            for img, title in zip(items_imgs, items_titles)
        ]
    )
