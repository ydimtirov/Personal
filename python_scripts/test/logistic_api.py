import numpy as np
from flask import Flask, jsonify, abort, request
import cPickle as pickle
filename = 'Logistic.sav'
logistic_regression = pickle.load(open(filename, 'rb'))

app = Flask(__name__)
@app.route('/api', methods = ['POST'])
def make_predict():
    data = request.get_json(force = True)
    predict_request= [data['preg'], data['plas'], data['pres'], data['skin'], data['test'], data['mass'], data['pedi'], data['age']]
    predict_request = np.array(predict_request)
    y_hat = logistic_regression.predict(predict_request)    
    output = [y_hat[0]]
    return jsonify(results = output)
    
if __name__ == '__main__':
    app.run(port = 9000, debug = True)
