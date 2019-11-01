# pylint: disable=invalid-name

from flask import Flask

app = Flask(__name__)

@app.route('/')

def index():
    '''
    Indentação 'INDEX PAGE'
    '''
    return 'Index Page!'
    app.run(host='0.0.0.0')

if __name__ == '__main__':
    app.run()
