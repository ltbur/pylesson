import requests
import json
from pprint import pprint

url = ('https://api.openweathermap.org/data/2.5/weather'
'?q={city}&appid={key}&lang=ja&units=metric')
url=url.format(city='Tokyo,JP',key='d95b92030af2acb1b3448bd2711aca79')
jsondata=requests.get(url).json()
pprint(jsondata)

