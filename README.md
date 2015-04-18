# Bottle API

Simple demo of a Python REST API using Bottle.

## About

Bottle: a fast, simple and lightweight WSGI micro web-framework for Python.

http://bottlepy.org/docs/dev/index.html

# Use it

## Setup

Install bottle (assuming you got a Python devel environment ready):

````
$ pip install bottle
````

## Play

Run it:

````
$ python myrestapi.py
````

Query it:

````
$ curl http://localhost:8080/containers/
```` 

````
$ curl -H 'Content-Type: application/json' -X POST -d '{"image": "organization/image", "service": "myService"}' http://localhost:8080/containers
```` 

````
$ curl -X DELETE http://localhost:8080/containers/stomped_archibald
```` 
