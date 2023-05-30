from typing import List
from pydantic import BaseModel


class League(BaseModel):
    id: int
    name: str
    country: str


class LeagueList(BaseModel):
    items: List[League]


class Team(BaseModel):
    id: int
    name: str
    logo: str
    colors: dict


class Formation(BaseModel):
    player: dict


class StartXI(BaseModel):
    player: dict


class Substitute(BaseModel):
    player: dict


class Coach(BaseModel):
    id: int
    name: str
    photo: str


class Fixture(BaseModel):
    id: int
    team: Team
    formation: str
    startXI: List[StartXI]
    substitutes: List[Substitute]
    coach: Coach


class FixtureList(BaseModel):
    items: List[Fixture]
