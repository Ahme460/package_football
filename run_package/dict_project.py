from .manage_packge import *

class API_FOOTBALL:
    def __init__(self):
        
        self.managers = {
            "all_leagues": All_Leagues_M(),
            "important_matches": Matchs_M(),
            "normal_matches": Normal_Matchs_M(),
            "team_league": Team_league_M(),
            "table_league": Table_league_M(),
            "top_goal_player": Top_Goal_player_M(),
            "top_assist_player": Top_Assist_player_M(),
            "squad_teams": Squed_Teams_M(),
            "transfer_team": Transfer_team_M(),
        }

    def get_manager(self, key: str):
        """
        Retrieve the manager class instance by its key.
        """
        if key not in self.managers:
            raise KeyError(f"Manager '{key}' not found in API_FOOTBALL.")
        return self.managers[key]


    def get_all_leagues(self):
        return self.managers["all_leagues"].class_data()


    def get_important_matches(self, data: str):
        return self.managers["important_matches"](data).class_data()
    

    def get_normal_matches(self, data: str):
        return self.managers["normal_matches"](data).class_data()


    def get_teams_in_league(self, league_id: str, season: int):
        return self.managers["team_league"].class_data(league_id, season)

  
    def get_table_league(self, league_id: str, season: int):
        return self.managers["table_league"].class_data(league_id, season)


    def get_top_goal_players(self, league_id: int, season: int):
        return self.managers["top_goal_player"].class_data(league_id, season)


    def get_top_assist_players(self, league_id: int, season: int):
        return self.managers["top_assist_player"].class_data(league_id, season)


    def get_squad_teams(self, team_id: int, season: int):
        return self.managers["squad_teams"].class_data(team_id, season)


    def get_team_transfers(self, team_id: int):
        return self.managers["transfer_team"].class_data(team_id)