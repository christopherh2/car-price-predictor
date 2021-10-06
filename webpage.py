from flask import Flask, request, url_for, redirect, render_template, flash
import pickle 
import pandas as pd
import numpy as np
import os

# Change the template folder as necessary
app = Flask(__name__, template_folder='C:\\Users\\Chris\\Desktop\\flaskr\\2 pg')

# home screen
@app.route('/')
def home():
    return render_template('pg1.html')


# Redirect to pg2 when form is submitted
@app.route('/pg2', methods=['POST'])
def submit():
    if request.method== 'POST':
        fname = request.form['fname']
        lname = request.form['lname']
        title = request.form['title']
        
    
    return render_template('pg2.html', title=title, fname=fname, lname=lname)
        