from sklearn.datasets import load_iris

iris = load_iris()

X = iris.data
Y = iris.target

print(X.shape)
print(Y.shape)

#Features Name.
print(iris.feature_names)