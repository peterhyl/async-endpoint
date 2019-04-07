# Async endpoint
Simple asynchronous endpoint to fetch data from database by name. I used
non-blocking technology peewee-async and aiohttp for asynchronous web endpoint
to fetching data(or create new) from database.

Models and managers are basic concept, you can edit or create new models by your
requirement and database models and structures.
# Deployment instruction:
Developed by Python 3.6, you can use virtual env.
```
pip install -r requirements.txt
```
Now you can run the application
```
python -m aiohttp.web -H localhost -P 8080 endpoint:init_app
```
or install Gunicorn and run the application as standalone server
```
pip install gunicorn
gunicorn endpoint:init_app --bind localhost:8080 --worker-class aiohttp.GunicornWebWorker
```
Application is routed on localhost and port 8080: http://localhost:8080 , you can change the
host and port.

# Authors
* **Peter Hyl**
