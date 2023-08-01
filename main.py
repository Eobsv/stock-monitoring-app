import requests
import smtplib
#import datetime

MY_EMAIL = "useyouremail"
MY_PASSWORD = "user your pass"
MY_RESPONDENT = "useyouremail"

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
#TODAY = datetime.date.today()

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "useyourkey"
NEWS_API_KEY = "useyourkey"

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

#If diff_percent is greater than 5 then get 3articles related to company name
if diff_percent > 0.25:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]
    three_articles = articles[:3]
    print(three_articles)

    titles_list = [f"Headline: {article['title']}. \n URL: {article['url']}" for article in three_articles]
    print(titles_list)


    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=MY_RESPONDENT,
                            msg=f"Subject: Latest articles on {COMPANY_NAME} due to recent stock changes\n\n"
                                f" {titles_list}")
