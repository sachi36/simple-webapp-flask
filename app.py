import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "Welcome to anna earth movers!"

@app.route('/jcb')
def hello():
    return 'we will provide the good service'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
