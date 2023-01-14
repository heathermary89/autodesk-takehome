# adp-infra-takehome

Simple Python application built using Flask.

## Pre-requisites

1. You have Python3.8 installed.

2. You have Pip3 installed

3. You have Docker installed

4. You have cloned this repository.

## Installation of dependencies

Change directory to cloned repository `autodesk-takehome` and use the package manager `pip3` to install the dependencies in `requirements.txt`

```bash
cd <path to autodesk-takehome>
pip3 install -r requirements.txt
```

## How to run the application locally

```bash
cd <path to autodesk-takehome>
python3 handlers/webapp.py
```

## How to test the application from command line

1. Test condition for GET request with Accept header as 'application/json' :

   ```bash
   curl 'http://localhost:5000/' -H 'Accept:application/json'
   ```

   Expected Output:

   ```bash
   curl http://localhost:5000/ -H 'Accept:application/json'
   {"message":"Hello, World"}
   ```

2. Test condition for GET request with no Accept header :

   ```bash
   curl 'http://localhost:5000/' -H 'Accept':
   ```

   Expected Output:

   ```bash
   curl 'http://localhost:5000/' -H 'Accept':
   <p>Hello, World</p>%
   ```

3. Test condition for any other GET requests:

   ```bash
   curl 'http://localhost:5000/'
   ```

   Expected Output: No output

4. Test POST request with payload:

   ```bash
   curl -X POST --header 'Content-Type:application/json' --data '{"request_id":"123","payload":{"this":"that"}}' http://localhost:5000/
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

   Expected Output : No Ouput

## Enable debug mode logging

To enable debug mode for logging, run the below commands:

```bash
    export FLASK_DEBUG=1
    python3  handlers/webapp.py
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
rootdir: /Users/harshav/Desktop/autodesk-takehome/handlers
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
➜ docker run -p 5000:5000 adp:latest
 * Serving Flask app 'webapp'
 * Debug mode: off
2023-01-14 07:40:35 - INFO - WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://172.17.0.2:5000
```

2. To run the application with debug mode enabled in docker run the below command:

```bash
docker run -p 5000:5000 -e FLASK_DEBUG=1 adp:latest
```

Expected Output:

```bash
docker run -p 5000:5000 -e FLASK_DEBUG=1 adp:latest
 * Serving Flask app 'webapp'
 * Debug mode: on
2023-01-14 07:53:16 - INFO - WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://172.17.0.2:5000
2023-01-14 07:53:16 - INFO - Press CTRL+C to quit
2023-01-14 07:53:16 - INFO -  * Restarting with stat
2023-01-14 07:53:17 - WARNING -  * Debugger is active!
2023-01-14 07:53:17 - INFO -  * Debugger PIN: 803-553-163
2023-01-14 07:53:21 - DEBUG - Debugging POST request for http://localhost:5000/
```

3. To run unit tests on the dockerized application, run the below command:

```bash
docker run -p 5000:5000 --entrypoint "pytest" adp:latest
```

Expected Output:

```bash
➜ docker run -p 5000:5000 --entrypoint "pytest" adp:latest
============================= test session starts ==============================
platform linux -- Python 3.8.16, pytest-7.2.0, pluggy-1.0.0
rootdir: /adp
collected 4 items

handlers/test_webapp.py .... [100%]

============================== 4 passed in 0.14s ===============================
```
