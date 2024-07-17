# Flask Secrets

This is a simple Flask web application with a login functionality. The application uses Flask-WTF for form handling and Flask-Bootstrap for styling.

## Features

- Home page with a welcome message
- Login page with email and password fields
- Validation for email and password inputs
- Success and Access Denied pages based on login credentials

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
   git clone https://github.com/yourusername/flask-login-app.git
   cd flask-login-app
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
   http://127.0.0.1:5001
   ```

## Project Structure

- `app.py`: The main application file containing routes and form handling logic.
- `templates/`: Directory containing HTML templates.
  - `base.html`: Base template with common layout.
  - `index.html`: Home page template.
  - `login.html`: Login page template.
  - `success.html`: Template shown on successful login.
  - `denied.html`: Template shown on access denied.
- `static/`: Directory for static files like CSS and JS (if any).

## Templates

### Base Template (`base.html`)

Defines the basic structure and includes blocks for title and content that can be overridden in child templates.

### Home Template (`index.html`)

Displays a welcome message and a link to the login page.

### Login Template (`login.html`)

Contains the login form, rendered using Flask-Bootstrap's `render_form`.

### Success Template (`success.html`)

Displayed when login is successful.

### Access Denied Template (`denied.html`)

Displayed when login credentials are incorrect.
