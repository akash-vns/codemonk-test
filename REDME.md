# codemonk test with articles #

### About  ###

* it's used to create user article based on their login .
* allow us to create multiple article in single call API.
* all the API doc is under the url swagger-ui with (domain name)
* for the testing purpose, I created some django fixture that will help you to Run and test application with sufficient data


run and helpful commands
------------
App going to urn on 127.0.0.1:8001 (if you hit the url, and it's shows server is running on page it means you project is successfully running)
* docker compose up --build

above command will create default super user and add some dummy data to search articles.

Used libraries
-----------------
* Django 
* django-rest-auth (for authentication)
* djangorestframework (for rest API)
* django-filter (for filter handling)
* psycopg2-binary (DB connection)


Authenticating API
-----------------
* to authenticate API user have to first call the login API, 
* login API return one authorization token
* user have to pass '''--header Authorization: Token `user_token`'''

