from typing import Dict , List , Optional ,Callable,Union
from .model import *
from .utils import get_top_scorers


class Goals:
    """
    sort first thirty plyer_stiticis by goals 
    or team 
    """
    pass


class Goals_player(Goals):
    def create_instance_player(self,data):
        return list(map(lambda player_stitic:Player_stitic(**player_stitic),data))


class Goals_teams(Goals):
    def create_instance_team(self,data):
        return list(map(lambda team_stitic:Team_statics(**team_stitic),data)) 

        
class Assiste:
    """base class for top assist"""
    pass
    

class Assist_player(Assiste):
    def create_instance_player(self,data):
        return list(map(lambda player_stitic:Player_stitic(**player_stitic),data))


class Assist_teams(Assiste):
    def create_instance_team(self,data):
        return list(map(lambda team_stitic:Team_statics(**team_stitic),data)) 

        
