from flask import Flask
app = Flask(__name__)

@app.route('/')
def victor_bujan():
    return 'Victor Bujan'



