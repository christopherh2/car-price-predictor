from flask import Flask, request, url_for, redirect, render_template, flash
import pickle, os
import pandas as pd
import numpy as np
from pycaret.regression import *

# Change the template folder as necessary
# Template folder will be default location which is a folder called template
app = Flask(__name__)

# home screen renders pg 1 file
@app.route('/')
def home():
    return render_template('pg1.html')


# Redirect to pg2 when form is submitted
@app.route('/form', methods=['POST'])
def submit():
    # Method will be post on form submit
    if request.method== 'POST':
        result=request.form
        model = result.get('model')
        
        # Server side form validation
        try:
            # Cast data as int or float to ensure data is in appropriate form
            year= int(result.get('year'))
            mileage= int(result.get('mileage'))
            engineSize= float(result.get('engineSize'))
            mpg = float(request.form.get('mpg'))

        except:
            # If a data type is not valid return error
            error= "Enter a valid number!"
            return render_template('pg1.html',error=error)
        
        else:
            # Check if form is filled out entirely
            if not model or not year or not mileage or not mpg or not engineSize:
                error="Error! Fill all the fields out!"
                return render_template('pg1.html',error=error)
            
            # Check if numbers are positive
            if mileage <0:
                error ="Enter a valid mileage!"
                return render_template('pg1.html',error=error)
            
            if mpg <=0:
                error ="Enter a valid mpg value!"
                return render_template('pg1.html',error=error)
                
            if engineSize <=0:
                error ="Enter a valid engine size!"
                return render_template('pg1.html',error=error)    
                
                
            # Load model and set columns
            lgbm = load_model("model2")
            cols = ['model','year','mileage','mpg','engineSize']
            data = [x for x in request.form.values()]
            final=np.array(data)
            
            # Arrange data and columns into a datafram
            df = pd.DataFrame(data=[final], columns=cols)
            
            # Make prediction using the dataframe
            pred= predict_model(lgbm, data=df)
            prediction = round(pred.Label[0],2)
        
        return render_template('pg2.html', data=data, cols=cols, prediction=prediction)

if __name__ == '__main__':
   app.run(debug = True)
        
