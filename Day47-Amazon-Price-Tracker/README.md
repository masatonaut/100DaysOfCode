# Amazon Price Tracker

This script tracks the price of an Amazon product and sends an email alert when the price falls below a specified threshold.

## Prerequisites

- Python 3.6+
- Amazon product URL
- SMTP email account (e.g., Gmail)

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/yourusername/amazon-price-tracker.git
   cd amazon-price-tracker
   ```

2. Install required packages:

   ```sh
   pip install requests beautifulsoup4
   ```

3. Set up your environment variables:
   - Create a `.env` file in the project directory and add your SMTP credentials:
     ```env
     SMTP_ADDRESS=smtp.gmail.com
     EMAIL=your_email@gmail.com
     PASSWORD=your_email_password
     ```

## Usage

1. Update the `URL` and `BUY_PRICE` in the script with the Amazon product URL and your desired buy price.

   ```python
   URL = "https://www.amazon.com/dp/B08J4F1VGK"
   BUY_PRICE = 200
   ```

2. Run the script:

   ```sh
   python price_tracker.py
   ```

3. If the product price is below the `BUY_PRICE`, an email alert will be sent to the specified email address.

## Example

1. When you run the script, it will check the current price of the product:

   ```
   Example Product Title
   180.0
   ```

2. If the price is below `BUY_PRICE`, you will receive an email alert:

   ```
   Subject: Amazon Price Alert!

   Example Product Title is now $180
   https://www.amazon.com/dp/B08J4F1VGK
   ```

## Notes

- Ensure that you have allowed "Less secure app access" for your Gmail account if you are using Gmail for SMTP.
