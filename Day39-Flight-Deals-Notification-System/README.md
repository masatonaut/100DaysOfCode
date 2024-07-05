## Flight Deals Notification System

This project is designed to track and notify users of the cheapest flight deals available for specific destinations. The system fetches data from a Google Sheet, searches for flights using the Amadeus API, and sends notifications using Twilio when a cheaper flight is found.

### Table of Contents

1. [Prerequisites](#prerequisites)
2. [Setup](#setup)
3. [Usage](#usage)
4. [File Descriptions](#file-descriptions)
5. [Sample Data](#sample-data)

### Prerequisites

- Python 3.x
- Twilio Account
- Amadeus API Account
- Google Sheets with Sheety API

### Setup

1. Clone the repository:

   ```sh
   git clone https://github.com/yourusername/flight-deals-notification.git
   cd flight-deals-notification
   ```

2. Install the required Python packages:

   ```sh
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the root directory and add the following environment variables:
   ```plaintext
   TWILIO_SID=your_twilio_sid
   TWILIO_AUTH_TOKEN=your_twilio_auth_token
   TWILIO_VIRTUAL_NUMBER=your_twilio_virtual_number
   TWILIO_VERIFIED_NUMBER=your_verified_number
   TWILIO_WHATSAPP_NUMBER=your_twilio_whatsapp_number
   AMADEUS_API_KEY=your_amadeus_api_key
   AMADEUS_SECRET=your_amadeus_api_secret
   SHEETY_USERNAME=your_sheety_username
   SHEETY_PASSWORD=your_sheety_password
   SHEETY_PRICES_ENDPOINT=https://api.sheety.co/your_project/your_sheet/prices
   ```

### Usage

1. Ensure your Google Sheet is set up with columns for `city`, `iataCode`, and `lowestPrice`.

2. Run the main script:

   ```sh
   python main.py
   ```

   The script will:

   - Fetch destination data from the Google Sheet.
   - Update missing IATA codes.
   - Search for the cheapest flights.
   - Send notifications if a cheaper flight is found.

### File Descriptions

- **main.py**: The main script to run the flight search and notification process.
- **data_manager.py**: Contains the `DataManager` class for handling Google Sheet data.
- **flight_search.py**: Contains the `FlightSearch` class for interacting with the Amadeus API.
- **flight_data.py**: Contains the `find_cheapest_flight` function to find the cheapest flight.
- **notification_manager.py**: Contains the `NotificationManager` class for sending notifications via SMS and WhatsApp using Twilio.

### Sample Data

**Google Sheet Structure:**

| id  | city        | iataCode | lowestPrice |
| --- | ----------- | -------- | ----------- |
| 1   | London      | LON      | 300         |
| 2   | New York    | NYC      | 400         |
| 3   | Tokyo       | TYO      | 500         |
| 4   | Los Angeles |          | 350         |
| 5   | Paris       | PAR      | 250         |

**.env File:**

```plaintext
TWILIO_SID=your_twilio_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
TWILIO_VIRTUAL_NUMBER=+1234567890
TWILIO_VERIFIED_NUMBER=+0987654321
TWILIO_WHATSAPP_NUMBER=+1234567890
AMADEUS_API_KEY=your_amadeus_api_key
AMADEUS_SECRET=your_amadeus_api_secret
SHEETY_USERNAME=your_sheety_username
SHEETY_PASSWORD=your_sheety_password
SHEETY_PRICES_ENDPOINT=https://api.sheety.co/your_project/your_sheet/prices
```

### Explanation of Workflow

1. **Fetch Destination Data**: The script retrieves destination data from a Google Sheet using the Sheety API.
2. **Update IATA Codes**: If any destination is missing an IATA code, the script fetches it from the Amadeus API.
3. **Search for Flights**: The script searches for flights from the origin city to each destination for a period starting tomorrow and spanning six months.
4. **Find Cheapest Flight**: The `find_cheapest_flight` function identifies the lowest-priced flight for each destination.
5. **Send Notifications**: If a cheaper flight is found, a notification is sent via Twilio SMS or WhatsApp.

This system allows users to keep track of flight prices and get notified when better deals become available, ensuring they never miss out on the best prices.
