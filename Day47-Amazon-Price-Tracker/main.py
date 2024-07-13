import requests
from bs4 import BeautifulSoup
import smtplib
import os

YOUR_SMTP_ADDRESS = os.getenv("SMTP_ADDRESS")
YOUR_EMAIL = os.getenv("EMAIL")
YOUR_PASSWORD = os.getenv("PASSWORD")

URL = "https://www.amazon.com/dp/B08J4F1VGK"
BUY_PRICE = 200

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}
response = requests.get(URL, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')

title = soup.find(id="productTitle").get_text().strip()
print(title)

price = soup.find(id="priceblock_ourprice").get_text().strip().replace('$', '').replace(',', '')
price_as_float = float(price)
print(price_as_float)

if price_as_float < BUY_PRICE:
    message = f"{title} is now ${price_as_float}"

    try:
        with smtplib.SMTP(YOUR_SMTP_ADDRESS, port=587) as connection:
            connection.starttls()
            connection.login(YOUR_EMAIL, YOUR_PASSWORD)
            connection.sendmail(
                from_addr=YOUR_EMAIL,
                to_addrs=YOUR_EMAIL,
                msg=f"Subject:Amazon Price Alert!\n\n{message}\n{URL}".encode("utf-8"),
            )
        print("Email sent successfully.")
    except Exception as e:
        print(f"Failed to send email: {e}")
