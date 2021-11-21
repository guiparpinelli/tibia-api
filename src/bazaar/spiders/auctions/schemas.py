from typing import List

from pydantic import BaseModel
from pydantic import validator

from bazaar.spiders.auctions import enums


class Item(BaseModel):
    img: str
    title: str

    @validator("title", pre=True)
    def remove_description_from_title(cls, v: str) -> str:
        return v.split("\n")[0].lower()


class Items(BaseModel):
    items: List[Item] = list()


class AuctionCard(BaseModel):
    name: str
    level: int
    vocation: enums.Vocation
    gender: enums.Gender
    world: str
    outfit: str
    auction_url: str
    items_display: Items
    sale_arguments: List[str] = list()


class Auctions(BaseModel):
    auctions: List[AuctionCard]
