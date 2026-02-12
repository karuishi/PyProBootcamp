import requests
import os
from twilio.rest import Client

VIRTUAL_NUMBER = "+16206757407"
MY_NUMBER = "+5571988360935"
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_Endpoint = "https://www.alphavantage.co/query"
NEWS_Endpoint = "https://newsapi.org/v2/everything"

stock_api_key = os.environ.get("STOCK_API_KEY")
news_api_key = os.environ.get("NEWS_API_KEY")
account_sid = os.environ.get("ACC_SID")
auth_token = os.environ.get("AUTH_TOKEN")

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "outputsize": "compact",
    "apikey": stock_api_key,
}

stock_response = requests.get(STOCK_Endpoint, stock_params)
stock_data = stock_response.json()["Time Series (Daily)"]
stock_data_list = [value for (key, value) in stock_data.items()]

yesterday_data = stock_data_list[0]
yesterday_closing_price = yesterday_data["4. close"]

day_before_yesterday_data = stock_data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]

difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
diff_percent = round((difference / float(yesterday_closing_price)) * 100)
up_down = "🔺" if difference > 0 else "🔻"

if abs(difference) > 5:
    news_params = {
        "qInTitle": COMPANY_NAME,
        "apiKey": news_api_key,
    }
    news_response = requests.get(NEWS_Endpoint, news_params)
    news_articles = news_response.json()["articles"] 
    recent_articles = news_articles[:3]
    
    client = Client(account_sid, auth_token)
    for article in recent_articles:
        headline = article["title"]
        brief = article["description"]
        
        msg_body = (
            f"{STOCK}: {up_down}{abs(difference)}%\n"
            f"Headline: {headline}\n"
            f"Brief: {brief}"
        )
        message = client.messages.create(
            body=msg_body,
            from_=VIRTUAL_NUMBER,
            to=MY_NUMBER,
        )
        print(message.status)


## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
    
## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 

#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

