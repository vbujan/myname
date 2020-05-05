from flask import Flask
app = Flask(__name__)
def victor():
    return 'Victor Bujan'
@app.route('/')
def victor():
    return 'Victor Bujan'
if __name__ == '__main__':
    app.run()

