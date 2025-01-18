from typing import Dict , List , Optional ,Callable,Union
from .model import Player_stitic
from .utils import get_top_scorers




class Goals:
    """
    sort first thirty plyer_stiticis by goals 
    or team 
    """
    def __init__(self,players:List[Player_stitic]) -> Union[Player_stitic]:
        self.players=players

    def __rank_players_by_Goal(self,league_id:int, season:int)-> list[Player_stitic]:
        data=get_top_scorers(league_id,season)
        return data
    
    def top_thery(self,league_id:int,season:int)-> Player_stitic :
        data=self.__rank_players_by_Goal(league_id=league_id,season=season)[0:3]
        return data
    def create_instance_player(self):
        pass




        
    
        
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
    
    def top_thery(self,league,season):
        data=self.__rank_players_by_assist(league_id=league,season=season)[0:3]
        return data
        




    

        