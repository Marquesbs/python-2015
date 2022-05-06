import requests
from bs4 import BeautifulSoup

url = 'https://som13.com.br/coldplay/albums'
page = requests.get (url)
bs = BeautifulSoup (page.content, 'html.parser')
lista=bs.findAll("p", ("class":"tit"))
for item in lista:
    print (item.getText(' '))
