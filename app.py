# app.py
from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    # Retrieve the port from the environment variable (default to 8080)
    port = os.environ.get('FLASK_PORT', '8080')
    return f"<h1>Hello from the Docker Container!</h1><p>The app is running on port: **{port}**</p>"

if __name__ == '__main__':
    # Flask runs on 0.0.0.0 to be accessible outside the container
    app.run(debug=True, host='0.0.0.0', port=8080)