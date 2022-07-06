import requests
from bs4 import BeautifulSoup

res=requests.get('https://joytas.net/kaba/')
res.encoding=res.apparent_encoding

soup=BeautifulSoup(res.text,'html.parser')

print(soup)
ele=soup.find('title') #<title>コビトカバ</title>

print(ele.text)

imgs=soup.find_all('img')
for img in imgs:
    print(img.get('src'))

div=soup.find(id='headerImageBox')

imgs=soup.select('.headerImage')
for img in imgs:
    print(img.get('src'))


names=soup.select('tr td:first-child')
for name in names:
    print(name.text)
