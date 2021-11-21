from enum import Enum


class Vocation(str, Enum):
    """Represents the character vocation"""

    KNIGHT = "Knight"
    ELITE_KNIGHT = "Elite Knight"
    PALADIN = "Paladin"
    ROYAL_PALADIN = "Royal Paladin"
    SORCERER = "Sorcerer"
    MASTER_SORCERER = "Master Sorcerer"
    DRUID = "Druid"
    ELDER_DRUID = "Elder Druid"


class Gender(str, Enum):
    """Represents the character gender"""

    MALE = "Male"
    FEMALE = "Female"


class AuctionStatus(Enum):
    """Represents the current status of an auction entry"""

    pass
