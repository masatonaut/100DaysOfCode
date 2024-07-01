## Birthday Wisher: A Python Script for Sending Automated Birthday Emails

This Python script sends automated birthday wishes via email. It uses Pandas to manage birthday data, and smtplib to handle email sending. The script selects a birthday message template randomly and customizes it with the recipient's name before sending the email.

### Introduction

The Birthday Wisher script automates the process of sending birthday wishes via email. By reading a CSV file containing birthday information, the script identifies if today is someone's birthday and sends them a personalized birthday message.

### Features

- **Automated Birthday Emails**: Sends a personalized birthday email to individuals whose birthday is today.
- **Randomized Messages**: Selects a random birthday message template from available templates.
- **Email Customization**: Replaces placeholders in the template with the recipient's name.

### How to Use

1. **Setup Email Configuration**: Update the script with your email details and allow less secure app access.
2. **Prepare Birthday Data**: Ensure `birthdays.csv` is up-to-date with the relevant birthday information.
3. **Run the Script**: Execute the script to send out birthday emails.

### Prerequisites

- **Email Account**: An email account with less secure app access enabled.
- **SMTP Server Address**: The SMTP server address of your email provider.
- **Pandas Library**: Install Pandas for handling CSV files.
- **smtplib Library**: Included in Python's standard library for sending emails.

### Steps to Configure and Run

1. **Update Email Details**: Replace `MY_EMAIL` and `MY_PASSWORD` with your email address and password.
   ```python
   MY_EMAIL = "YOUR EMAIL"
   MY_PASSWORD = "YOUR PASSWORD"
   ```
2. **Enable Less Secure Apps**: Go to your email provider's settings and allow less secure apps.
3. **Set SMTP Server Address**: Update the SMTP server address to match your email provider.
   ```python
   with smtplib.SMTP("YOUR EMAIL PROVIDER SMTP SERVER ADDRESS") as connection:
   ```
4. **Prepare Birthday Data**: Update `birthdays.csv` to contain the correct month and day for today's date.
5. **Install Pandas**: If not already installed, install Pandas using pip:
   ```sh
   pip install pandas
   ```
6. **Run the Script**: Execute the script to send birthday emails:
   ```sh
   python main.py
   ```

### File Structure

- **birthdays.csv**: A CSV file containing birthday information. Ensure it includes columns for name, email, month, and day.
- **letter_templates**: A directory containing text files for birthday messages (e.g., `letter_1.txt`, `letter_2.txt`, `letter_3.txt`).

### Example `birthdays.csv`

```
name,email,month,day
John Doe,johndoe@example.com,6,30
Jane Smith,janesmith@example.com,12,25
```

### Example Letter Template (`letter_1.txt`)

```
Dear [NAME],

Wishing you a very Happy Birthday!

Best wishes,
Your Friend
```

### Detailed Code Explanation

#### Importing Libraries

```python
from datetime import datetime
import pandas
import random
import smtplib
```

- **datetime**: For getting the current date.
- **pandas**: For handling CSV data.
- **random**: For selecting a random birthday message template.
- **smtplib**: For sending emails.

#### Setting Up Email and Date Information

```python
MY_EMAIL = "YOUR EMAIL"
MY_PASSWORD = "YOUR PASSWORD"

today = datetime.now()
today_tuple = (today.month, today.day)
```

- **MY_EMAIL/MY_PASSWORD**: Your email credentials.
- **today**: Current date and time.
- **today_tuple**: Tuple containing the current month and day.

#### Reading and Processing Birthday Data

```python
data = pandas.read_csv("birthdays.csv")
birthdays_dict = {
    (data_row["month"], data_row["day"]): data_row
    for (index, data_row) in data.iterrows()
}
```

- **data**: Reads the birthday data from `birthdays.csv`.
- **birthdays_dict**: Dictionary mapping (month, day) tuples to corresponding birthday entries.

#### Checking for Birthdays and Sending Emails

```python
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("YOUR EMAIL PROVIDER SMTP SERVER ADDRESS") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{contents}",
        )
```

- **Checking for Birthdays**: If today's date matches any entry in `birthdays_dict`, proceed to send an email.
- **Selecting a Random Template**: Chooses a random letter template from the `letter_templates` directory.
- **Customizing the Message**: Replaces the `[NAME]` placeholder with the birthday person's name.
- **Sending the Email**: Logs into the email server and sends the customized birthday message.
