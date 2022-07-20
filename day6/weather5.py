import requests
import json
from datetime import datetime,timedelta,timezone
from pprint import pprint
import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib

url = ('https://api.openweathermap.org/data/2.5/forecast'
'?q={city}&appid={key}&lang=ja&units=metric')
url=url.format(city='Shibuya,JP',key='d95b92030af2acb1b3448bd2711aca79')
jsondata=requests.get(url).json()

df=pd.DataFrame(columns=['気温','湿度'])

#timezoneを日本に変更
tz=timezone(timedelta(hours = +9),'JST')
for dat in jsondata['list']:
    jst=str(datetime.fromtimestamp(dat['dt'],tz))[:-9]
    temp=dat['main']['temp']
    humidity=dat['main']['humidity']
    df.loc[jst]=[temp,humidity]

df.plot(figsize=(15,8))
plt.ylim(-10,100)
plt.grid()
plt.show()
