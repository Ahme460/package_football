from leagues.model import Player

class Player_transfer(Player):
    def __init__(self,id_player,name,photo,team,team_out,price_transfer,date):
        self.id=id_player
        self.name=name
        self.photo=photo
        self.team:dict=team
        self.team_out:dict=team_out
        self.price=price_transfer
        self.date=date



