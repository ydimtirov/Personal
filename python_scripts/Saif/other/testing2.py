#imports
import pandas as pd
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
import pickle
import numpy as np
from sklearn.preprocessing import scale
from sklearn.decomposition import PCA
from flask import Flask
from flask_restful import Resource, Api, reqparse, request
from flask import render_template
from operator import itemgetter 

#Steps 1 and 2

def compute_results(url = "https://archive.ics.uci.edu/ml/machine-learning-databases/pima-indians-diabetes/pima-indians-diabetes.data"):

	names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
	dataframe = pd.read_csv(url, names=names[:-1])
	#scale as to make them uniform
	scaled_dataframe = pd.DataFrame(scale(dataframe), columns = names[:-1]) 
	array = scaled_dataframe.values

	#PCA
	pca = PCA(n_components= 8)
	pca.fit(array)

	#according to this I feel 5 features are important
	print(pca.explained_variance_ratio_)


	check_var =np.cumsum(np.round(pca.explained_variance_ratio_, decimals=4)*100)
	print(check_var)


	print(pd.DataFrame(pca.components_,columns=names[:8],index = ['PC-1','PC-2','3','4','5','6','7','8']))

	#selecting 5 variables - preg, pedi, plas, mass, test for resp PCAs
	dataframe = pd.read_csv(url,names = names)
	dataframe.drop(['pres','skin','age'],inplace=True,axis=1)
	print(dataframe)
	short_array = dataframe.values



	X = short_array[:,0:5]
	Y = short_array[:,-1]

	test_size = 0.33
	seed = 7
	X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X, Y, test_size=test_size, random_state=seed)
	
	# Fit the model on 33%
	model = LogisticRegression()
	model.fit(X_train, Y_train)
	print(model)

	out = model.predict(X_test)
	result = model.score(X_test, Y_test)

	# Accuracy = 76.38%
	print("Result is --" + str(result))
	confidence_scores_ = model.predict_proba(X_test)
	confidence_score = [max(items) for items in confidence_scores_]

	df1 = pd.DataFrame(X_test, columns = ['preg','plas','test','mass','pedi'])
	df2 = pd.DataFrame(Y_test, columns = ['class'])
	df3 = pd.DataFrame(out, columns = ['Prediction'])
	df4 = pd.DataFrame(confidence_score, columns = ['Confidence'])


	df_to_write = pd.concat([df1,df2,df3,df4], axis = 1)
	df_to_write.to_csv('Output.csv' , index = False)


	#serialize - Step 3
	pickle.dump(model, open('model.pickle', 'wb'))
	


'''Use this to pass entire file as a dictionary'''
	# dict_to_return = {key: [] for key in df_to_write.columns}

	# for column in df_to_write.columns:
	# 	dict_to_return[column] = df_to_write[column].tolist()

	# print(dict_to_return)




#Uses the model created by compute_results() to predict for entries 
def run_ml(params):
	opened_model = pickle.load(open('model.pickle', 'rb'))
	vals = params['vals']
	all_items = [float(item) for item in vals]
	indices = [0,1,4,5,6]
	X_test = list(itemgetter(*indices)(all_items))
	print(X_test)
	out = opened_model.predict(np.asarray(X_test))
	return out



# Step 4
app  = Flask(__name__, template_folder='template')
api = Api(app)
parser = reqparse.RequestParser()


class SimpleModel:
	@app.route('/')
	def my_form():
		return render_template("C:\GitHub\python_scripts\Saif\my_form.html")

	@app.route('/', methods=['POST'])
	def my_form_post():
		text = request.form['text']
		processed_text = {'vals': [arg for arg in text.split()]}
		out = run_ml(processed_text)
		return str(int(out))
		

#main function
if __name__ == '__main__':
	compute_results()
	app.run(host = "0.0.0.0", port = 7000, debug=True)