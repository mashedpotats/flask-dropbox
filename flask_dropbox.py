# TODO: CHANGE LOGIN METHOD TO USERNAME & PASSWORD
import json
import os

from flask import Flask, session, render_template, send_from_directory, request

import dropbox_server

app = Flask(__name__)

TOKEN = 'mfcRgIwx6aAAAAAAAAAAWhRuPZRpiGb9bHNNDzudgYyMZr-MDae0eOMjxYD6hyJd'
dbx = dropbox_server.DropboxServer(token=TOKEN)


# root page
@app.route('/')
def index():
    return render_template('index.html')


# login page
@app.route('/login')
def login():
    return render_template('login.html'), 302


# save token
@app.route('/wiki/token', methods=['POST'])
def save_token():
    session['token'] = request.form['token']
    return "201", 201


# read
@app.route('/wiki/read', methods=['GET'])
def read():
    return json.dumps(dbx.read())  # return as JSON compatible string


# write
@app.route('/wiki/write', methods=['POST'])
def write():
    return dbx.write(request.form['filename'], request.form['data'])


# delete
@app.route('/wiki/delete', methods=['DELETE'])
def delete():
    return dbx.delete(request.args['filename'])


# error handler for 404
@app.errorhandler(404)
def error(e):
    return render_template('error.html', status=e.code), e.code


# route urls for static files
@app.route('/<path:path>')
def send_js(path):
    return send_from_directory('static', path)


app.secret_key = os.urandom(24)

if __name__ == '__main__':
    app.run()
