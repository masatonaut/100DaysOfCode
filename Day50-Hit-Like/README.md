# Tinder Auto-Like Script

This script automates the process of liking profiles on Tinder using Selenium WebDriver.

## Prerequisites

- Python 3.x
- Google Chrome browser
- ChromeDriver (compatible with your Chrome version)
- Selenium library

## Installation

1. **Clone the repository:**

   ```sh
   git clone https://github.com/yourusername/tinder-auto-like.git
   cd tinder-auto-like
   ```

2. **Install required packages:**

   ```sh
   pip install selenium
   ```

3. **Download ChromeDriver:**
   - [ChromeDriver Download](https://sites.google.com/chromium.org/driver/downloads)
   - Ensure the ChromeDriver is in your PATH or place it in the project directory.

## Configuration

1. **Update your login credentials:**
   - Open the script file and replace the placeholders with your Facebook login credentials:
     ```python
     FB_EMAIL = "YOUR FACEBOOK LOGIN EMAIL"
     FB_PASSWORD = "YOUR FACEBOOK PASSWORD"
     ```

## Usage

1. **Run the script:**

   ```sh
   python tinder_auto_like.py
   ```

2. **Follow the instructions:**
   - The script will open Tinder, log in via Facebook, and start liking profiles.
   - Solve any CAPTCHA manually when prompted.

## Script Workflow

1. **Open Tinder login page:**

   - The script navigates to Tinder's login page.

2. **Log in to Tinder using Facebook:**

   - The script enters your Facebook email and password to log in.

3. **Handle pop-ups:**

   - The script will allow location access, deny notifications, and accept cookies.

4. **Like profiles:**

   - The script will like 100 profiles, handling any pop-ups or errors that occur.

5. **Close the browser:**
   - After completing the likes, the script will close the browser.

## Notes

- Ensure that ChromeDriver is compatible with your Chrome version.
- Use responsibly and be aware of Tinder's terms of service.
