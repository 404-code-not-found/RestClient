from flask import Flask, render_template
import requests
import json

from flask import Flask, render_template

app = Flask(__name__)

postData = data = '''{
   "title" : 'foo',
   "body" : 'bar',
   "userId" : 1
}'''


@app.route('/')
def hello_world():
    return requests.get('https://jsonplaceholder.typicode.com/todos/1').content


@app.route('/post')
def post():
    return requests.post('https://jsonplaceholder.typicode.com/posts', postData).content


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001)
