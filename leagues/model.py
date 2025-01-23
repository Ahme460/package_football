from dataclasses import dataclass
from typing import Dict,Optional

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
    group:Optional[int]=None
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
    def __init__(self,id,name,postion,pic):
        self.id=id
        self.name=name
        self.postion=postion
        self.pic=pic


@dataclass
class Player_stitic(Player):
    name:str
    id_player:int
    photo:str
    goal:int
    assist:int
    shots:Dict
    minutes:int
    postion:str
    passes:dict
    tackls:Dict
    dribbles_succ=int    


class Team_statics(Teams):
    def __init__(self,id,name,img,country,goal,assist):
       super().__init__(id,name,img,country)
       self.goal=goal
       self.assist=assist
       
    def __str__(self):
        return f"team is {self.name} goal this seasin {self.goal}"





