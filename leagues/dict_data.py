from typing import Callable,List,Dict
def dict_data(futch_data: Callable) -> List[Dict]:
    data = futch_data()
    player_statistics = list(map(lambda i: {
        "id_player": i['player']['id'],
        "name": i['player']['name'],
        "photo": i['player']['photo'],
        "goal": i['statistics'][0]['goals']['total'],
        "assist": i['statistics'][0]['goals']['assists'],
        "shots": i['statistics'][0]['shots'],
        "minutes": i['statistics'][0]['games']['minutes'],
        "position": i['statistics'][0]['games']['position'],
        "passes": i['statistics'][0]['passes'],
        "tackles": i['statistics'][0]['tackles'],
        "dribbles_succ": i['statistics'][0]['dribbles']['success']
    }, data))
    return player_statistics
