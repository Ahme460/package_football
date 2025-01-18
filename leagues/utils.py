import requests
from .constract import API_token
import json
from datetime import datetime
from abc import abstractmethod

class Rquest:
    def rquest_data(self,url:str,headers:dict,params:dict):
        response=requests.get(url,headers=headers,params=params)
        data=response.json()
        return data['response']


class Get_teams_league(Rquest):
    def get_teams_league(self,url,header,params):
        self.rquest_data(url,header,params)


        
    #print(json.dumps(data,indent=4))

#add fun to filter 
class Last_matchs(Rquest):
    def last_match_result_to_team(self,url,header,params):
        self.rquest_data(url,header,params)

#add fun to filter
class Next_match(Rquest):
    def next_match(self,url,header,params):
        self.rquest_data(url,header,params)
   

class Table_league(Rquest):
    def table_league(self,url,header,params):
        self.rquest_data(url,header,params)


class Formation(Rquest):

    def formation(self,url,header,params):
        self.rquest_data(url,header,params)
        

class TOP_scorers(Rquest):
    def get_top_scorers(self,url,header,params):
        self.rquest_data(url,header,params)



class TOP_assist(Rquest):
    def get_top_scorers(self,url,header,params):
        self.rquest_data(url,header,params)



class TOP_card(Rquest):
    def get_top_scorers(self,url,header,params):
        self.rquest_data(url,header,params)



class Top_goall_and_assist(Rquest):
    def get_top_goal(self,url,header,params):
       return self.rquest_data(url,header,params)

    def get_top_assist(self,url,header,params):
       return self.rquest_data(url,header,params)
        
class Comparsone(Top_goall_and_assist):
    def __init__(self,top_goal:callable,top_assist:callable) -> dict:
        self.top_goal=top_goal
        self.top_assist=top_assist     
    def comparsone(self,url_scoers,url_assists,header,params):
        Goal_and_assist=[
            
        ]
        goal=self.top_goal(url_scoers,header,params)
        assist=self.get_top_assist(url_assists,header,params)
        for i in goal:
            Goal_and_assist.append(
                        {
                            "id":i['player']['id'],
                            "name":i['player']['name'],
                            "photo":i['player']['photo'],
                           # "team":i['statistics']['team'],
                            "goal":i['statistics'][0]['goals'] ,
                            "assist":i['statistics'][0]['goals'] ['assists'],
                            "goal_and_assist":i['statistics'][0]['goals']['total']+i['statistics'][0]['goals']['assists']

                        }
                    )
        for x in assist:
            existing_player = next((player for player in Goal_and_assist if player['id'] == x['player']['id']), None)
            if existing_player:
                continue
            else:
                # إذا لم يكن اللاعب موجودًا، أضفه إلى القائمة
                Goal_and_assist.append(
                    {
                        "id": x['player']['id'],
                        "name": x['player']['name'],
                        "photo": x['player']['photo'],
                        "goal": x['statistics'][0]['goals']['total'],
                        "assist": x['statistics'][0]['goals']['assists'],
                        "goal_and_assist": x['statistics'][0]['goals']['total'] + x['statistics'][0]['goals']['assists'],
                    }
                )
        Goal_and_assist=sorted(Goal_and_assist,key=lambda g_a:g_a['goal_and_assist'] ,reverse=True)
        return Goal_and_assist[:10]


# def filter_by_time(list_data:list):
#     today = datetime.now()
#     list_data.sort(key=lambda x: abs(datetime.fromisoformat(x['fixture']["date"][:-6]) - today))
#     nearest_match = list_data
#     #print(nearest_match)
#     return nearest_match


