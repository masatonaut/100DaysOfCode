# Pixela Activity Tracker

This Python script uses the Pixela API to record daily activity data, specifically the distance cycled. The script sends an HTTP POST request to the Pixela API to add this data to a specified graph for a given user.

## Prerequisites

Ensure you have the following before running the script:

- Python 3.x installed on your machine
- `requests` library installed (`pip install requests`)

## Setup

1. **Clone the repository or download the script:**

   ```sh
   git clone https://github.com/yourusername/pixela-activity-tracker.git
   cd pixela-activity-tracker
   ```

2. **Install required libraries:**

   ```sh
   pip install requests
   ```

3. **Update the script with your Pixela credentials:**

   Open `tracker.py` and replace the placeholder values with your actual Pixela username, token, and graph ID.

   ```python
   USERNAME = "exampleuser"      # Replace with your Pixela username
   TOKEN = "exampletoken123"     # Replace with your Pixela token
   GRAPH_ID = "graph1"           # Replace with your Pixela graph ID
   ```

## Running the Script

1. **Execute the script:**

   ```sh
   python tracker.py
   ```

   The script will:

   - Get the current date.
   - Send a POST request to the Pixela API to record the cycling distance (set as 15.0 km in this example).

2. **Check the output:**

   If successful, you will see a response indicating success:

   ```json
   { "message": "Success.", "isSuccess": true }
   ```

   If there is an error, you will see an error message:

   ```json
   { "message": "Invalid date format.", "isSuccess": false }
   ```

## Script Explanation

Here’s a detailed explanation of what the script does:

1. **Import necessary libraries:**

   ```python
   import requests
   from datetime import datetime
   ```

2. **Set up user details and API endpoints:**

   ```python
   USERNAME = "exampleuser"
   TOKEN = "exampletoken123"
   GRAPH_ID = "graph1"
   pixela_endpoint = "https://pixe.la/v1/users"
   headers = {
       "X-USER-TOKEN": TOKEN
   }
   ```

3. **Create the pixel creation endpoint:**

   ```python
   pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
   ```

4. **Get the current date and set the activity data:**

   ```python
   today = datetime.now()
   pixel_data = {
       "date": today.strftime("%Y%m%d"),
       "quantity": "15.0",  # Sample data: 15 km cycled
   }
   ```

5. **Send the POST request to the Pixela API:**

   ```python
   response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
   print(response.text)
   ```

## Customizing the Script

- **Change the Activity Data:**

  You can modify the `quantity` value in `pixel_data` to reflect your actual activity data.

  ```python
  pixel_data = {
      "date": today.strftime("%Y%m%d"),
      "quantity": "20.0",  # Example: 20 km cycled
  }
  ```

- **Schedule the Script:**

  Use a task scheduler (like cron on Unix-based systems or Task Scheduler on Windows) to run this script daily to automatically log your activities.

## Troubleshooting

- **Invalid Token Error:**

  Ensure your Pixela token is correctly set in the `TOKEN` variable.

- **Graph Not Found:**

  Verify the `GRAPH_ID` is correct and that the graph exists in your Pixela account.

- **Date Format Error:**

  The date must be in `YYYYMMDD` format. Ensure the system date is correctly set.

## References

- [Pixela API Documentation](https://docs.pixe.la/)
