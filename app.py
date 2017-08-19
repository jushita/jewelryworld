__author__ = 'jushitaa'

from flask import Flask, render_template, request, session, make_response



app = Flask(__name__)  # '__main__'
app.secret_key = 'development keys'


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.debug = True
    app.run(port=8005)
