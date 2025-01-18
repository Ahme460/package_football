from leagues.utils import Rquest

class Get_transfer_team(Rquest):
    def get_transfer_team(self,url,headers,params):
       return self.rquest_data(url,headers,params)

class Analysis_data:
    def transfer_price(self,txt):
        txt=txt.split()
        if len(txt) > 1:
            return txt[1]
        else:
            return txt

    def dict_data(self, futch_data: callable):
        data = futch_data()
        player_transfer = list(map(lambda i: {
            "id_player": i['player']['id'],
            "name": i['player']['name'],
            "photo": f"https://media.api-sports.io/football/players/{i['player']['id']}.png",
            "team": i['teams']['in'],
            "teams": i['teams']['out'],
            "price_transfer": self.transfer_price(i['transfers']['type']),
            "data": i['transfers']['date']
        }, data))
        return player_transfer




