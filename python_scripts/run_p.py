import pandas
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
import pickle
# load the model from disk
loaded_model = pickle.load(open('finalized_model.sav', 'rb'))
result = loaded_model.score(X_test, Y_test)
print(result)