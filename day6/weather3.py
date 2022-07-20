import requests
import json
from datetime import datetime,timedelta,timezone

url = ('https://api.openweathermap.org/data/2.5/forecast'
'?q={city}&appid={key}&lang=ja&units=metric')
url=url.format(city='Shibuya,JP',key='d95b92030af2acb1b3448bd2711aca79')
jsondata=requests.get(url).json()

#timezoneを日本に変更
tz=timezone(timedelta(hours = +9),'JST')
for dat in jsondata['list']:
    jst=str(datetime.fromtimestamp(dat['dt'],tz))[:-9]
    weather=dat['weather'][0]['description']
    temp=dat['main']['temp']
    print(f'日時:{jst},天気:{weather},気温:{temp}℃')
