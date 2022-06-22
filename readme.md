## Instructions to use this *NewsFeedPortal* project
- Firstly clone the peoject
- Before use the project you need to install python, pip
- It's better to use virtual environment for each django project to reduce the virsion confliction
- I have used virtualenv in this project.

## Setup Virtual Environment
- Install virtual environment golabally
    - pip install virtualenv
- Then create my own virtual environment in my project
    - virtualenv venv
- Run this command for installing required packages:
    - pip install -r requirements.txt
- Start with virtual env: . venv/bin/activate

## Intallation:
- I have inclued the required packages inside requirements.txt file. So run-
    - pip install -r requirements.txt
- To run the project on your machine:
    - python3 manage.py runserver

## Phase 1
- You can see the news feed by this link:
    - BASE_DIR/news     (BASE_DIR= your local serer after ruuning the server)
    - Here you can see the news. By default the page shows country=uk news
    - You can filter news by Country and Source from from top left search bar
clea
## Phase 2
- You can SignUp and SignIn from news directory or home directory
- After signing in, you will land to home page from where you can SignOut or go to news page
- You can also Reset your password from SignIn page if you forgot you password
- You can not visit *news/user-news/* and *settings* url's page without signin. If you visit those url's, you will redirected to signin page

## Phase 3
- After signing in, you will arrive a homepage. You can go your settings page or personal news portal from this homepage.
- In News portal, you can see the news and go to the news source page by clicking *See News* button
