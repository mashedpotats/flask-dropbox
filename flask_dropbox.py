# TODO: CHANGE LOGIN METHOD TO USERNAME & PASSWORD
import os
import dropbox_server

from flask import Flask, session, redirect, url_for, render_template, send_from_directory, request, abort

app = Flask(__name__)


@app.route('/')
def index():
    # if 'token' in session:
    if True: # temporary
        return render_template('index.html')

    return redirect(url_for('login'))


# login page
@app.route('/login')
def login():
    return render_template('login.html'), 302


# save token
@app.route('/wiki/token', methods=['POST'])
def save_token():
    session['token'] = request.form['token']
    return "201", 201


# get directory contents
@app.route('/wiki/content', methods=['GET'])
def get_content():
    if 'token' in session:
        return dropbox_server.get_content(session['token'], request.args['path'])
    abort(401)


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
