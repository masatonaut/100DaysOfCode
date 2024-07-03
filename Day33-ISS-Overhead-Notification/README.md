## ISS Overhead Notification Program

# Overview

This program checks if the International Space Station (ISS) is overhead your location and if it is currently night time at your location. If both conditions are met, it sends you an email notification to look up at the sky. The program uses APIs to get the ISS's current position and the sunrise/sunset times for your location. It runs continuously, checking the conditions every 60 seconds.

# Prerequisites

Before running the code, you need to update the following places in the script with your own information:

1. Replace `MY_EMAIL` and `MY_PASSWORD` with your own email and password.
2. Set `MY_LAT` and `MY_LONG` to your location's latitude and longitude.
3. Replace `__YOUR_SMTP_ADDRESS_HERE___` with your email provider's SMTP server address.

You also need to allow less secure apps to access your email account if required by your email provider.

# Instructions

1. **Clone the repository or download the script**.

2. **Install required libraries**:
   Ensure you have the `requests`, `datetime`, `smtplib`, and `time` libraries installed. You can install them using pip if necessary:

   ```bash
   pip install requests
   ```

3. **Update the script**:
   Open the script and replace the placeholder values with your own information:

   ```python
   MY_EMAIL = "your.email@example.com"
   MY_PASSWORD = "your_password"
   MY_LAT = 51.507351  # Your latitude
   MY_LONG = -0.127758  # Your longitude
   ```

4. **Run the script**:
   Execute the script using Python. The program will check the conditions every 60 seconds and send an email if the ISS is overhead and it's night time.

# Code Explanation

### Importing Necessary Libraries

```python
import requests
from datetime import datetime
import smtplib
import time
```

- `requests`: For making API requests.
- `datetime`: For handling date and time.
- `smtplib`: For sending emails.
- `time`: For adding delays between checks.

### Setting Up Variables

```python
MY_EMAIL = "your.email@example.com"
MY_PASSWORD = "your_password"
MY_LAT = 51.507351  # Your latitude
MY_LONG = -0.127758  # Your longitude
```

- `MY_EMAIL` and `MY_PASSWORD`: Your email and password for sending the notification email.
- `MY_LAT` and `MY_LONG`: Your location's latitude and longitude.

### Checking if the ISS is Overhead

```python
def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if (
        MY_LAT - 5 <= iss_latitude <= MY_LAT + 5
        and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5
    ):
        return True
```

- `requests.get`: Fetches the current position of the ISS.
- `response.raise_for_status()`: Checks if the API request was successful.
- `data.json()`: Parses the response as JSON.
- Checks if the ISS's latitude and longitude are within ±5 degrees of your location.

### Checking if it's Night Time

```python
def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True
```

- `requests.get`: Fetches the sunrise and sunset times for your location.
- Parses the response and extracts the sunrise and sunset times.
- Checks if the current time is between sunset and sunrise.

### Main Loop

```python
while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("smtp.example.com")
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject:Look Up👆\n\nThe ISS is above you in the sky.",
        )
```

- The script runs in an infinite loop, checking every 60 seconds.
- If the ISS is overhead and it's night time, sends an email notification.

# Running the Script

1. Ensure you have updated all the necessary variables in the script.
2. Run the script using Python:
   ```bash
   python iss_notification.py
   ```
3. The script will run continuously, sending you an email whenever the ISS is overhead and it's night time at your location.

### Notes

- Ensure you have a stable internet connection as the script makes API calls.
- Keep your email credentials secure. Consider using environment variables or a more secure method for storing credentials in a production environment.
- Test the script with different values for latitude and longitude to ensure it works correctly.
