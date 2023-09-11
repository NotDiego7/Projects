import requests, smtplib
from datetime import datetime, timedelta
from os import environ

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

ALPHAVANTAGE_KEY = "RQ4DYKJI3UA43XLX"
NEWS_KEY = "51b4fb2fe194489f91073ad8e50860fc"

GMAIL_SMTP_PASS = environ.get("GMAIL_SMTP_PASS")

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between two_days_ago and the day before two_days_ago then print("Get News").
# NOTE: Need market close from 2 days ago and market close from two_days_ago

# --------------------------------- Get Dates -------------------------------- #
two_days_ago = datetime.now().date() - timedelta(days = 2)

if two_days_ago.weekday() > 4: # If it was a weekend day
    if two_days_ago.weekday() == 5:
        focus_date = two_days_ago - timedelta(days = 2)
        second_focus_date = two_days_ago - timedelta(days = 3)

    elif two_days_ago.weekday() == 6:
        focus_date = two_days_ago - timedelta(days = 3)
        second_focus_date = two_days_ago - timedelta(days = 4)
else:
    focus_date = two_days_ago
    second_focus_date = two_days_ago - timedelta(days = 1)

# ------------------------- Get Dates' Closing Values ------------------------ #
alpha_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": ALPHAVANTAGE_KEY,
}

url = 'https://www.alphavantage.co/query'

endpoint_response = requests.get(url= url, params= alpha_params)
endpoint_response.raise_for_status()
tesla_stock_data = endpoint_response.json()

focus_date_closing = float(tesla_stock_data["Time Series (Daily)"][str(focus_date)]["4. close"])
second_focus_date_closing = float(tesla_stock_data["Time Series (Daily)"][str(second_focus_date)]["4. close"])

# ----------------- Check Differences Between Closing Values ----------------- #
perc_change = round((second_focus_date_closing - focus_date_closing) / focus_date_closing * 100, 2)
if perc_change > 0:
    perc_change = f"UP {perc_change}%"
elif perc_change < 0:
    perc_change = f"DOWN {perc_change}%"

# if perc_change > 0 or perc_change < 0: #TODO: Need to readjust to 5 and -5

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
news_params = {
    "apiKey": NEWS_KEY,
    "q": '+Trump,"Trump 2024",Donald Trump', #TODO: {COMPANY_NAME}, Tesla, {STOCK}
}

endpoint_response = requests.get(url= "https://newsapi.org/v2/everything", params= news_params)
endpoint_response.raise_for_status()
tesla_breaking_news = endpoint_response.json()
top_three = tesla_breaking_news["articles"][:3]

for article in top_three:
    headline = article["title"]
    brief = article["description"]
    url = article["url"]

## STEP 3: Use SMTP
# Send a seperate email with the percentage change and each article's title and description to your email. 

    with smtplib.SMTP(host= "smtp.gmail.com", port= 587) as connection:
        connection.starttls()
        connection.login("Diego007lopez@gmail.com", GMAIL_SMTP_PASS)
        connection.sendmail(from_addr= "TheDog", to_addrs= "Lopez.d9@outlook.com", msg= f"Subject: {headline}\n\n{brief}\n\n{url}\n\nBitch-ass Stank Jocelyn, figured out how to automize sending you Trump news on the daily LMAO JK".encode('utf-8'))


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

