# LinkedIn Job Application Automation

This script automates the process of applying for jobs on LinkedIn using Selenium WebDriver.

## Prerequisites

- Python 3.x
- Google Chrome browser
- ChromeDriver (compatible with your Chrome version)
- Selenium library

## Installation

1. **Clone the repository:**

   ```sh
   git clone https://github.com/yourusername/linkedin-job-automation.git
   cd linkedin-job-automation
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
   - Open the script file and replace the placeholders with your LinkedIn login credentials and phone number:
     ```python
     ACCOUNT_EMAIL = "YOUR LOGIN EMAIL"
     ACCOUNT_PASSWORD = "YOUR LOGIN PASSWORD"
     PHONE = "YOUR PHONE NUMBER"
     ```

## Usage

1. **Run the script:**

   ```sh
   python linkedin_job_apply.py
   ```

2. **Follow the instructions:**
   - The script will open LinkedIn, log in, and start applying for jobs.
   - You will need to manually solve the CAPTCHA when prompted.

## Script Workflow

1. **Open LinkedIn job search page:**

   - The script navigates to a specific LinkedIn job search page.

2. **Log in to LinkedIn:**

   - The script enters your email and password to log in.

3. **Solve CAPTCHA:**

   - Manually solve the CAPTCHA and press Enter to continue.

4. **Apply for jobs:**

   - The script iterates through job listings, attempts to apply, and fills in your phone number if required.

5. **Handles complex applications:**

   - Skips applications that require additional steps beyond a simple form submission.

6. **Close the browser:**
   - After applying to the jobs, the script will close the browser.

## Notes

- Ensure that ChromeDriver is compatible with your Chrome version.
- The script is designed to handle simple job applications and may skip more complex forms.
- Use responsibly and be aware of LinkedIn's terms of service.
