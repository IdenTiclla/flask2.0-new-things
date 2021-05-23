from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "hello flask 2.0"

@app.get('/first')
def my_get_endpoint():
    return 'This was a GET request.'


@app.post('/second')
def my_post_endpoint():
    return 'This was a POST request.'

if __name__ == '__main__':
    app.run()