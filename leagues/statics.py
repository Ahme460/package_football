from typing import Dict , List , Optional ,Callable,Union
from .model import *
from .utils import get_top_scorers


class Goals:
    """
    sort first thirty plyer_stiticis by goals 
    or team 
    """
    def __init__(self,players:List[Player_stitic]) -> Union[Player_stitic]:
        self.players=players

    def __rank_players_by_Goal(self,top_scoers,league_id:int, season:int)-> list[Player_stitic]:
        data=top_scoers(league_id,season)
        return data
    

class Goals_player(Goals):
    def create_instance_player(self,league,season):
        data=self.__rank_players_by_Goal(league,season)
        return list(map(lambda player_stitic:Player_stitic(**player_stitic),data))


class Goals_teams(Goals):
    def create_instance_team(self,id_team,season):
        data=self.__rank_players_by_Goal(id_team,season)
        return list(map(lambda team_stitic:Team_statics(**team_stitic),data)) 

        
class Assiste:
    def __init__(self,players:Union[Player_stitic]) -> Union[Player_stitic]:
        self.playes=players

    def __rank_players_by_assist(self,league_id:int, season:int)-> List[Player_stitic]:
        data=get_top_scorers(league_id,season)
        print(data)
        data = [
        player for player in data
        if player.get('statistics') and player['statistics'][0].get('goals') and player['statistics'][0]['goals'].get('assists') is not None
    ]
        data=sorted(data, key=lambda x: x['statistics'][0]['goals']['assists'], reverse=True)
        return data
    

class Assist_player(Assiste):
    def create_instance_player(self,league,season):
        data=self.__rank_players_by_assist(league,season)
        return list(map(lambda player_stitic:Player_stitic(**player_stitic),data))


class Assist_teams(Assiste):
    def create_instance_team(self,id_team,season):
        data=self.__rank_players_by_assist(id_team,season)
        return list(map(lambda team_stitic:Team_statics(**team_stitic),data)) 

        