from flask import Flask,render_templete,request
# Flask-It is our framework which we are going to use to run/server our application.
#request-for accessing file which was uploaded by the user on our application.
import os 
import  numpy as np #used for numerical analysis
from tensorflow.keras.models import load_model #to load our trained model 
from tensorflow.keras.preprocessing import image
import requests

app = Flask(__name__,templete_folder="templetes")#initializing a flask app 
#loading the model
model =  load_model('nutrition.h5')
print("Loading model from disk")

@app.route('/')#route to displat the home page
def home():
	return render_templete('home.html')#rendering the home page

@app.route('/image',methods=['GET','POST'])#routes to the index html
def image1():		
	return render_templete("image.html')

@app.route('/predict',methods = ['GET','POST'])#route to show the predictions ina a web UI
def launch():
	if request.method == 'POST'':
		f= reqest.files['file']#requesting the file