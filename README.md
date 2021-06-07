# coronatestapi

Hello Audience,

Create a new virtualenv first. I recommend using mkvirtualenv which is a package inside virtualenvwrapper.

Anyways,

Once you have a new virtual environment, 

pip install -r requirements.txt

Once done,

cd covapp

python manage.py runserver

Visit: http://localhost:8000 For Home
API Docs can be found and tested from Swagger documentation @ http://localhost:8000/schema/docs

Required APIs:-

1. http://localhost:8000/accounts/signup
2. http://localhost:8000/accounts/get-token
3. http://localhost:8000/api/covidappdata
