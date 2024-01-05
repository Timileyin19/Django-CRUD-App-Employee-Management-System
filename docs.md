# Set Up Guide

## Ensure Python is install or install it

```
    python --version
```

## Start the Virtual Environment

```
    python -m venv venv
```

## install Django

```
    pip install django
```

## Start a Django Project

```
    django-admin startproject employee_management .
```

## Run the application

```
    python manage.py runserver
```

## Start an application

```
    python manage.py startapp employees
```

## Add the created App to the parent project

```
    employee_management/settings >> INSTALLED_APPS >> 'employees'
```

## Start Building the Application

```
    employees/views

    def index(request):
        return render(request, 'students/index.html', {
            'students': Student.objects.all()
        })
```

## Create the View Template

```
    employees >> templates >> employees (to avoid conflict of app with the same file) >> index.html
```

## Create the urls for this template

```
    employees >> urls.py
```

## Add the created URL to the parent urls using the "include" keyword

```
    employee_management >> urls
```

## Create the Model

```
    employees >> models.py
```

## Then create the migrations and perform the migration

```
    python manage.py makemigrations
    python manage.py migrate
```

## Import the created model into the View

```
    employees >> views.py
```

## Create the Static File and Dango will load it automatically

```
    employees >> static >> js/css folders
```

## Register the Employee model in the Admin Interface

```
    employees >> admin.py
```

## create the Admin user

```
    python manage.py createsuperuser
```

## access the admin interface

```
    localhost:8000/admin
```

## To Edit Details - Create form

```
    employees >> forms.py
```

## Create the requirements.txt file that contain all the python dependencies used in the project

```
    pip freeze > requirements.txt
```
