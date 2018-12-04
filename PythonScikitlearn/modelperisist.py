"""
In the case of the digits dataset, the task is to predict, given an image, which digit it represents.
 There are samples of each of the 10 possible classes (the digits zero through nine) on which we fit
 an estimator to be able to predict the classes to which unseen samples belong.
"""
from sklearn import svm
from sklearn import datasets
from joblib import dump,load

iris = datasets.load_iris()
digits = datasets.load_digits()
#print(digits['data'])
#print(digits['target'])

#In scikit-learn, an estimator for classification is a Python object that implements the methods fit(X, y) and predict(T).
clf = svm.SVC(gamma=0.001, C=100.)
clf.fit(digits.data[:-1], digits.target[:-1])
print(clf.predict(digits.data[-1:]))
dump(clf, 'filename.joblib')

#you can reload the pickled model (possibly in another Python process) with:
clf = load('filename.joblib')
