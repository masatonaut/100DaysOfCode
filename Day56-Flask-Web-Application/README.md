# Flask Web Application

This project demonstrates a simple web application built with Flask. The application serves a static HTML page with a form and social media links.

## Prerequisites

- Python 3.x
- Flask

## Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/flask-web-app.git
   cd flask-web-app
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

## Project Structure

```
flask-web-app/
│
├── app.py
└── templates/
    └── index.html
```

## Usage

1. **Create the Python script (app.py):**
   ```python
   from flask import Flask, render_template

   app = Flask(__name__)

   @app.route('/')
   def home():
       return render_template('index.html')

   if __name__ == "__main__":
       app.run(debug=True)
   ```

2. **Create the HTML template (templates/index.html):**
   ```html
   <!DOCTYPE html>
   <html>
     <head>
       <title>Identity by HTML5 UP</title>
       <meta charset="utf-8" />
       <meta name="viewport" content="width=device-width, initial-scale=1" />
       <link rel="stylesheet" href="assets/css/main.css" />
       <noscript
         ><link rel="stylesheet" href="assets/css/noscript.css"
       /></noscript>
     </head>
     <body class="is-loading">
       <div id="wrapper">
         <section id="main">
           <header>
             <span class="avatar"><img src="images/avatar.jpg" alt="" /></span>
             <h1>Jane Doe</h1>
             <p>Senior Psychonautics Engineer</p>
           </header>
           <hr />
           <h2>Extra Stuff!</h2>
           <form method="post" action="#">
             <div class="field">
               <input type="text" name="name" id="name" placeholder="Name" />
             </div>
             <div class="field">
               <input type="email" name="email" id="email" placeholder="Email" />
             </div>
             <div class="field">
               <div class="select-wrapper">
                 <select name="department" id="department">
                   <option value="">Department</option>
                   <option value="sales">Sales</option>
                   <option value="tech">Tech Support</option>
                   <option value="null">/dev/null</option>
                 </select>
               </div>
             </div>
             <div class="field">
               <textarea
                 name="message"
                 id="message"
                 placeholder="Message"
                 rows="4"
               ></textarea>
             </div>
             <div class="field">
               <input type="checkbox" id="human" name="human" /><label for="human"
                 >I'm a human</label
               >
             </div>
             <div class="field">
               <label>But are you a robot?</label>
               <input type="radio" id="robot_yes" name="robot" /><label
                 for="robot_yes"
                 >Yes</label
               >
               <input type="radio" id="robot_no" name="robot" /><label
                 for="robot_no"
                 >No</label
               >
             </div>
             <ul class="actions">
               <li><a href="#" class="button">Get Started</a></li>
             </ul>
           </form>
           <hr />
           <footer>
             <ul class="icons">
               <li><a href="#" class="fa-twitter">Twitter</a></li>
               <li><a href="#" class="fa-instagram">Instagram</a></li>
               <li><a href="#" class="fa-facebook">Facebook</a></li>
             </ul>
           </footer>
         </section>
         <footer id="footer">
           <ul class="copyright">
             <li>&copy; Jane Doe</li>
             <li>Design: <a href="http://html5up.net">HTML5 UP</a></li>
           </ul>
         </footer>
       </div>
       <script>
         if ("addEventListener" in window) {
           window.addEventListener("load", function () {
             document.body.className = document.body.className.replace(
               /\bis-loading\b/,
               ""
             );
           });
           document.body.className += navigator.userAgent.match(/(MSIE|rv:11\.0)/)
             ? " is-ie"
             : "";
         }
       </script>
     </body>
   </html>
   ```

3. **Run the application:**
   ```sh
   python app.py
   ```

4. **Access the application:**
   Open your web browser and go to `http://127.0.0.1:5000/` to see the home page.