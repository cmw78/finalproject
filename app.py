from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import models
import forms

app = Flask(__name__)
app.secret_key = 's3cr3t'
app.config.from_object('config')
db = SQLAlchemy(app, session_options = {'autocommit': False})

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/searchClass')
def searchClass():
	return render_template('searchClass.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)