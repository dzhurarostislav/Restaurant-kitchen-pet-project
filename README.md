# Restaurant-kitchen-pet-project
# Run preloaded data
 run python manage.py loaddata my_fixture.json to load data from fixture to database.
 
 Use default credentials to login into app:
 
 User123
 Gferh12SDe
# Setup django project on different platforms
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

```
cd repository
python -m venv venv
Activate the virtual environment:
```
On Windows:
```
venv\Scripts\activate
On macOS/Linux:
```
```
source venv/bin/activate
```
3. Install Dependencies:
Install the project dependencies using pip:

```
pip install -r requirements.txt
```
If there's no requirements.txt file, you might need to check the project documentation or source code to identify the required dependencies.


4. Configure Database:
Django projects often require a database. Configure your database settings in the settings.py file. You might need to set up a new database and apply migrations:

```
python manage.py migrate
```
5. Run the Development Server:
Start the Django development server:

```
python manage.py runserver
```
The development server should now be running. Open a web browser and go to http://127.0.0.1:8000/ to see your Django application.

Additional Steps:
Settings Configuration:

Review and configure other settings in the settings.py file if necessary.
Static Files and Media:

Configure static files and media settings if the project involves serving static files or handling media uploads.
Secret Key and Security:

Generate a new secret key for the project and update the SECRET_KEY setting in settings.py.
Django Admin:

Create a superuser account to access the Django admin interface:

```
python manage.py createsuperuser
```
