from flask import Flask
from flask import request

app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'hello test'

@app.route('/input_url')
def request_input():
    data = request.args.get('x')
    return 'this is my input from url {}'.format(data)

if __name__ == '__main__':
    app.run()