from .model import Player
from .utils import Formation
from typing import Callable



class Squed_team:
    def __init__(self):
        self.__player_data={
            "id":0,
            "name":"",
            "postion":"",
            "pic":""  
            }
        
        self.__sques={
        "coathc":[],
        "goal_kepper":[],
        "defens":[],
        "Midfielders":[],
        "Forwards":[]   
    }
    
    def __get_team_players(self,fun:Callable):
        return fun()
    
    
    def formation_team_postion(self,fun):
        data=self.__get_team_players(fun)
        for i in data:
            self.__player_data['id']=i['player']['id']
            self.__player_data['name']=i['player']['name']
            self.__player_data['postion']=i['statistics'][0]['games']['position']
            self.__player_data['pic']=i['player']['photo']
            
            if i['statistics'][0]['games']['position'] == 'G':
                self.__sques['goal_kepper'].append(Player(**self.__player_data))

            elif i['statistics'][0]['games']['position'] == 'D':
                self.__sques['defens'].append(Player(**self.__player_data))
                
            elif i['statistics'][0]['games']['position'] == 'M':
                self.__sques['Midfielders'].append(Player(**self.__player_data))
            
            elif i['statistics'][0]['games']['position'] == 'F':
                self.__sques['Forwards'].append(Player(**self.__player_data))
    
    @property            
    def sques_team(self):
        return self.__sques
    
        
            
