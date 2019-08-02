## Title
Awards

## Description
Awards is a platform where users can post their projects to be viewed by other users who can rate the project based on the usability,designed user interface and the content of these postedbprojects. A user can also leave a comment behind for the project owner to know where they deserve a merit or where they need to improve on.

## Author
Juliet Koech

## Date Made 
2/7/2019

## User stories
* As a signed up user you can be able to review and rate other peoples projects

* You can visit the live site of the project and interact with it

* Post your projects and wait for the response of others

## Application Functionality
* The application allows posting and rating of projects

* The projects overall score is then computated to determine which project has the highest scores

* A user can create their own profile where they can fetch data from an api and user can access data in the database as well as use it in your application

## Installations
* Clone the repository with: git clone https://github.com/Julzpeter/Awards

* You will then unzip the zipped format of the repo

* You will need to install all dependencies by running this command :

1) First make sure your requirements.txt file is like this:

 config==0.3.9
 dj-database-url==0.5.0
 django==1.11
 django-bootstrap3==10.0.1
 django-heroku==0.3.1 
 gunicorn==19.9.0 
 Pillow==5.2.0 
 psycopg2==2.7.5 
 python-decouple==3.1 
 pytz==2018.5 
 whitenoise==4.0
 django-mathfilters==0.4.0
 pytz==2019.1
 djangorestframework==3.9.4

2) If not use this command: pip freeze > requirements.txt

3) Install python 3.6 +

4) use django version 1.11

* For the application to run locally you will have to create a postgress database. The following are the steps to use:

a) In your psql: CREATE DATABASE award_1;

b)In your terminal migrate with: python3.7 manage.py migrate

c) Make a .env file to store your environmental variables

d) Serve the application with: python manage.py runserver

e) Open the app in localhost:8000 

## Technologies used
1) Django 1.11.17
2) Python3.6
3) Html and Css

##  MIT LiCENSE
[MIT]()



