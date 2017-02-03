from sklearn.datasets import load_iris
from sklearn.datasets import load_boston

boston = load_boston()

x = boston.features

# x = iris.data[:,2:][0:140]
# y = iris.target[0:140]
# x_test = iris.data[:, 2:][141:150]
# y_test = iris.target[141:150]

print x