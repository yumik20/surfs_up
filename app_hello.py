from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world'
#then at terminal, run export FLASK_APP=app.py        then run flask run    in the same place this file where this file located. 
