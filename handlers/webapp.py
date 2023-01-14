from flask import Flask, request
import logging
import json

app = Flask(__name__)

# Configure logging -- had to set datefmt to drop milliseconds
logging.basicConfig(filename='record.log', level=logging.DEBUG, datefmt='%Y-%m-%d %H:%M:%S', format='%(asctime)s - %(levelname)s - %(message)s')


#Handling GET requests based on headers
@app.route('/')
def handle_get_request():
    enable_debug(request.method, request.url)
    if 'Accept' in request.headers and request.headers['Accept'] == 'application/json':
        return {"message":"Hello, World"}
    elif 'Accept' not in request.headers:
        return '<p>Hello, World</p>'
    return ''

#Handling POST requests
@app.route('/', methods =['POST'])
def handle_post_request():
    enable_debug(request.method, request.url)
    if request.get_data():
        data_string = request.get_data()
        data = json.loads(data_string)
        request_id = data.get('request_id')
        payload = data.get('payload')

        if request_id and payload:
            return 'OK', 200
        else:
            return 'BAD REQUEST', 400
    else:
        return '', 400

#Enabling debug mode
def enable_debug(method, url):
    if app.debug:
        app.logger.debug(f'Debugging {method} request for {url}')
    return ''


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
