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

import json

def get_match_statistics():
    url = f"https://v3.football.api-sports.io/fixtures/players"
    headers = {
        "x-apisports-key": "2be8169e016e5c7cc5379ec0405defb6"  # ضع مفتاح API الخاص بك هنا
    }
    params = {
        "fixture": 1208249  # معرف المباراة
    }

    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    print(json.dumps(data,indent=4))


get_match_statistics()

import requests
import json
from datetime import datetime, timedelta

def get_yesterday_fixture_id():
    # حساب تاريخ الأمس بشكل صحيح
    yesterday = datetime.now() - timedelta(days=4)
    yesterday_str = yesterday.strftime('%Y-%m-%d')

    url = "https://v3.football.api-sports.io/fixtures/players"
    headers = {
        "x-apisports-key": "2be8169e016e5c7cc5379ec0405defb6"  # ضع مفتاح API الخاص بك هنا
    }
    params = {
        "date": yesterday_str,
        "league": 39,  # الدوري الإنجليزي الممتاز مثلاً
        "season": 2024
    }

    response = requests.get(url, headers=headers, params=params)
    data = response.json()

    # طباعة الاستجابة للتحقق من البيانات
    print(json.dumps(data, indent=4))

    if "response" in data and data['response']:
        # الحصول على معرف المباراة الأولى في القائمة
        fixture_id = data['response'][0]['fixture']['id']
        print(f"Fixture ID for a match on {yesterday_str}: {fixture_id}")
        return fixture_id
    else:
        print("No fixtures found for yesterday or an error occurred.")
        return None

