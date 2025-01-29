
def info_dict(data):
    fixture = data['response'][0]
    time = fixture['fixture']['date']
    stadium = fixture['fixture']['venue']['name']
    city = fixture['fixture']['venue']['city']
    referee = fixture['fixture']['referee']
    return {
        "time":time,
        "stadium":stadium,
        "city":city,
        "referee":referee,
    }



def statistics_mathc_dict(data,team):
    team_stats = data['response'][team]['statistics']
    stats = {stat['type']: stat['value'] for stat in team_stats}
    return {
        "shots_on_goal": stats.get('Shots on Goal', 0),
        "shots_off_goal": stats.get('Shots off Goal', 0),
        "shots_inside_box": stats.get('Shots insidebox', 0),
        "shots_outside_box": stats.get('Shots outsidebox', 0),
        "total_shots": stats.get('Total Shots', 0),
        "blocked_shots": stats.get('Blocked Shots', 0),
        "fouls": stats.get('Fouls', 0),
        "corner_kicks": stats.get('Corner Kicks', 0),
        "offsides": stats.get('Offsides', 0),
        "ball_possession": float(stats.get('Ball Possession', '0%').strip('%')),
        "yellow_cards": stats.get('Yellow Cards', 0),
        "red_cards": stats.get('Red Cards', 0),
        "goalkeeper_saves": stats.get('Goalkeeper Saves', 0),
        "total_passes": stats.get('Total passes', 0),
        "passes_accurate": stats.get('Passes accurate', 0),
        "passes_percentage": float(stats.get('Passes %', '0%').strip('%'))
    }


def event_mathc_dict(data):
    time=data['time']['elapsed']
    extra=time=data['time'].get('extra',0)
    if extra:
        time+=extra
    team=data['team']
    player_id=data['player']['id']
    player_name=data['player']['name']
    event_type=data['type']
    detal_event=data['detail']
    comments=data['comments']

    return {
        "time": time,
        "team": team,
        "player_id": player_id,
        "player_name": player_name,
        "event_type": event_type,
        "detal_event": detal_event,
        "comments": comments
    }

