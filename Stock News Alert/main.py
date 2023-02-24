import requests
import smtplib

def get_news():
    NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
    NEWS_API = "API KEY"
    NEWS_PARAMS = {
        "apiKey": NEWS_API,
        "q": f"{COMPANY_NAME} or Exxon OR XOM",
        "from": YESTERDAY,
        "to": TODAY,
        "sortBy": "popularity",
        "language": "en",
        "pageSize": 30,
        "page": 1,
    }

    news_response = requests.get(NEWS_ENDPOINT, params=NEWS_PARAMS)
    news_data = news_response.json()
    news_list = news_data["articles"][:3]
    return [(news["title"], news["description"]) for news in news_list]

def send_email_notification():
    my_email = "EMAIL"
    password = "PASS"

    for news in news_list:
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=my_email,
                msg=f"Subject: {STOCK}: {symbol} {price_change}%\n\n"
                    f"Headline: {news[0]}\n"
                    f"Brief: {news[1]}"
            )

# TODAY = dt.strptime("2023/02/21", '%Y/%m/%d').date()
TODAY = "2023-02-17"
YESTERDAY = "2023-02-16"

## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yerstday's closing stock price.

STOCK = "XOM"
COMPANY_NAME = "Exxon Mobil"
CLOSE_TIME = "16:00:00"
CLOSE_KEY = "4. close"

SERIES = "Time Series (30min)"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API_KEY = "API KEY"
STOCK_PARAMS = {
    "function": "TIME_SERIES_INTRADAY",
    "symbol": STOCK,
    "interval": "30min",
    "outputsize": "compact",
    "datatype": "json",
    "apikey": STOCK_API_KEY,
}

stock_response = requests.get(STOCK_ENDPOINT, params=STOCK_PARAMS)
stock_response.raise_for_status()
stock_data = stock_response.json()
today_closing_price = float(stock_data[SERIES][TODAY +" " + CLOSE_TIME][CLOSE_KEY])
yesterday_closing_price = float(stock_data[SERIES][YESTERDAY +" " + CLOSE_TIME][CLOSE_KEY])
price_change = round((today_closing_price-yesterday_closing_price)/yesterday_closing_price * 100, 2)

if price_change >= 3 or price_change <= -3:
    news_list = get_news()
    if price_change >= 3:
        symbol = "UP"
    if price_change <= -3:
        symbol = "DOWN"
    send_email_notification()




## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
#HINT 1: Think about using the Python Slice Operator



## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
#HINT 1: Consider using a List Comprehension.



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

