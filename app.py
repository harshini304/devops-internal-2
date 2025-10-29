from flask import Flask
 HEAD
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from a Docker Container! This is Set 2 - Experiment 7.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Docker! This is a simple Flask web app."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
 274f365c1ad2a9f9110db9bba87fca87d17dce59
