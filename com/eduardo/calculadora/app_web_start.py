# pylint: disable=invalid-name
# -*- coding: utf-8 -*-

from flask import Flask

app = Flask(__name__)

@app.route('/')

def index():
    '''
    Indentação 'INDEX PAGE'
    '''
    return 'Index Page!'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
