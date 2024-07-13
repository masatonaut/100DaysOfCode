# My Flask Blog

This project is a simple blog application built using Flask. It retrieves blog posts from an external API and displays them on a webpage. Users can click on individual posts to see the full content.

## Prerequisites

- Python 3.x
- Virtual environment (recommended)

## Installation

1. **Clone the repository:**

   ```sh
   git clone https://github.com/yourusername/my-flask-blog.git
   cd my-flask-blog
   ```

2. **Create a virtual environment and activate it:**

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages:**
   ```sh
   pip install Flask requests
   ```

## Project Structure

```
my_flask_blog/
│
├── app.py
├── post.py
├── static/
│   └── css/
│       └── styles.css
└── templates/
    ├── index.html
    └── post.html
```

## Usage

1. **Create the necessary files:**

   - `app.py`

     ```python
     from flask import Flask, render_template
     from post import Post
     import requests

     posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
     post_objects = []
     for post in posts:
         post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
         post_objects.append(post_obj)

     app = Flask(__name__)

     @app.route('/')
     def get_all_posts():
         return render_template("index.html", all_posts=post_objects)

     @app.route("/post/<int:index>")
     def show_post(index):
         requested_post = None
         for blog_post in post_objects:
             if blog_post.id == index:
                 requested_post = blog_post
         return render_template("post.html", post=requested_post)

     if __name__ == "__main__":
         app.run(debug=True)
     ```

   - `post.py`

     ```python
     class Post:
         def __init__(self, post_id, title, subtitle, body):
             self.id = post_id
             self.title = title
             self.subtitle = subtitle
             self.body = body
     ```

   - `templates/index.html`

     ```html
     <!DOCTYPE html>
     <html lang="en">
       <head>
         <meta charset="UTF-8" />
         <title>My Blog</title>
         <link
           href="https://fonts.googleapis.com/css2?family=Raleway"
           rel="stylesheet"
         />
         <link rel="stylesheet" href="../static/css/styles.css" />
       </head>
       <body>
         <div class="wrapper">
           <div class="top">
             <div class="title"><h1>My Blog</h1></div>
           </div>

           {% for post in all_posts %}
           <div class="content">
             <div class="card">
               <h2>{{ post.title }}</h2>
               <p>{{ post.subtitle }}</p>
               <a href="{{ url_for('show_post', index=post.id) }}">Read</a>
             </div>
           </div>
           {% endfor %}
         </div>
       </body>
       <footer>
         <p>Made with ♥️ in London.</p>
       </footer>
     </html>
     ```

   - `templates/post.html`

     ```html
     <!DOCTYPE html>
     <html lang="en">
       <head>
         <meta charset="UTF-8" />
         <title>{{ post.title }}</title>
         <link
           href="https://fonts.googleapis.com/css2?family=Raleway"
           rel="stylesheet"
         />
         <link rel="stylesheet" href="../static/css/styles.css" />
       </head>
       <body>
         <div class="wrapper">
           <div class="top">
             <div class="title"><h1>{{ post.title }}</h1></div>
           </div>
           <div class="content">
             <div class="card">
               <h2>{{ post.subtitle }}</h2>
               <p>{{ post.body }}</p>
             </div>
           </div>
         </div>
       </body>
       <footer>
         <p>Made with ♥️ in London.</p>
       </footer>
     </html>
     ```

   - `static/css/styles.css`

     ```css
     body {
       font-family: "Raleway", sans-serif;
       background-color: #f8f9fa;
       margin: 0;
       padding: 0;
       color: #333;
     }

     .wrapper {
       width: 80%;
       margin: auto;
       padding-top: 50px;
     }

     .top {
       text-align: center;
       margin-bottom: 30px;
     }

     .title h1 {
       margin: 0;
       font-size: 2.5em;
       color: #333;
     }

     .content {
       margin: 20px 0;
     }

     .card {
       background-color: #fff;
       border: 1px solid #ddd;
       padding: 20px;
       border-radius: 5px;
       box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
       margin-bottom: 20px;
     }

     .card h2 {
       margin-top: 0;
       font-size: 1.5em;
     }

     .card p {
       color: #777;
     }

     .card a {
       text-decoration: none;
       color: #007bff;
       font-weight: bold;
     }

     .card a:hover {
       text-decoration: underline;
     }

     footer {
       text-align: center;
       padding: 20px 0;
       font-size: 0.9em;
       color: #777;
     }
     ```

2. **Run the application:**

   ```sh
   python app.py
   ```

3. **Access the application:**
   Open your web browser and go to `http://127.0.0.1:5000/` to see the home page with the list of blog posts. Click on the "Read" link to view the full content of each post.
