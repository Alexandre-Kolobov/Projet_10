Project: Develop an API RESTful with using Django Rest Framework

Project Description: This application was created to manages issues for projects


How to run the program:


1) To set up pipenv, please make sure that you have a python version higher that 3.6 (in prompt: python --version)

2) Please open your commande line and do "pip install --user pipenv"

3) Please make git clone https://github.com/Alexandre-Kolobov/Projet_10.git

4) Go with your commande line in /Projet_10 of clonned project and make "pipenv shell". This will activate a venv for you and install all dependences. 

5) Now you are ready to launch the web app. In the commande line go to /API/soft_desk_api/ and make "python manage.py runserver".


You can find the API's documentation here: https://documenter.getpostman.com/view/27423951/2s9YC5zDMq 

How to generate and check an flake8 html report:
    Please use this command in your prompt : "flake8 --format=html --htmldir=flake8-report" (This will generate a new html report in flake8-report repository.)
    To open it, plase use your web browser to open the file index.html

Additional:
    If you need to use Django's shell please put in the commande line "python manage.py shell"
    If you need to remove all data from database please put in the commande line "python manage.py flush"


Users pour demo:

	Login: Alex
	Mdp: Test
	
	Login: Claire
	Mdp: Test
	
	Login: Raphaël
	Mdp: Test
