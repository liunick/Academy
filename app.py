from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from werkzeug import secure_filename
import requests
import os

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['FILE_EXTENSIONS'] = ['png', 'jpg', 'pdf', 'jpeg', 'gif']

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1] in app.config['FILE_EXTENSIONS']

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])
def uploadFile():
	if request.method == 'POST':
		fileObj = request.files['file']
		if fileObj and allowed_file(fileObj.filename):
			safeFile = secure_filename(fileObj.filename)
			fileObj.save(os.path.join(app.config['UPLOAD_FOLDER'], safeFile))
			return redirect(url_for('uploaded_file', filename=safeFile))

@app.route('/uploads/<filename>')
def uploaded_file(filename):
	return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
	app.run(host='0.0.0.0')