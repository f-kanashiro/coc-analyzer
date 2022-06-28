from typing import List
from typing import Any
from dataclasses import dataclass

@dataclass
class Attack:
    attackerTag: str
    defenderTag: str
    stars: int
    destructionPercentage: int
    order: int
    duration: int

    @staticmethod
    def from_dict(obj: Any) -> 'Attack':
        _attackerTag = str(obj.get("attackerTag"))
        _defenderTag = str(obj.get("defenderTag"))
        _stars = int(obj.get("stars"))
        _destructionPercentage = int(obj.get("destructionPercentage"))
        _order = int(obj.get("order"))
        _duration = int(obj.get("duration"))
        return Attack(_attackerTag, _defenderTag, _stars, _destructionPercentage, _order, _duration)
        
@dataclass
class BestOpponentAttack:
    attackerTag: str
    defenderTag: str
    stars: int
    destructionPercentage: int
    order: int
    duration: int

    @staticmethod
    def from_dict(obj: Any) -> 'BestOpponentAttack':
        _attackerTag = str(obj.get("attackerTag"))
        _defenderTag = str(obj.get("defenderTag"))
        _stars = int(obj.get("stars"))
        _destructionPercentage = int(obj.get("destructionPercentage"))
        _order = int(obj.get("order"))
        _duration = int(obj.get("duration"))
        return BestOpponentAttack(_attackerTag, _defenderTag, _stars, _destructionPercentage, _order, _duration)

@dataclass
class Member:
    tag: str
    name: str
    townhallLevel: int
    mapPosition: int
    opponentAttacks: int
    bestOpponentAttack: BestOpponentAttack
    attacks: List[Attack]

    @staticmethod
    def from_dict(obj: Any) -> 'Member':
        _tag = str(obj.get("tag"))
        _name = str(obj.get("name"))
        _townhallLevel = int(obj.get("townhallLevel"))
        _mapPosition = int(obj.get("mapPosition"))
        _opponentAttacks = int(obj.get("opponentAttacks"))
        _bestOpponentAttack = BestOpponentAttack.from_dict(obj.get("bestOpponentAttack"))
        _attacks = [Attack.from_dict(y) for y in obj.get("attacks")]
        return Member(_tag, _name, _townhallLevel, _mapPosition, _opponentAttacks, _bestOpponentAttack, _attacks)



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
class Clan:
    tag: str
    name: str
    badgeUrls: BadgeUrls
    clanLevel: int
    attacks: int
    stars: int
    destructionPercentage: float
    members: List[Member]

    @staticmethod
    def from_dict(obj: Any) -> 'Clan':
        _tag = str(obj.get("tag"))
        _name = str(obj.get("name"))
        _badgeUrls = BadgeUrls.from_dict(obj.get("badgeUrls"))
        _clanLevel = int(obj.get("clanLevel"))
        _attacks = int(obj.get("attacks"))
        _stars = int(obj.get("stars"))
        _destructionPercentage = float(obj.get("destructionPercentage"))
        _members = [Member.from_dict(y) for y in obj.get("members")]
        return Clan(_tag, _name, _badgeUrls, _clanLevel, _attacks, _stars, _destructionPercentage, _members)

@dataclass
class Opponent:
    tag: str
    name: str
    badgeUrls: BadgeUrls
    clanLevel: int
    attacks: int
    stars: int
    destructionPercentage: float
    members: List[Member]

    @staticmethod
    def from_dict(obj: Any) -> 'Opponent':
        _tag = str(obj.get("tag"))
        _name = str(obj.get("name"))
        _badgeUrls = BadgeUrls.from_dict(obj.get("badgeUrls"))
        _clanLevel = int(obj.get("clanLevel"))
        _attacks = int(obj.get("attacks"))
        _stars = int(obj.get("stars"))
        _destructionPercentage = float(obj.get("destructionPercentage"))
        _members = [Member.from_dict(y) for y in obj.get("members")]
        return Opponent(_tag, _name, _badgeUrls, _clanLevel, _attacks, _stars, _destructionPercentage, _members)

@dataclass
class Root:
    state: str
    teamSize: int
    attacksPerMember: int
    preparationStartTime: str
    startTime: str
    endTime: str
    clan: Clan
    opponent: Opponent

    @staticmethod
    def from_dict(obj: Any) -> 'Root':
        _state = str(obj.get("state"))
        _teamSize = int(obj.get("teamSize"))
        _attacksPerMember = int(obj.get("attacksPerMember"))
        _preparationStartTime = str(obj.get("preparationStartTime"))
        _startTime = str(obj.get("startTime"))
        _endTime = str(obj.get("endTime"))
        _clan = Clan.from_dict(obj.get("clan"))
        _opponent = Opponent.from_dict(obj.get("opponent"))
        return Root(_state, _teamSize, _attacksPerMember, _preparationStartTime, _startTime, _endTime, _clan, _opponent)