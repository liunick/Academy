from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from werkzeug import secure_filename
from clarifai import rest
from clarifai.rest import ClarifaiApp
import requests
import os

app = Flask(__name__)
clarifaiApp = ClarifaiApp(api_key='d1df0d143a3a4e4b8ecb696c0ed9dde4')

app.config['DEBUG'] = True
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['FILE_EXTENSIONS'] = ['png', 'jpg', 'pdf', 'jpeg', 'gif']
app.config['KEYWORDS_PASTA'] = ['pasta', 'spaghetti', 'angel-hair pasta']
app.config['KEYWORDS'] = ['Neil']
app.config['APPROVAL_PERCENTAGE'] = .6000

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1] in app.config['FILE_EXTENSIONS']

def is_pasta(data):
	cutoff = app.config['APPROVAL_PERCENTAGE']
	return any(x in data.keys() for x in app.config['KEYWORDS']) \
		and any(i > cutoff for i in (data[x] for x in app.config['KEYWORDS']))

def is_significant(data):
	cutoff = app.config['APPROVAL_PERCENTAGE']
	return any(x in data.keys() for x in app.config['KEYWORDS']) \
		and any(i > cutoff for i in (data[x] for x in app.config['KEYWORDS']))

def clarifai_data(model, filename):
	model = clarifaiApp.models.get(model)
	output = model.predict_by_filename(filename=filename)
	data = {}
	for item in output['outputs'][0]['data']['concepts']:
		data[item['name']] =  item['value']
	return data

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/trainer', methods=['GET'])
def trainer():
	return render_template('trainer.html')

@app.route('/train', methods=['GET', 'POST'])
def trainModel():
	if request.method == 'POST':
		fileObj = request.files['file']
		if fileObj and allowed_file(fileObj.filename):
			safeFile = secure_filename(fileObj.filename)
			local_filename = os.path.join(app.config['UPLOAD_FOLDER'], safeFile)
			fileObj.save(local_filename)
			

@app.route('/upload', methods=['GET', 'POST'])
def uploadFile():
	if request.method == 'POST':
		fileObj = request.files['file']
		if fileObj and allowed_file(fileObj.filename):
			safeFile = secure_filename(fileObj.filename)
			local_filename = os.path.join(app.config['UPLOAD_FOLDER'], safeFile)
			fileObj.save(local_filename)
			data = clarifai_data('Friends', local_filename)
			return render_template('index.html', data=is_significant(data), imgSrc=local_filename)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
	return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
	app.run(host='0.0.0.0')