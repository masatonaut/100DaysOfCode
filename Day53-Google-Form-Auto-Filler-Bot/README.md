# Google Form Auto Filler Bot

This script automates the process of filling out a Google Form with real estate property information using Selenium.

## Prerequisites

- Python 3.x
- Google Chrome browser
- ChromeDriver (compatible with your Chrome version)
- Required Python packages:
  - BeautifulSoup4
  - Requests
  - Selenium

## Installation

1. **Clone the repository:**

   ```sh
   git clone https://github.com/yourusername/google-form-auto-filler.git
   cd google-form-auto-filler
   ```

2. **Install required packages:**

   ```sh
   pip install beautifulsoup4 requests selenium
   ```

3. **Download ChromeDriver:**
   - [ChromeDriver Download](https://sites.google.com/chromium.org/driver/downloads)
   - Ensure the ChromeDriver is in your PATH or place it in the project directory.

## Configuration

1. **Update the Google Form link:**
   - Open the script file and replace the placeholder `"YOUR_GOOGLE_FORM_LINK_HERE"` with your actual Google Form link.

## Usage

1. **Run the script:**
   ```sh
   python google_form_auto_filler.py
   ```

## Script Workflow

1. **Scrape real estate property data:**

   - The script uses BeautifulSoup to scrape links, addresses, and prices of rental properties from a Zillow clone website.

2. **Fill in the Google Form using Selenium:**
   - The script opens the Google Form in Chrome, and for each property, it fills in the address, price, and link, then submits the form.

## Notes

- Ensure that ChromeDriver is compatible with your Chrome version.
- Modify the XPath expressions in the script if your Google Form's structure is different.
- Use responsibly and be aware of Google Form's usage policies to avoid any restrictions.
