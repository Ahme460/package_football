
from .utils import *
from .model import *
from dataclasses import dataclass
from typing import List ,Callable,Union
from models_home.model import Matchs_league 
from models_home.get_data_model import Get_data_match

# data league teams 
@dataclass
class Teams_League:
    leagues_all=list[Teams]
    def teams_league(self):
        data=get_teams_league()
        leagues_objects=map(lambda teams: Teams(
            id=teams['team']['id'],
            name=teams['team']['name'],
            img=teams['team']['logo'],
            country=teams['team']['country']
        ),data)

        self.leagues_all = list(leagues_objects)
        return self.leagues_all
    




class Get_matchs(Get_data_match):
    def __inti__(self , data_match:List[Matchs_league]=None):
        super().__init__(data_match)
    def get_data_match(self,data:Callable):
        print("next match")
        return super().get_data_match(data)


@dataclass
class Get_Table:
    table_league:List[Table_league]=None
    def get_data_table(self):
        data=table_league()
        #print(data)
        table_rank_objects=list(map(lambda row: Table_league(
            ranking=row['rank'],
            count_mathc=row['all']['played'],
            win_mathc=row['all']['win'],
            draw_match=row['all']['draw'],
            lost_match=row['all']['lose'],
            count_goal=row['all']['goals']['for'],
            aginst_goal=row['all']['goals']['against'],
            point=row['points'],
            team=row['team']
            
        ),data))
        self.table_league=table_rank_objects
        print(self.table_league)
        return self.table_league



class Get_top_status:
    