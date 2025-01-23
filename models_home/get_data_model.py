from .ulits import *
from .model import *
from dataclasses import dataclass
from typing import List ,Callable
from datetime import datetime
import pytz 


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
        match_objects=list(map(lambda match: Matchs_league(
            id_match=match['fixture']['id'],
            id_league=match['league']['id'],
            team_home=match['teams']['home'],
            team_away=match['teams']['away'],
            status=match['fixture']['status']['long'],
            result=match['goals'],
            time_match=match['fixture']['date'],
            league_name=match['league']['name']
        ),data))
        self.data_match=list(match_objects)
        return self.data_match


 

class Important_matches:
    def __init__(self):
        self.big_leagues_ids:List=[1, 2, 3, 848, 12, 20, 534, 531, 17, 39, 45, 46, 528, 78, 81, 529, 135, 137, 547, 61, 65, 66, 526, 233, 539, 714, 307, 826, 504, 140, 143, 556, 15, 4, 5, 9, 6, 7, 10]

    def matchs_league(self, data: List[dict]) -> List[dict]:
        filtered_matches = list(filter(lambda match: match['league']['id'] in self.big_leagues_ids, data))
        return filtered_matches
    
    def sort_data(self,data:Callable):
        sort_mathcs=self.matchs_league(data)
        sort_mathcs=sorted(sort_mathcs,lambda id:id['league']['id'])
        return data
    
    def return_data(self, data: List[dict]) -> dict:
        matches = self.sort_data(data)
        dict_matches = {}
        for match in matches:
            league_name = f"league name is : {match['league']['name']}"
            if league_name not in dict_matches:
                dict_matches[league_name] = []
            dict_matches[league_name].append(match)
        
        return dict_matches