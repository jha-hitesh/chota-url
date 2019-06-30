# Chota URL

A simple url shortner written in Django 2.2

## Features

- Simple to use authentication less API

## How to Use Locally

    // 1. Create a virtual environment
    
    $ virtualenv -p /usr/bin/python3 chota-url
    
    // 2. Install requirements.txt

    $ pip install -r requirements.txt

    // 3. Migrate models
    $ python manage.py makemigrations common
    $ python manage.py migrate

    // 4. Run locally
    
    $ python manage.py runserver

## Deployment to Heroku

    $ git init
    $ git add -A
    $ git commit -m "Initial commit"

    $ heroku create
    $ git push heroku master