## Start a django project
- go to the targetted directory and run: 
    - django-admin startproject NewsfeedPortal
- run the project on server:
    - python3 manage.py runserver

## Virtual Environment
- Install virtual environment golabally
    - pip install virtualenv
- Then create my own virtual environment in my project
    - virtualenv venv
- Store the requierments packages with version within the project by this command:
    - pip freeze > requirements.txt
- Added required packages inside requiremnts.txt and run:
    - pip install -r requirements.txt
- Start with virtual env: . venv/bin/activate

## Create App
- go to the project directory and run:
    - python3 manage.py startapp NewsApp
- register this app to NewsfeedPortal/settings.py-> INSTALLED_APPS

## Phase 1
- Connect NewsApi through api
- Show news in news page
- We have used django-environ for keeping ar secret data
