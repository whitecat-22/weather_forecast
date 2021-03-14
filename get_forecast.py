import requests
import json
import environ
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

env = environ.Env()
env.read_env(os.path.join(BASE_DIR, '.env'))
# APIキーの設定
API_KEY = env('API_KEY')

# 主要な都市名で取得可能
# city_name = "Ichikawa"
# "lon": 139.9247
# "lat": 35.7197
# api = "http://api.openweathermap.org/data/2.5/weather?units=metric&q={city}&APPID={key}"

api = "http://api.openweathermap.org/data/2.5/onecall?lat=35.7197&lon=139.9247&units=metric&lang=en&exclude=minutely,hourly&APPID={key}"

# url = api.format(city=city_name, key=API_KEY)
url = api.format(key=API_KEY)
# print(url)
response = requests.get(url)
data = response.json()
jsonText = json.dumps(data, indent=4)
print(jsonText)
