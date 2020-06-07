Steps to run the Project:

Step1- download the project from git:  https://github.com/avi527/Testcloudstackgroup

Step2- Go through requirement.txt file, you need to install all the packages.

Step3- Start the server with python manage.py runserver
		o/p url will be like this: http://127.0.0.1:8000/cloudstackApp/
Step4- Run command with migrate and makemigrations

Step5- create super user with python manage.py createsuperuser command

Step6- Register User to the generated URL and then login with same email and password.
	for eg. http://127.0.0.1:8000/cloudstackApp/
Step7- After login it will redirect to home profile page, logout option is available to login different user as well.
