import requests
from datetime import datetime, timedelta

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_KEY = "JB66CGNJ57LA44LU"
NEWS_API_KEY = "3458a716fbcc44e7bfa94b03174e1c6b"

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY
}

response = requests.get(
    url="https://www.alphavantage.co/query", params=stock_parameters)
response.raise_for_status()
stock_data = response.json()["Time Series (Daily)"]

yesterday = datetime.now() - timedelta(1)
day_before_yesterday = datetime.now() - timedelta(2)

yesterday_close = float(stock_data[str(yesterday.date())]["4. close"])
day_before_yesterday_close = float(
    stock_data[str(day_before_yesterday.date())]["4. close"])


if abs(((yesterday_close - day_before_yesterday_close)/yesterday_close)*100) < 5:
    new_parameters = {
        'qInTitle': COMPANY_NAME,
        'apiKey': NEWS_API_KEY
    }

    res = requests.get(
        url="https://newsapi.org/v2/top-headlines", params=new_parameters)
    res.raise_for_status()
    articles = res.json()['articles']
    three_articles = articles[:3]
    print(three_articles)


