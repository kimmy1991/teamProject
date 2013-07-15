teamProject
===========
We will be making an app store

It will consist of the following

website- should allow users to upload and browse apps avalible on the server
webservices- should bridge the communication between the front end and backend, this should handle all request and return
appropriate error messages and validate the data coming in
android app- i dont care what app you make
database- we can pick from a few database, make some suggestions


Specification for the database:


A table called categories with the following fields

ID(PK) Category application_name

--- How to install the project---

Install pip
Make a 'virtualenv' for this project using following commands:
virtualenv <folder_name>
source <folder_name>/bin/activate
(to quit the virtual environment, type in terminal: deactive)

Install the required dependencies: pip install -r requirements.txt
Run the project:

python manage.py runserver

Goto: http://localhost:5000

