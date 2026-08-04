import requests
import os
from dotenv import load_dotenv
load_dotenv()
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

news_api=os.getenv("NEWS_API")

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
stock={
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK_NAME,
    "apikey":os.getenv("STOCK_API")
}
news_params={
    "apiKey":news_api,
    "qInTitle":COMPANY_NAME,
}

response=requests.get(url=STOCK_ENDPOINT,params=stock)
response.raise_for_status()
data=response.json()["Time Series (Daily)"]
data_list=[value for (key,value) in data.items()]
yesturday_data=data_list[0]
yesturday_closing_price=yesturday_data["4. close"]
print(yesturday_closing_price)
day_before_yesturday=data_list[1]
day_before_yesturday_closing_price=day_before_yesturday["4. close"]
print(day_before_yesturday_closing_price)
difference=abs((float(yesturday_closing_price)-float(day_before_yesturday_closing_price)))
diff_percent =(difference/ float(yesturday_closing_price)) *100
print(diff_percent)

news_response = requests.get(url=NEWS_ENDPOINT, params=news_params)
articles = news_response.json()["articles"]
three_articles = articles[:3]
formatted_articles = [
    f"Headline: {article['title']}\nBrief: {article['description']}"
    for article in three_articles
]
if diff_percent >5:
    for article in formatted_articles:
        print(article)
    

