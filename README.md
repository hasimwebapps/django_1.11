# Setup
## Setup Local Env
- python3 -m venv Env
- source Env/bin/activate

## Upgrade pip
- pip install --upgrade pip

## Check pip list & version
- pip list

## install Django 1.11
- pip install Django==1.11.17
- pip list

# Start Project
## Start Project
- django-admin startproject mywebsite

## Run Project
-  python manage.py runserver


# Create Apps
## Django Admin create App
- django-admin startapp profiles

## Django Migrate
- python manage.py makemigrations
- python manage.py migrate


## Django create super users
- python manage.py createsuperuser


## API Specs
# Users
- User list - http://127.0.0.1:8000/api/users/list

