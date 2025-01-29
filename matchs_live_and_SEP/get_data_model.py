from .model import Info_mathc,StiticsMathcs,Event
from dict_data import *

class Get_Info_mathc:
    def get_info_mathc(self,data):
        return Info_mathc(**info_dict(data))



class Get_Stitics_mathcs:
    def __init__(self) -> dict[StiticsMathcs]:
        self.__stitics_teams:dict={}
    def get_stitic_mathc(self,data):
        for i in range(2):
            self.__stitics_teams['team1']=StiticsMathcs(**statistics_mathc_dict(data,team=i))
            self.__stitics_teams['team2']=StiticsMathcs(**statistics_mathc_dict(data,team=i+1))
            break
        return self.__stitics_teams
    

class Get_events_mathcs:
    def __init__(self) -> list[Event]:
        self.__events=[]
    def get_events_match(self,data):
        self.__events(map(lambda event: Event(**event_mathc_dict(event)) ,data['response']))   
        return self.__events
    