HEAD
# app.py
from flask import Flask
import os

from flask import Flask
 HEAD
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from a Docker Container! This is Set 2 - Experiment 7.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
 21105f70e9f542b017a53a07e237ad8967ceb0ba

app = Flask(__name__)

@app.route('/')
 HEAD
def hello():
    # Retrieve the port from the environment variable (default to 8080)
    port = os.environ.get('FLASK_PORT', '8080')
    return f"<h1>Hello from the Docker Container!</h1><p>The app is running on port: **{port}**</p>"

if __name__ == '__main__':
    # Flask runs on 0.0.0.0 to be accessible outside the container
    app.run(debug=True, host='0.0.0.0', port=8080)

def home():
    return "Hello, Docker! This is a simple Flask web app."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
 274f365c1ad2a9f9110db9bba87fca87d17dce59
 21105f70e9f542b017a53a07e237ad8967ceb0ba
