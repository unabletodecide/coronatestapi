# coronatestapi

Hello Audience,

There is only one dependency to run this app, actually 2:-
1. docker
2. docker-compose - version 3.x

Once you have them, ready. Git clone the repository and we are good to go.

FIRST, RUN: docker-compose build
THEN, RUN: docker-compose up

That's it!

Visit: http://localhost:8000 For Home
API Docs can be found and tested from Swagger documentation @ http://localhost:8000/schema/docs

Required APIs:-

1. http://localhost:8000/accounts/signup
2. http://localhost:8000/accounts/get-token
3. http://localhost:8000/api/covidappdata
