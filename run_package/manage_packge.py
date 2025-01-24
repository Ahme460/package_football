from models_home.get_data_model import *
from models_home.ulits import *
from leagues import *
from transafer import *
from typing import Callable
from .interface import Callable_packed
from .parametr import *

#get all leagues 


class All_Leagues_M(Callable_packed):
    def __init__(self):
        self.instance= All_leagues()
        self.request= All_league_request()
        self.params= params_all_league()
        
    def get_request_class(self):
        request=self.request.rquest_data(**self.params)
        return request
    
    def class_data(self):
        leagues=self.instance.get_all_leagues(self.get_request_class)
        return leagues
    
    
class Matchs_M(Callable_packed):
    def __init__(self, data: str):
        self.instance = Important_matches() 
        self.request = Mathchs_league_request() 
        self.data = data  
        self.params = params_mathcs_by_data(data)  

    def get_request_class(self):
        response = self.request.rquest_data(**self.params)
        return response

    def class_data(self):
        matches = self.instance.get_data_match(self.get_request_class())
        matches=self.instance.return_data(matches)
        return matches









    
    
    
    
    
    
    
    
    
    def all_leagues(self,data:Callable):
        return data
    

#get mathcs today
class Mathcs_by_time:
    