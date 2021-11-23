from flask import Flask, request, render_template, g, redirect, Response, url_for

import os

tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
app = Flask(__name__, template_folder=tmpl_dir)


@app.route('/')
def index():
  return redirect('/login')

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/loginaction', methods=['POST'])
def login_action():
    return redirect(url_for('landing'))

@app.route('/createaccount')
def createaccount():
    return render_template("create_account.html")

@app.route('/addnewuseraction', methods=['POST'])
def addnewuser():
    return redirect(url_for('landing'))

@app.route('/landing')
def landing():
    return render_template("landing.html")


