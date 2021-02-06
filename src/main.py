import requests
from flask import Flask
from flask import request
app = Flask(__name__)

#change this!
FORWARD_URL = 'http://127.0.0.1:5000/forward-url'

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/some-url', methods = ['GET', 'POST'])
def get_data():
    if request.method == 'GET':
        return requests.get(FORWARD_URL).content
    
    if request.method == 'POST':
        original_data = request.form # a multidict containing POST data
        #print(original_data)
        return requests.post(FORWARD_URL, data = dict(original_data)).content

# used for debug
@app.route('/forward-url', methods = ['GET', 'POST'])
def show_data():
    if request.method == 'GET':
        return 'Forwarded-GET'
    
    if request.method == 'POST':
        forwarded_data = request.form
        print(forwarded_data)
        return 'Forwarded-POST'

    