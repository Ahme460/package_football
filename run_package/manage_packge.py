from models_home.get_data_model import *
from models_home.ulits import *
from leagues import *
from leagues.statics import *
from leagues.squed import *
from transafer import *
from typing import Callable
from .interface import Callable_packed
from .parametr import *
from leagues.create_data_model import *
from leagues.dict_data import *
from transafer.create_model import *
from transafer.utlis import *


class All_Leagues_M(Callable_packed):
    def __init__(self):
        self.instance= All_leagues()
        self.request= Mathchs_leagues_request_by_date()
        self.params= params_all_league()
        
    def get_request_class(self):
        request=self.request.rquest_data(**self.params)
        return request
    
    def class_data(self):
        leagues=self.instance.get_all_leagues(self.get_request_class())
        return leagues
  

class TOP_Leagues_M(Callable_packed):
    def __init__(self):
        self.request=Rquest()
        self.instance=Top_leagues()
        
    def get_request_class(self):
        request=self.request.rquest_data(**params_all_league())
        return request
    
    def class_data(self):
        leagues=self.instance.get_top_leagues(self.get_request_class())
        return leagues
  
    
    
class Matchs_M(Callable_packed):
    def __init__(self, data: str):
        self.instance = Important_matches() 
        self.request = Mathchs_leagues_request_by_date() 
        self.data = data  
        self.params = params_mathcs_by_data(data)  

    def get_request_class(self):
        response = self.request.rquest_data(**self.params)
        return response

    def class_data(self):
        matches = self.instance.get_data_match(self.get_request_class())
        matches=self.instance.return_data(matches)
        return matches

    
class Matchs_league_M(Callable_packed):
    def __init__(self):
        self.instance = Get_data_match() 
        self.request = Mathchs_leagues_request() 
    def get_request_class(self,league_id,season):
        response = self.request.rquest_data(**params_mathcs_league(league_id,season))
        return response

    def class_data(self,league_id:int,season:int):
        matches = self.instance.get_data_match(self.get_request_class(league_id,season))
        return matches
    

class Last_mathcs_team(Callable_packed):
    def __init__(self):
        self.instance = Get_data_match() 
        self.request = Mathchs_leagues_request()
        
    def get_request_class(self,team_id:int,last):
        return self.request.rquest_data(**params_last_mathcs(team_id,last_n=last))
    
    def class_data(self,team_id:int,last):
        matchs=self.instance.get_data_match(self.get_request_class(team_id,last))
        return matchs
    
    


class Next_mathcs_team(Callable_packed):
    def __init__(self):
        self.instance = Get_data_match() 
        self.request = Mathchs_leagues_request()
        
    def get_request_class(self,team_id:int,next):
        return self.request.rquest_data(**params_next_mathcs(team_id,last_n=next))
    
    def class_data(self,team_id:int,next):
        matchs=self.instance.get_data_match(self.get_request_class(team_id,next))
        return matchs
    
 

class Normal_Matchs_M(Callable_packed):
    def __init__(self, data: str):
        self.instance = Normal_mathcs() 
        self.request = Mathchs_leagues_request_by_date() 
        self.data = data  
        self.params = params_mathcs_by_data(data)  

    def get_request_class(self):
        response = self.request.rquest_data(**self.params)
        return response

    def class_data(self):
        matches = self.instance.get_data_match(self.get_request_class())
        matches=self.instance.return_data(matches)
        return matches



class Team_league_M(Callable_packed):
    def __init__(self):
        self.instance = Teams_League() 
        self.request = Get_teams_league()  
        
    def get_request_class(self,league_id:str,season:int):
        return self.request.rquest_data(**params_teams_in_league(league_id,season))

    def class_data(self,league_id:str,season:int):
        data=self.get_request_class(league_id,season)
        teams=self.instance.teams_league(data)
        return teams
    
    
class Table_league_M(Callable_packed):
    def __init__(self):
        self.instance = Get_Table() 
        self.request = Table_league_request()  
        
    def get_request_class(self,league_id:str,season:int):
        return self.request.rquest_data(**params_table_league(league_id,season))
    
    def class_data(self,league_id:str,season:int):
        data=self.get_request_class(league_id,season)
        table=self.instance.get_data_table(data)
        return table
    

class Top_Goal_player_M(Callable_packed):
    def __init__(self):
        self.instance = Goals_player() 
        self.request = TOP_scorers()
  
    def get_request_class(self,league_id:int,season:int):
        return self.request.rquest_data(**params_goal(league_id,season))
    
    def class_data(self,league_id:int,season:int):
        data=self.get_request_class(league_id,season)
        top_goal=self.instance.create_instance_player(dict_data(data))
        return top_goal
    
    
class Top_Assist_player_M(Callable_packed):
    def __init__(self):
        self.instance = Assist_player() 
        self.request = TOP_assist()
  
    def get_request_class(self,league_id:int,season:int):
        return self.request.rquest_data(**params_assist(league_id,season))
    
    def class_data(self,league_id:int,season:int):
        data=self.get_request_class(league_id,season)
        top_goal=self.instance.create_instance_player(dict_data(data))
        return top_goal
    

class Squed_Teams_M(Callable_packed):
    def __init__(self):
        self.instance=Squed_team()
        self.request=Request_GET_Squed()
        
    def get_request_class(self,team_id:int,season:int):
        return self.request.rquest_data(**params_team_squed(team_id,season))
    
    def class_data(self,team_id:int,season:int):
        data=self.get_request_class(team_id,season)
        squed=self.instance.formation_team_postion(data)
        return squed
            


class Transfer_team_M(Callable_packed):
    def __init__(self) -> list[Player_transfer]:
        self.request=Get_transfer_team()
        self.instance=Analysis_data()

    def get_request_class(self,team_id:int):
        return self.request.rquest_data(**params_transfer_team(team_id))
    
    def class_data(self,team_id):
        data=self.instance.dict_data(self.get_request_class(team_id))
        return list(map(lambda player_tr:Player_transfer(**player_tr),data))
            
    
    
