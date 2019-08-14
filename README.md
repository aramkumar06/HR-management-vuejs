# A Django / Django REST framework based HR management VueJS app for small companies

- This is django / django rest based HR management app for small companies.

## Backend
  - django 2.1
  - django-rest-framework 3.8.2
  - psycopg2 2.7.5
  - django-cors-headers 2.4.0
  
## Frontend
  - Vue 2.5.13
  
## How to install
  - install python 3.6
  - install postgresql 10.3
  
## Load fixtures
  - `python3 manage.py loaddata fixtures/countries.json`
  - `python3 manage.py loaddata fixtures/sites.json`
  - `python3 manage.py loaddata fixtures/roles.json`
  - `python3 manage.py loaddata fixtures/teams.json`
  - `python3 manage.py loaddata fixtures/accounts.json`
  - `python3 manage.py loaddata fixtures/books.json`
  - `python3 manage.py loaddata fixtures/users.json`
