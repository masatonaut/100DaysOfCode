## README

### Stock and News Alert System

This Python script monitors the stock price of Tesla Inc. (TSLA) and sends SMS alerts using Twilio when the stock price changes significantly. If the stock price changes by more than 5% between yesterday and the day before, the script retrieves the latest news articles about Tesla and sends them via SMS.

### Prerequisites

- Python 3.x
- Twilio account with a verified phone number and virtual phone number
- API keys for Alpha Vantage and News API

### Setup

1. **Clone the repository**:

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install required packages**:

   ```bash
   pip install requests twilio
   ```

3. **Configure the script**:
   - Replace placeholders with your actual API keys and Twilio credentials:
     ```python
     VIRTUAL_TWILIO_NUMBER = "your virtual twilio number"
     VERIFIED_NUMBER = "your own phone number verified with Twilio"
     STOCK_API_KEY = "YOUR OWN API KEY FROM ALPHAVANTAGE"
     NEWS_API_KEY = "YOUR OWN API KEY FROM NEWSAPI"
     TWILIO_SID = "YOUR TWILIO ACCOUNT SID"
     TWILIO_AUTH_TOKEN = "YOUR TWILIO AUTH TOKEN"
     ```

### Usage

Run the script:

```bash
python script_name.py
```

### How it Works

1. **Fetch Stock Data**:

   - The script uses the Alpha Vantage API to get the daily time series data for TSLA.
   - It calculates the percentage change between yesterday's and the day before yesterday's closing prices.

2. **Check for Significant Change**:

   - If the stock price changes by more than 5%, the script fetches the latest news articles about Tesla using the News API.

3. **Send SMS Alerts**:
   - The script formats the news articles and sends them as separate SMS messages using Twilio.

### Code Explanation

#### Fetch Stock Data

```python
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
```

- The script fetches the daily stock data for TSLA and extracts the closing prices for the last two days.

#### Calculate Percentage Change

```python
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
print(day_before_yesterday_closing_price)

difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
up_down = "🔺" if difference > 0 else "🔻"
diff_percent = round((difference / float(yesterday_closing_price)) * 100)
print(diff_percent)
```

- The script calculates the difference and percentage change between the two closing prices.

#### Fetch News Articles

```python
if abs(diff_percent) > 5:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]
    three_articles = articles[:3]
    print(three_articles)
```

- If the percentage change is greater than 5%, the script fetches the latest news articles about Tesla.

#### Send SMS Alerts

```python
formatted_articles = [f"{STOCK_NAME}: {up_down}{diff_percent}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]
print(formatted_articles)

client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

for article in formatted_articles:
    message = client.messages.create(
        body=article,
        from_=VIRTUAL_TWILIO_NUMBER,
        to=VERIFIED_NUMBER
    )
```

- The script formats the news articles and sends them as separate SMS messages using Twilio.

### Conclusion

This script provides a simple way to monitor stock price changes and receive timely news updates via SMS. You can customize it to monitor different stocks or adjust the percentage change threshold as needed.
