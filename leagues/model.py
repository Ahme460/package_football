from dataclasses import dataclass
from typing import Dict

@dataclass
class Teams:
    id:int
    name:str
    img:str
    country:str


    def __repr__(self) -> str:
        return self.name



@dataclass
class Table_league:
    ranking:int
    count_mathc:int
    win_mathc:int
    draw_match:int
    lost_match:int
    count_goal:int
    aginst_goal:int
    point:int
    team:dict


    def __repr__ (self) -> str:
        return f"{self.point}___{self.team['name']}"


class Player:
    pass

@dataclass
class Player_stitic(Player):
    name:str
    id_player:int
    age:int
    photo:str
    goal:int
    assist:int
    shots:Dict
    minutes:int
    postion:str
    passes:dict
    tackls:Dict
    dribbles_succ=int
    



