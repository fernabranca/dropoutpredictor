from flask import Flask
from models.random_predictor import evaluate_sample

app = Flask(__name__)

@app.route('/')
def index():
		result=evaluate_sample()
		if result: 
			return '<h1>anda</h1>'
		else: 
			return '<h1>no anda</h1>' 
		

