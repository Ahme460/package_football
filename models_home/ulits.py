from typing import Dict
from .constract import API_token
from requests import get
import json
import requests
#mEUhW8mVc1vmJLdg9sZNJ7NrYZuGyvXOvoPMa8UhAfn7NsyxxHwQPFcYj2TX
from datetime import datetime
import pytz 

def all_league():
    header: Dict = {
        "x-apisports-key": API_token  
    }
    url = "https://v3.football.api-sports.io/leagues"
    response = get(url=url, headers=header)
    data = response.json()
    leagues = data.get("response", [])
    return leagues[:2]

#print(all_league())


#https://api-football-v1.p.rapidapi.com/v3/fixtures?date=2025-01-07

# def mathcs_by_time(header:dict=None,params:dict=None,data:str=None):
#     header: Dict = {
#         "x-apisports-key": API_token  
#     }
#     url="https://api-football-v1.p.rapidapi.com/v3/fixtures"

#     params={
#         "data":data
#     }

#     response = get(url=url, headers=header,params=params)
#     data = response.json()
#     leagues = data.get("response", [])
#     print(leagues)

# mathcs_by_time()




# import requests

# url = "https://v3.football.api-sports.io/fixtures"
# headers = {
#     "x-apisports-key": API_token
# }
# params = {
#     "date": "2025-01-07",  # يمكنك تغيير التاريخ إلى اليوم الحالي
#     "season": "2024"
# }

# response = requests.get(url, headers=headers, params=params)
# data = response.json()
# for fixture in data['response']:
#         if fixture['league']['country']=='England' and fixture['league']['country']=='England':
#             print(f"Match: {fixture['teams']['home']['name']} vs {fixture['teams']['away']['name']}")
#             print(f"Date: {fixture['fixture']['date']}")
#             print(fixture['league'])
#             print("-" * 30)




def get_matchs_by_league():

    url = "https://v3.football.api-sports.io/fixtures"
    headers = {
        "x-apisports-key": API_token
    }
    params = {
    "date": "2025-01-05",  # يمكنك تغيير التاريخ إلى اليوم الحالي
    "league": "39",  # استبدل هذا بمعرف الدوري الذي تريده
    "season": "2024"
    }

    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    return data['response']

def get_time(time):
    match_time_utc = time
    # تحويل النص إلى كائن datetime
    utc_time = datetime.fromisoformat(match_time_utc)

    # تحديد المنطقة الزمنية المحلية
    local_timezone = pytz.timezone("Africa/Cairo")  # غيّرها لمنطقتك

    # تحويل التوقيت إلى المنطقة الزمنية المحلية
    local_time = utc_time.astimezone(local_timezone)

    # استخراج الساعة والدقيقة
    hour = local_time.strftime('%I')  # %I للحصول على الساعة بصيغة 12 ساعة
    minute = local_time.strftime('%M')  # للحصول على الدقائق
    am_pm = local_time.strftime('%p')  # AM أو PM

    return {
        "hour":hour,
        "minute":minute,
        "am_pm":am_pm
    }