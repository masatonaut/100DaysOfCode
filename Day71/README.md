# Project Deployment Guide

This guide will help you deploy your project from development to production. Follow the steps below to ensure a smooth deployment process.

## Prerequisites

- Ensure you have a project ready for deployment.
- Have `git` installed and configured on your system.
- Sign up for a hosting provider that supports WSGI applications (e.g., Heroku, DigitalOcean).

## Steps

### 1. Add a `.gitignore` file

Create a `.gitignore` file to exclude unnecessary files from your version control. You can also download a pre-configured `.gitignore` file.

```sh
echo "venv/" >> .gitignore
echo "__pycache__/" >> .gitignore
echo ".env" >> .gitignore
```

### 2. Use Git for Version Control

Initialize a Git repository in your project directory and commit your changes.

```sh
git init
git add .
git commit -m "Initial commit"
```

### 3. Use Environment Variables

Store sensitive information, such as API keys and database URIs, in environment variables. Create a `.env` file and add your variables:

```sh
touch .env
echo "SECRET_KEY=your_secret_key" >> .env
echo "DATABASE_URL=your_database_url" >> .env
```

Ensure you load these variables in your application:

```python
from dotenv import load_dotenv
load_dotenv()
```

### 4. Setup a WSGI Server with Gunicorn

Install Gunicorn to serve your Flask application:

```sh
pip install gunicorn
```

Add a `Procfile` to specify how to run your application:

```sh
echo "web: gunicorn app:app" > Procfile
```

### 5. Push to Remote on GitHub

Create a repository on GitHub and push your project:

```sh
git remote add origin https://github.com/yourusername/your-repo.git
git branch -M main
git push -u origin main
```

### 6. Sign up for a Hosting Provider

Sign up for a hosting provider such as Heroku, and follow their instructions to deploy your project. For example, with Heroku:

```sh
heroku login
heroku create your-app-name
git push heroku main
```

### 7. Upgrade SQLite to PostgreSQL

If your project uses SQLite and you want to upgrade to PostgreSQL, follow these steps:

1. Install `psycopg2`:

   ```sh
   pip install psycopg2
   ```

2. Update your database URI in the `.env` file to use PostgreSQL:

   ```sh
   echo "DATABASE_URL=postgres://username:password@hostname:port/dbname" >> .env
   ```

3. Migrate your data from SQLite to PostgreSQL using a tool like `pgloader` or manually export/import your data.
