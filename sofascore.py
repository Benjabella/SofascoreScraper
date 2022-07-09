import requests
import json
import pandas as pd
from datetime import date

today = date.today()

url = (f"https://api.sofascore.com/api/v1/sport/football/scheduled-events/{today}")

headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0',
  'Accept': '*/*',
  'Accept-Language': 'en-US,en;q=0.5',
  'Accept-Encoding': 'gzip, deflate, br',
  'Referer': 'https://www.sofascore.com/',
  'Origin': 'https://www.sofascore.com',
  'Connection': 'keep-alive',
  'Sec-Fetch-Dest': 'empty',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Site': 'same-site',
  'If-None-Match': 'W/31652024eb',
  'Cache-Control': 'max-age=0',
  'TE': 'trailers'
}

r = requests.get(url, headers=headers)

data = r.json()

df = pd.json_normalize(data['events'])

df.to_csv(f'sofascore_{today}.csv', index=False)

