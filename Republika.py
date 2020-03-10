import requests
from bs4 import BeautifulSoup
import datetime
import json

republika={
    "time":"",
    "category":"",
    "title":"",
    "publish":""
}

data = []

page = requests.get("https://republika.co.id/")
obj = BeautifulSoup(page.text,'html.parser');


for headline in obj.find_all('div', class_='conten1'):
    republika["category"] = headline.find('h1').text
    republika["title"] = headline.find('h2').text
    date = datetime.datetime.now()
    today = date.strftime("%A")+", "+date.strftime("%d")+" "+date.strftime("%B")+" "+date.strftime("%Y")
    republika["time"] = today
    republika["publish"] = headline.find('div', class_='date').text


    data.append(dict(republika))


with open("I:\\Republika.json", "w") as file:
    json.dump(data, file)