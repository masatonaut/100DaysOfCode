# Internet Speed Twitter Bot

This script automates the process of measuring your internet speed and tweeting a complaint to your internet service provider if the speed is below the promised values.

## Prerequisites

- Python 3.x
- Google Chrome browser
- ChromeDriver (compatible with your Chrome version)
- Selenium library

## Installation

1. **Clone the repository:**

   ```sh
   git clone https://github.com/yourusername/internet-speed-twitter-bot.git
   cd internet-speed-twitter-bot
   ```

2. **Install required packages:**

   ```sh
   pip install selenium
   ```

3. **Download ChromeDriver:**
   - [ChromeDriver Download](https://sites.google.com/chromium.org/driver/downloads)
   - Ensure the ChromeDriver is in your PATH or place it in the project directory.

## Configuration

1. **Update your login credentials and promised speeds:**
   - Open the script file and replace the placeholders with your Twitter login credentials and the promised internet speeds:
     ```python
     PROMISED_DOWN = 150
     PROMISED_UP = 10
     TWITTER_EMAIL = "YOUR TWITTER EMAIL"
     TWITTER_PASSWORD = "YOUR TWITTER PASSWORD"
     ```

## Usage

1. **Run the script:**
   ```sh
   python internet_speed_twitter_bot.py
   ```

## Script Workflow

1. **Measure internet speed:**

   - The script navigates to Speedtest.net and measures your internet speed.

2. **Log in to Twitter:**

   - The script logs in to your Twitter account using the provided credentials.

3. **Tweet complaint:**

   - If the measured speeds are below the promised values, the script composes and posts a tweet complaining about the slow speeds.

4. **Close the browser:**
   - The script closes the browser after tweeting the complaint.

## Notes

- Ensure that ChromeDriver is compatible with your Chrome version.
- Use responsibly and be aware of Twitter's terms of service.
