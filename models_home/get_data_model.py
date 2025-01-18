from .ulits import *
from .model import *
from dataclasses import dataclass
from typing import List ,Callable


#get league data 1

@dataclass
class all_leagues:
    leagues_all=list[leagues]
    def get_all_leagues(self):
        data=all_league()
        leagues_objects=map(lambda league: leagues(
            id=league['league']['id'],
            name=league['league']['name'],
            type=league['league']['type'],
            image=league['league']['logo'],
            country=league['country']['name']
        ),data)

        self.leagues_all = list(leagues_objects)

        return self.leagues_all
    




# get match data 2

@dataclass
class Get_data_match:
    data_match:List[Matchs_league]=None
    
    def get_data_match(self,data:Callable):
        if isinstance(data, dict):
            data = [data] 
        #print(data)
        match_objects=list(map(lambda match: Matchs_league(
            id_match=match['fixture']['id'],
            id_league=match['league']['id'],
            team_home=match['teams']['home'],
            team_away=match['teams']['away'],
            status=match['fixture']['status']['long'],
            result=match['goals'],
            time_match=get_time(match['fixture']['date']),
            league_name=match['league']['name']

        ),data))
        self.data_match=list(match_objects)
        return self.data_match
    

