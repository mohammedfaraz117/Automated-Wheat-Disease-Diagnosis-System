from flask import Flask, render_template, request, redirect, url_for,jsonify
import os


app = Flask(__name__)


@app.route('/')
def login():
    return render_template('login.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/upload')
def upload():
    return render_template('upload.html')

@app.route('/detect')
def detect():
    return render_template('detect.html')

@app.route('/precautions')
def precautions():
    return render_template('precautions.html')



@app.route('/about')
def about():
    return render_template('about.html')




if __name__ == '__main__':
    
    app.run(port=8080,debug=True)
