from decouple import config

_api_key_ = config('API_KEY')


def params_all_league():
    return {
        "url":"https://v3.football.api-sports.io/leagues",
        "header":{"x-apisports-key": _api_key_},
        "params":{},
        
    }
    
    
def params_mathcs_by_data(date:str):
        return {
        "url":"https://v3.football.api-sports.io/fixtures",
        "header":{"x-apisports-key": _api_key_},
        "params":{
        "date": date
        },
        
    }
    

def params_mathcs_league(league_id:int,season:int):
        return {
        "url":"https://v3.football.api-sports.io/fixtures",
        "header":{"x-apisports-key": _api_key_},
        "params":{
        "league": league_id,
        "season": season
            },
        
    }
   
     
def params_teams_in_league(league_id, season):
    return {
    "url" : "https://v3.football.api-sports.io/teams",
    "header" : {"x-apisports-key": _api_key_},
    "params" :
    {
        "league": league_id,
        "season": season
    }
   }


def params_table_league(league_id:int,season:int):
        return {
        "url":"https://v3.football.api-sports.io/standings",
        "header":{"x-apisports-key": _api_key_},
        "params":{
        "league": league_id,
        "season": season
            },
        
    }
        

    
def params_goal(league_id:int,season:int):
        return {
        "url":"https://v3.football.api-sports.io/players/topscorers",
        "header":{"x-apisports-key": _api_key_},
        "params":{
        "league": league_id,
        "season": season
            },
        
    }
    

def params_assist(league_id:int,season:int):
        return {
        "url":"https://v3.football.api-sports.io/players/topassists",
        "header":{"x-apisports-key": _api_key_},
        "params":{
        "league": league_id,
        "season": season
            },
        
    }
    


def params_team_stitics(league_id:int, season:int,team_id:int):
            return {
        "url":"https://v3.football.api-sports.io/teams/statistics",
        "header":{"x-apisports-key": _api_key_},
        "params":{
        "league": league_id,
        "season": season,
        "team_id":team_id
            },
        
    }
            
            
def params_team_squed(team_id:int,season:int):
        return {
        "url":"https://v3.football.api-sports.io/players/squads",
        "header":{"x-apisports-key": _api_key_},
        "params":{
        "team_id": team_id,
        "season": season
            },
        
    }
        
        
        
def params_transfer_team(team_id):
        return {
        "url":"https://v3.football.api-sports.io/transfers",
        "header":{"x-apisports-key": _api_key_},
        "params":{
        "team_id": team_id,
            }, 
    }
        
