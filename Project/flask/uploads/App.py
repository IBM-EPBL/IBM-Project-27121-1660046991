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
		basepath=os.path.dirname('__file__')#storing the file directory
		filepath = os.path.join(basepath,"uploads",f.filename)#storing the file in uploads folder
		f.save(fileppath)#saving rhe file
			       
		img = image.load_img(filepath,target_size=(64,64))#load and reshaping the image
		x=image.img_to_array(img)#converting image to and array
	 	x=np.expand_dims(x,axis=0)#changing the dimensions of the image
			       
		pred = np.argmax(model.predict(x),axis=1)
		print("prediction",pred)#printing the prediction
		index = ['Apples','Banana','Orange','Pineapple','Watermelon']
			       
		result = str(index[pred[0]])
			       
		x=result
		print(x)
		result = nutrition(result)
		print(result)
			       
		return render_templete("0.html",showcase=(result),showcase1=(x))
def nutrition(index):
	url = "https://calorieninjas.p.rapidapi.com/v1/nutrition"
	querystring = {"query":index}
	header = {
		'x-rapidapi-key': "5d797ab107ms
