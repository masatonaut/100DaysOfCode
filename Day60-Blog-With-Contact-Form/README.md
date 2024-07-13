# Flask Blog Application with Contact Form

This project is a simple blog website built with Flask that allows users to view blog posts and send messages via a contact form. The messages are sent to a specified email address using SMTP.

## Features

- **View Blog Posts**: Displays a list of blog posts retrieved from an external API.
- **View Individual Post**: Allows users to view the full content of individual blog posts.
- **About Page**: Static page with information about the blog.
- **Contact Form**: Allows users to send a message, which is then emailed to a specified address.

## Requirements

- Python 3.x
- Flask 2.3.2
- Requests 2.31.0

## Setup

1. **Clone the repository**:

   ```sh
   git clone https://github.com/your-repository.git
   cd your-repository
   ```

2. **Create and activate a virtual environment**:

   ```sh
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install the required packages**:

   ```sh
   pip install -r requirements.txt
   ```

4. **Set up your email credentials**:

   Open `app.py` and replace the placeholders with your email address and password:

   ```python
   OWN_EMAIL = "YOUR OWN EMAIL ADDRESS"
   OWN_PASSWORD = "YOUR EMAIL ADDRESS PASSWORD"
   ```

5. **Run the application**:

   ```sh
   python app.py
   ```

6. **Access the application**:

   Open your web browser and navigate to `http://127.0.0.1:5001/`.

## Usage

- **Home Page**: Displays a list of blog posts. Click on a post title to view the full content.
- **About Page**: Provides information about the blog.
- **Contact Page**: Send a message via the contact form. Messages are sent to the email address specified in the `OWN_EMAIL` variable.
