
# Employee Management in Django

This is a django project based on python's web frame work Django that contains basic CRUD funtionality with couple of additional things.

This project contains a basic `sqlite3` database for storing data and for managing it.
It is able to handle all the database opreations and quries, also we can create super user and we can see all the information from Django admin site.


## Deployment

For cloning this repository use :

```bash
  git clone git@github.com:SYN606/Employee-management-in-Django.git

```

then change the directory and run the `requirements.txt` file :
```bash
    cd Employee-management-in-Django
```
Then
```bash
    pip install -r requirements.txt
```

For running the server use :

```bash
    python manage.py runserver
```

>>> Extra Quries :

For migrating data base first time :

```bash
    python manage.py makemigrations
```
Then 
```bash
    python manage.py migrate
```