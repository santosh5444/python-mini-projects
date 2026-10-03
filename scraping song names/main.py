import requests
from bs4 import BeautifulSoup
date=input("enter year u want to travel in the yyyy-mm-dd format : ")
URL=f"https://appbrewery.github.io/bakeboard-hot-100/{date}/"
response=requests.get(URL)
print(response.status_code)
soup=BeautifulSoup(response.text,"html.parser")
songs=soup.find_all("h3")
for items in songs:
    print(items.get_text())
