from typing import List
from typing import Any
from dataclasses import dataclass

@dataclass
class BadgeUrls:
    small: str
    large: str
    medium: str

    @staticmethod
    def from_dict(obj: Any) -> 'BadgeUrls':
        _small = str(obj.get("small"))
        _large = str(obj.get("large"))
        _medium = str(obj.get("medium"))
        return BadgeUrls(_small, _large, _medium)

@dataclass
class Member:
    tag: str
    name: str
    townHallLevel: int

    @staticmethod
    def from_dict(obj: Any) -> 'Member':
        _tag = str(obj.get("tag"))
        _name = str(obj.get("name"))
        _townHallLevel = int(obj.get("townHallLevel"))
        return Member(_tag, _name, _townHallLevel)        

@dataclass
class Clan:
    tag: str
    name: str
    clanLevel: int
    badgeUrls: BadgeUrls
    members: List[Member]

    @staticmethod
    def from_dict(obj: Any) -> 'Clan':
        _tag = str(obj.get("tag"))
        _name = str(obj.get("name"))
        _clanLevel = int(obj.get("clanLevel"))
        _badgeUrls = BadgeUrls.from_dict(obj.get("badgeUrls"))
        _members = [Member.from_dict(y) for y in obj.get("members")]
        return Clan(_tag, _name, _clanLevel, _badgeUrls, _members)

@dataclass
class Round:
    warTags: List[str]

    @staticmethod
    def from_dict(obj: Any) -> 'Round':
        _warTags = [obj.get("warTags")]
        return Round(_warTags)

@dataclass
class Root:
    state: str
    season: str
    clans: List[List[str]]
    rounds: List[Round]

    @staticmethod
    def from_dict(obj: Any) -> 'Root':
        _state = str(obj.get("state"))
        _season = str(obj.get("season"))
        _clans = [Clan.from_dict(y) for y in obj.get("clans")]
        _rounds = [Round.from_dict(y) for y in obj.get("rounds")]
        return Root(_state, _season, _clans, _rounds)