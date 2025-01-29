from leagues.model import Player,Player_stitic
from dataclasses import dataclass
from typing import List ,Dict


@dataclass
class StiticsMathcs:
    shots_on_goal: int
    shots_off_goal: int
    shots_inside_box: int
    shots_outside_box: int
    total_shots: int
    blocked_shots: int
    fouls: int
    corner_kicks: int
    offsides: int
    ball_possession: float
    yellow_cards: int
    red_cards: int
    goalkeeper_saves: int
    total_passes: int
    passes_accurate: int
    passes_percentage: float
    



@dataclass    
class Info_mathc:
    time:str
    stadium:str
    city:str
    referee:str
    
    
    
    
@dataclass    
class Event:
    time:int
    team:dict
    player_id:int
    player_name:str
    event_type:str
    detal_event:str
    comments:str
    

@dataclass   
class Player_stitic_mathc(Player_stitic):
    rating:float
    