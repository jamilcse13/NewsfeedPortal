## Start a django project
- Clone the project from this repository
- You have to install python3 and pip in your machine

## Setup Virtual Environment
- Install virtual environment golabally
    - pip install virtualenv
- Then create my own virtual environment in my project
    - virtualenv venv
- Run this command for installing required packages:
    - pip install -r requirements.txt
- Start with virtual env: . venv/bin/activate

- run the project:
    - python3 manage.py runserver

## Create App
- go to the project directory and run:
    - python3 manage.py startapp NewsApp
- register this app to NewsfeedPortal/settings.py-> INSTALLED_APPS

## Phase 1
- You can see the news feed by this link:
    - BASE_DIR/news     (BASE_DIR= your local serer after ruuning the server)


