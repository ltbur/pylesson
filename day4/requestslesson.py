import requests
response= requests.get('https://www.python.org/downloads/')
text = response.text
print(text)
