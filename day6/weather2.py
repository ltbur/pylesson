import requests
import json

url = ('https://api.openweathermap.org/data/2.5/weather'
'?zip={zip}&appid={key}&lang=ja&units=metric')
url=url.format(zip='106-0032,JP',key='d95b92030af2acb1b3448bd2711aca79')
jsondata=requests.get(url).json()

print('都市名:',jsondata['name'])
print('気温:',jsondata['main']['temp'])
print('天気:',jsondata['weather'][0]['main'])
print('天気詳細:',jsondata['weather'][0]['description'])
