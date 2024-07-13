# Simple Flask Web Application

This project demonstrates a basic Flask web application with two routes: one for the home page and one for a goodbye page.

## Prerequisites

- Python 3.x
- Flask

## Installation

1. **Clone the repository:**

   ```sh
   git clone https://github.com/yourusername/simple-flask-app.git
   cd simple-flask-app
   ```

2. **Create a virtual environment and activate it:**

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages:**
   ```sh
   pip install Flask
   ```

## Usage

1. **Run the application:**

   ```sh
   python app.py
   ```

2. **Access the application:**
   - Open your web browser and go to `http://127.0.0.1:5000/` to see the home page.
   - Go to `http://127.0.0.1:5000/bye` to see the goodbye page.

## Code Overview

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/bye')
def say_bye():
    return 'Bye'

if __name__ == "__main__":
    app.run()
```

### Explanation

- **Flask Initialization**:

  ```python
  app = Flask(__name__)
  ```

  Creates an instance of the Flask class.

- **Route Definitions**:

  ```python
  @app.route('/')
  def hello_world():
      return 'Hello, World!'
  ```

  Defines the root URL route that returns "Hello, World!".

  ```python
  @app.route('/bye')
  def say_bye():
      return 'Bye'
  ```

  Defines the `/bye` URL route that returns "Bye".

- **Run the Application**:
  ```python
  if __name__ == "__main__":
      app.run()
  ```
  Runs the Flask development server if the script is executed directly.

## License

This project is licensed under the MIT License.
