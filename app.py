from flask import Flask
from models.random_predictor import RandomAlgorithm
from models.desertion_example import DesertionAlgorithm
from flask import request
from models.base import Algorithm

mapper = {
    "random_predictor": RandomAlgorithm(), 
    "desertion_algorithm": DesertionAlgorithm(),
}

app = Flask(__name__)

@app.route('/')
def index():
    algorithm_name = request.args.get('algorithm')
    algorithm = mapper.get(algorithm_name, Algorithm)
    result = algorithm.evaluate(**request.args)
    if result > 0.5: 
        return '<h1>no deserta</h1>'
    else: 
        return '<h1>si deserta</h1>' 
    

