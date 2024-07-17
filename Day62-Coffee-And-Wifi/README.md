# Coffee And Wifi

A Flask web application to manage and display information about cafes, including their location, opening hours, coffee ratings, wifi strength, and power socket availability.

## Features

- **Home Page**: Welcome page with navigation links.
- **Add Cafe**: Form to add a new cafe to the database.
- **View Cafes**: Display a list of all cafes with details.

## Requirements

- Python 3.x
- Flask
- Flask-WTF
- WTForms
- Flask-Bootstrap (Bootstrap-Flask)
- Email-validator

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/coffee-and-wifi.git
   cd coffee-and-wifi
   ```

2. Create a virtual environment and activate it:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:

   ```bash
   python app.py
   ```

2. Open your web browser and go to:
   ```
   http://127.0.0.1:5002
   ```

## Project Structure

- `app.py`: Main application file containing routes and form handling logic.
- `static/`: Directory for static files like CSS and JS.
  - `css/`: Contains stylesheets.
- `templates/`: Directory containing HTML templates.
  - `base.html`: Base template with common layout.
  - `index.html`: Home page template.
  - `add.html`: Form template for adding new cafes.
  - `cafes.html`: Template to display the list of cafes.

## Templates

### Base Template (`base.html`)

Defines the basic structure and includes blocks for title and content that can be overridden in child templates.

### Home Template (`index.html`)

Displays a welcome message and navigation links.

### Add Cafe Template (`add.html`)

Contains a form for adding new cafe information, rendered using Flask-Bootstrap's `render_form`.

### Cafes Template (`cafes.html`)

Displays a table of all cafes with details like name, location (with a link to Google Maps), opening and closing times, coffee rating, wifi strength, and power socket availability.
