import requests

def get_standings(league_id, season):
    url = "https://v3.football.api-sports.io/standings"
    headers = {
        "x-apisports-key": "2be8169e016e5c7cc5379ec0405defb6"
    }
    params = {
        "league": league_id,
        "season": season
    }

    response = requests.get(url, headers=headers, params=params)
    data = response.json()

    if "response" in data and data['response']:
        import json 
        print(json.dumps(data,indent=4))

        
    else:
        print("No standings found for the league or an error occurred.")
        return []

# استبدل "YOUR_API_KEY" بمفتاح API الخاص بك و"league_id" بمعرف دوري أبطال أفريقيا و"season" بالموسم الذي تريده
standings = get_standings(league_id=39, season=2024)


