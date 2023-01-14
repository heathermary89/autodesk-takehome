# adp-infra-takehome

Simple Python application built using Flask.

## Pre-requisites

1. You have Python3 installed.

2. You have Pip3 installed

3. You have Docker installed

4. You have cloned this repository.

## Installation of dependencies

Change directory to adp-takehome and use the package manager pip to install the dependencies in requirements.txt

```bash
cd <path to adp-takehome>
pip3 install -r requirements.txt
```

## How to run the application locally

```bash
cd <path to adp-takehome>
python3 handlers/webapp.py
```

## How to test the application from command line

1. Test condition for GET request with Accept header as 'application/json' :

   ```bash
   curl 'http://localhost:5000/' -H 'Accept:application/json'
   ```

   Expected Output:

   ```bash
   {
   "message": "Hello, World"
   }
   ```

2. Test condition for GET request with no Accept header :

   ```bash
   curl 'http://localhost:5000/' -H 'Accept':
   ```

   Expected Output:

   ```bash
   <p>Hello, World</p
   ```

3. Test condition for any other GET requests:

   ```bash
   curl 'http://localhost:5000/'
   ```

   Expected Output: No output

4. Test POST request with payload:

   ```bash
   curl -X POST --header 'Content-Type:application/json' --data '{"request_id":"123","payload":{"this":"that"} http://localhost:5000/
   ```

   Expected Output: OK

5. Test POST request without full payload :

   ```bash
   curl -X POST --header 'Content-Type:application/json' --data '{"request_id":"123"}' http://localhost:5000/
   ```

   Expected Output : BAD REQUEST

6. Test POST request with no payload:

   ```bash
   curl -X POST --header 'Content-Type:application/json' --data '' http://localhost:5000/
   ```

   Expected Output : NO DATA

## Enable debug mode logging

```bash
    export FLASK_DEBUG=1
    python handlers/webapp.py
```

Informational logs will get written to record.log file by default but when debug is enabled, you will see Debug statements specifiying the type of request and the URL. Debug mode can be disabled by unloading the environment variable FLASK_DEBUG like

```bash
    unset FLASK_DEBUG
```

## Application Unit Testing

To run unit tests for the application, run the below commands:

```bash
   cd handlers
   pytest -v
```

Expected Output:

```bash
➜  handlers git:(master) ✗ pytest -v
=============test session starts =============================================================
platform darwin -- Python 3.8.5, pytest-7.2.0, pluggy-1.0.0 -- /Library/Frameworks/Python.framework/Versions/3.8/bin/python3.8
cachedir: .pytest_cache
rootdir: /Users/harshav/Desktop/adp-takehome/handlers
collected 4 items

test_webapp.py::test_get_request_success PASSED                                                                                                                                                      [ 25%]
test_webapp.py::test_get_request_failure_not_found PASSED                                                                                                                                            [ 50%]
test_webapp.py::test_post_request_success PASSED                                                                                                                                                     [ 75%]
test_webapp.py::test_post_route_failure_bad_request PASSED                                                                                                                                           [100%]

============================================================================================ 4 passed in 0.12s =============================================================================================

```

# Dockerizing the application

1. To containerize the application, use the Dockerfile to build the docker image and run the docker container:

```bash
cd </path-of-Dockerfile>
docker build -t adp:latest .
docker run -p 5000:5000 adp:latest
```

Expected Output:

```bash
➜  adp-takehome git:(master) ✗ docker run -p 5000:5000  adp:version13
 * Serving Flask app 'webapp'
 * Debug mode: off
```

2. To run the application with debug enabled in docker run the below command:

```bash
docker run -p 5000:5000 -e FLASK_DEBUG=1 adp:latest
```

Expected Output:

```bash
➜  adp-takehome git:(master) ✗ docker run -p 5000:5000 --env FLASK_DEBUG=1 adp:version13
 * Serving Flask app 'webapp'
 * Debug mode: on
```

3. To run unit tests on the dockerized application, run the below command:

```bash
docker run -p 5000:5000 --entrypoint "pytest" adp:latest
```

Expected Output:

```bash
➜ adp-takehome git:(master) ✗ docker run -p 5000:5000 --entrypoint "pytest" adp:version13
============================= test session starts ==============================
platform linux -- Python 3.8.16, pytest-7.2.0, pluggy-1.0.0
rootdir: /adp
collected 4 items

handlers/test_webapp.py .... [100%]

============================== 4 passed in 0.14s ===============================
```
