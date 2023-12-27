# Restaurant-kitchen-pet-project now deployed to render
Check it out!

https://restaurant-kitchen-0cd1.onrender.com/
# 1. General info
This project was created for educational purposes to better familiarize yourself with the Django web framework. The site includes several models such as cooks, dishes and ingredients, allows you to create these entities and edit them, the site also has registration and authorization. The User(cook) model is implemented using the built-in AbstractUser model.

# 2. Setup django project on different platforms
Starting a Django project from a GitHub repository on different platforms involves a few general steps. Here's a step-by-step guide that you can follow for Windows, macOS, and Linux:


Prerequisites:
Git: Make sure Git is installed on your system. You can download it from https://git-scm.com/.

Python: Install Python on your system. You can download it from https://www.python.org/downloads/.

Steps:
1. Clone the Repository:
Open your terminal or command prompt and navigate to the directory where you want to create your Django project.


```
https://github.com/okien1/Restaurant-kitchen-pet-project.git

```

2. Create a Virtual Environment (Optional but Recommended):
Navigate into the project directory and create a virtual environment. Virtual environments help isolate dependencies for different projects.

Activate the virtual environment on Windows:
```
cd repository
python -m venv venv
venv\Scripts\activate
```
On macOS/Linux:

```
source venv/bin/activate
```
3. Install Dependencies:
Install the project dependencies using pip:

```
pip install -r requirements.txt
```


4. Configure Database:
Configure your database settings in the settings.py file.

```
python manage.py makemigrations
python manage.py migrate
```
5. Run the Development Server:
```
python manage.py runserver
```
The development server should now be running. Open a web browser and go to http://127.0.0.1:8000/ to see your Django application.

Generate a new secret key for the project and update the SECRET_KEY setting in settings.py.

# 3. Run preloaded data
 run
 ```
python manage.py loaddata my_fixture.json
```
 to load data from fixture to database.
 
# Use default credentials to login into app:

 login: User123
 
 password: Gferh12SDe
