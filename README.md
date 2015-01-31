# Setup
=======

### Virtual Env

`mkvirtualenv sl`

### Install Requirements

`pip install -r requirements/requirements.txt`

### Setup database

Ensure that you have postgres installed. Then create a dev database and dev user.

```
createdb -U <username to connect as> salient
createuser -U <username to connect as> -P <password prompt> salient
```

### Run Django

```
./manage.py syncdb
./manage.py runserver
```
