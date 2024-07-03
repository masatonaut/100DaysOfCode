## Rain Alert System

This Rain Alert System is a Python application that uses the OpenWeatherMap API to check for rain in your specified location and sends an SMS alert via Twilio if rain is expected. It's a practical tool for reminding you to carry an umbrella if the weather is going to be rainy.

### Features

- Fetches weather data from the OpenWeatherMap API.
- Analyzes the weather data to determine if it's going to rain within the next few hours.
- Sends an SMS notification to a specified phone number if rain is detected.

### Prerequisites

- Python 3.x installed on your machine.
- An account and API key from OpenWeatherMap.
- An account and a verified phone number from Twilio along with a Twilio virtual phone number.

### Installation

1. **Clone the repository**:

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install required Python packages**:
   ```bash
   pip install requests twilio
   ```

### Configuration

1. **Set up OpenWeatherMap API**:

   - Sign up at [OpenWeatherMap](https://openweathermap.org/) and obtain an API key.
   - Insert your API key in the `api_key` variable in the script.

2. **Set up Twilio SMS Service**:
   - Sign up at [Twilio](https://www.twilio.com/) and get your Account SID and Auth Token.
   - Buy a Twilio virtual phone number and verify your real phone number to receive SMS.
   - Insert the Account SID, Auth Token, and phone numbers in the corresponding variables in the script.

### Usage

To run the program, navigate to the directory containing the script and run:

```bash
python rain_alert.py
```

The script will periodically check the weather in the specified location and send an SMS if rain is detected.

### Code Explanation

- **OpenWeatherMap API Integration**:

  - Uses the `requests` library to send HTTP requests to the OpenWeatherMap API.
  - Retrieves weather forecast data based on latitude and longitude.

- **Weather Analysis**:

  - Parses the JSON response to check for weather conditions.
  - Looks for weather condition codes less than 700 which indicate precipitation.

- **Twilio SMS Integration**:
  - Uses the Twilio `Client` to send SMS messages.
  - Configurable message body and recipient.

### Troubleshooting

- Ensure that your API keys and phone numbers are correctly set up and that you have adequate permissions and credits in both OpenWeatherMap and Twilio accounts.
- Check for any error messages in the console, which might indicate issues with the API requests or the response handling.
