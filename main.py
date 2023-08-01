import requests
#import datetime

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
#TODAY = datetime.date.today()

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "QJZ19VGJ15RB65O6"

# Fetching yesterday's close price.
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}
response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
print(yesterday_closing_price)
#print(TODAY)

# Get the day before yesterday's closing stock price
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
print(day_before_yesterday_closing_price)

#Find the positive difference between 1. and 2.
difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))
print(difference)

#Workout the percentage in price between closing price yesterday and cosing price the day before yesterday
diff_percent = (difference / float(yesterday_closing_price)) * 100
print(diff_percent)

#If diff_percent is greater than 5 then print("Get News")
if diff_percent > 5:
    print("Get News")