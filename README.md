Setup Instructions:

	- Open Visual Studio Code / PyCharm. Select: File-> open->Project: proj_PI (folder)
	- Install packages Django, djangorestframework.
	- Open two terminals:
		1. change directory to API --> cd ContactAPI
		2. change directory to APP --> cd Contactors

	-run(first ContactAPI) --> python manage.py runserver 4554.
	-run on other terminal --> python manage.py runserver (leave the port empty)

	- Create a DB in PostgreSQL named "ContactsDB" (in case the database not created automatically)

	Open the localhost link on Contactors terminal.

	change url:- http://127.0.0.1:8000/Hifi/			/* 2nd path shown on the body of the page below admin



Technologies used:

	Frontend: HTML, CSS, Bootstrap
	Backend: Python Django, restframework
	Database: PostgreSQL 
