# Django CRM project

## Summary

This is a learning project using the Django python framework connected to a postgres database running in docker and following the [Django Project – Code a CRM App Tutorial](https://www.youtube.com/watch?v=t10QcFx7d5k) youtube video.

---

## Setup

### Initialising database for local run

Make sure you have docker installed and run `docker-compose up -d` to start a postgres database in docker in detached mode.

### Installation and setup

1. Create virtual environment:
   1. type `python -m venv virt`, where `virt` is the name you want to give to your virtual environment. This will create a virt folder in your project
   2. Activate the virtual environment by typing `source virt/bin/activate`. This is the path to the activate script inside the virt folder.
2. Install project dependencies
   1. pip install django
   2. pip install psycopg2-binary (for postgres connection)
3. Start the project configuration files from within the main folder of the project by typying `django-admin startproject crm` where `crm` is just a name for the project folder. This is going to create the `crm` folder with a `manage.py` configuration in it.
4. Inside the newly created `crm` folder, initialise the project by typing `python manage.py startapp website` where `website` is the name of the application.
5. Managing dependencies:
   1. After all dependencies are installed, run `pip freeze > requirements.txt` to export all dependencies into a text file named `requirements.txt`
   2. When running the project from scratch, you can type `pip install -r requirements.txt` instead of manually installing all dependencies again.

### Connecting the postgres database

1. Open the `crm/crm/settings.py` file
2. Go to the `DATABASES` section of the file and
   1. Configure the databases object for the database you're using (postgresql in this case)
   2. Add your application name to the `INSTALLED_APPS` object (`website` in this example)
3. In the same foldera as where the `manage.py` file is, run `python manage.py migrate`. This will add all the django tables and other stuff into the database

### Create a superuser

Type `python manage.py createsuperuser` to create a superuser. Follow the instructions on the prompt (recommended user name is `admin`)

---

## Next...
