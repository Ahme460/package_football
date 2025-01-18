from .ulits import *
from typing import Dict ,List,Optional ,Union
from dataclasses import dataclass


@dataclass
class leagues:
    id:int
    name:str
    type:str
    image:str
    country:str

    def __repr__(self) -> str:
        return f"Object_ {self.name}"


    

@dataclass
class Matchs_league:
    id_match:int
    id_league:int
    team_home:dict
    team_away:dict
    status:Dict
    result:Dict
    time_match:Union[str,int,float]
    league_name:Dict

    def __repr__(self) -> str:
      
      return f"match {self.team_home['name']} vs {self.team_away['name']}"






        
    








