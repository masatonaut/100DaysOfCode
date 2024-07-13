# Cookie Clicker Automation Script

This script automates the "Cookie Clicker" game using Selenium WebDriver. It clicks the cookie, buys upgrades, and stops after 5 minutes to display the cookies per second (CPS).

## Prerequisites

- Python 3.x
- Google Chrome browser
- ChromeDriver (compatible with your Chrome version)
- Selenium library

## Installation

1. **Clone the repository:**

   ```sh
   git clone https://github.com/yourusername/cookie-clicker-automation.git
   cd cookie-clicker-automation
   ```

2. **Install required packages:**

   ```sh
   pip install selenium
   ```

3. **Download ChromeDriver:**
   - [ChromeDriver Download](https://sites.google.com/chromium.org/driver/downloads)
   - Ensure the ChromeDriver is in your PATH or place it in the project directory.

## Usage

1. **Run the script:**

   ```sh
   python cookie_clicker.py
   ```

2. **The script will:**
   - Open the Cookie Clicker game in Chrome.
   - Click the cookie to produce cookies.
   - Check for available upgrades every 5 seconds.
   - Purchase the most expensive affordable upgrade.
   - After 5 minutes, print the cookies per second (CPS) and stop.

## Code Overview

- **Initialization and Setup:**

  ```python
  from selenium import webdriver
  from selenium.webdriver.common.by import By
  import time

  chrome_options = webdriver.ChromeOptions()
  chrome_options.add_experimental_option("detach", True)
  driver = webdriver.Chrome(options=chrome_options)
  driver.get("http://orteil.dashnet.org/experiments/cookie/")
  ```

- **Main Automation Loop:**

  ```python
  cookie = driver.find_element(by=By.ID, value="cookie")
  items = driver.find_elements(by=By.CSS_SELECTOR, value="#store div")
  item_ids = [item.get_attribute("id") for item in items]

  timeout = time.time() + 5
  five_min = time.time() + 60 * 5

  while True:
      cookie.click()
      if time.time() > timeout:
          all_prices = driver.find_elements(by=By.CSS_SELECTOR, value="#store b")
          item_prices = []
          for price in all_prices:
              element_text = price.text
              if element_text != "":
                  cost = int(element_text.split("-")[1].strip().replace(",", ""))
                  item_prices.append(cost)

          cookie_upgrades = {}
          for n in range(len(item_prices)):
              cookie_upgrades[item_prices[n]] = item_ids[n]

          money_element = driver.find_element(by=By.ID, value="money").text
          if "," in money_element:
              money_element = money_element.replace(",", "")
          cookie_count = int(money_element)

          affordable_upgrades = {}
          for cost, id in cookie_upgrades.items():
              if cookie_count > cost:
                  affordable_upgrades[cost] = id

          highest_price_affordable_upgrade = max(affordable_upgrades)
          to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]
          driver.find_element(by=By.ID, value=to_purchase_id).click()
          timeout = time.time() + 5

      if time.time() > five_min:
          cookie_per_s = driver.find_element(by=By.ID, value="cps").text
          print(cookie_per_s)
          break
  ```

## Notes

- Ensure ChromeDriver is compatible with your Chrome version.
- Adjust the script timing and behavior as needed.
