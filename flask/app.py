# -*- coding: utf-8 -*-
"""
Created on Sun May 17 17:31:19 2020

@author: Sri Nayani
"""

from flask import Flask,render_template,request

import pickle
import numpy as np

model = pickle.load(open('class.pkl','rb')) 
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/login',methods =['POST'])
def login():
    preg = request.form['preg']
    plas = request.form['plas']
    pres = request.form['pres']
    skin = request.form['skin']
    insulin = request.form['insulin']
    mass = request.form['mass']
    pedi = request.form['pedi']
    age = request.form['age']
    total = [[int(age),float(pedi),float(mass),int(insulin),int(skin),int(pres),int(plas),int(preg)]]
    print(total)
    y_pred = model.predict(total)
    
    print(y_pred)
    
    return render_template("index.html",showcase = y_pred)

if __name__ == '__main__':
    app.run(debug = True)