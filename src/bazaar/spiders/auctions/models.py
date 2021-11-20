from dataclasses import dataclass
from dataclasses import field
from typing import List


@dataclass
class AuctionHead:
    name: str
    level: str
    vocation: str
    sex: str
    world: str
    outfit: str
    auction_url: str


@dataclass
class Item:
    img: str
    title: str


@dataclass
class Items:
    items: List[Item] = field(default_factory=list)
