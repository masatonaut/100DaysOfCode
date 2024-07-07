# Flight Deal Tracker

This Python project tracks flight prices and sends notifications when it finds a deal. It retrieves flight data, checks for the lowest prices, and sends alerts via SMS, WhatsApp, or email.

## Prerequisites

- Python 3.x
- Twilio account with verified phone number
- API keys for Amadeus and Sheety
- SMTP email server

## Installation

1. **Clone the repository**:

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Create a virtual environment (optional but recommended)**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install the required packages**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   Create a `.env` file in the project directory and add the following:

   ```plaintext
   SHEETY_USERNAME=your_sheety_username
   SHEETY_PASSWORD=your_sheety_password
   SHEETY_PRICES_ENDPOINT=https://api.sheety.co/your_project_endpoint/prices
   SHEETY_USERS_ENDPOINT=https://api.sheety.co/your_project_endpoint/users

   AMADEUS_API_KEY=your_amadeus_api_key
   AMADEUS_SECRET=your_amadeus_secret

   TWILIO_SID=your_twilio_sid
   TWILIO_AUTH_TOKEN=your_twilio_auth_token
   TWILIO_VIRTUAL_NUMBER=your_twilio_virtual_number
   TWILIO_VERIFIED_NUMBER=your_verified_phone_number
   TWILIO_WHATSAPP_NUMBER=your_twilio_whatsapp_number

   EMAIL_PROVIDER_SMTP_ADDRESS=smtp.your_email_provider.com
   MY_EMAIL=your_email_address
   MY_EMAIL_PASSWORD=your_email_password
   ```

5. **Set up Google Sheets**:
   - Create a sheet with columns: `city`, `iataCode`, `lowestPrice`.
   - Create another sheet for user emails.

## Usage

Run the program:

```bash
python main.py
```

## How It Works

1. **Data Retrieval**: Retrieves flight data from Google Sheets using the `DataManager` class.
2. **IATA Code Update**: Updates missing IATA codes using the `FlightSearch` class.
3. **Customer Email Retrieval**: Retrieves customer emails.
4. **Flight Search**: Searches for flights and identifies the cheapest options using the `FlightSearch` and `find_cheapest_flight` functions.
5. **Notification Sending**: Sends notifications via SMS, WhatsApp, or email using the `NotificationManager` class.
