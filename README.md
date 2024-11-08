# CodeLens
##  CodeLens - a program that determines the programming language from a screenshot, recognizes its text and returns it correctly formatted.

### How to install?

#### Source code way:

- Clone git repository on your local PC
- Activate virtual environment in project root:
```commandline
pip install virtualenv
python -m virtualenv venv 
.\venv\Scripts\activate 
```
- Install poetry in your virtual env
```commandline
python -m pip install poetry
```
- Install all dependencies via poetry
```commandline
python -m poetry install
```
- Then you can apply django migrations and run server
```commandline
cd codelens_backend
python manage.py migrate
python manage.py runserver
```

