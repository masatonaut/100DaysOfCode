# Instagram Auto Follower Bot

This script automates the process of following followers of a specified Instagram account using Selenium WebDriver.

## Prerequisites

- Python 3.x
- Google Chrome browser
- ChromeDriver (compatible with your Chrome version)
- Selenium library

## Installation

1. **Clone the repository:**

   ```sh
   git clone https://github.com/yourusername/instagram-auto-follower-bot.git
   cd instagram-auto-follower-bot
   ```

2. **Install required packages:**

   ```sh
   pip install selenium
   ```

3. **Download ChromeDriver:**
   - [ChromeDriver Download](https://sites.google.com/chromium.org/driver/downloads)
   - Ensure the ChromeDriver is in your PATH or place it in the project directory.

## Configuration

1. **Update your login credentials and target account:**
   - Open the script file and replace the placeholders with your Instagram login credentials and the target account username:
     ```python
     SIMILAR_ACCOUNT = "target_account"
     USERNAME = "your_instagram_username"
     PASSWORD = "your_instagram_password"
     ```

## Usage

1. **Run the script:**
   ```sh
   python instagram_auto_follower_bot.py
   ```

## Script Workflow

1. **Login to Instagram:**

   - The script navigates to Instagram's login page, enters your credentials, and logs in.

2. **Navigate to the target account's followers page:**

   - The script goes to the followers page of the specified target account.

3. **Scroll the followers list:**

   - The script scrolls through the followers list to load more followers.

4. **Follow users:**
   - The script clicks the "Follow" button for each user in the followers list.
   - If a "Unfollow/Cancel" dialog appears, it handles it by clicking "Cancel".

## Notes

- Ensure that ChromeDriver is compatible with your Chrome version.
- Use responsibly and be aware of Instagram's terms of service to avoid account restrictions or bans.
