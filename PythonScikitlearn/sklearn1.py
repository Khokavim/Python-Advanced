"""
Training set and testing set

Machine learning is about learning some properties of a data set and then testing those properties against another data set.
A common practice in machine learning is to evaluate an algorithm by splitting a data set into two. We call one of those
sets the training set, on which we learn some properties; we call the other set the testing set, on which we test the learned properties.
"""
from sklearn import datasets

"""
A dataset is a dictionary-like object that holds all the data and some metadata about the data. 
This data is stored in the .data member, which is a n_samples, n_features array.
 In the case of supervised problem, one or more response variables are stored in the .target member
"""
iris = datasets.load_iris()
digits = datasets.load_digits()
#print(digits['data'])
#print(digits['target'])
print(digits['images'][0]) #data-shaping for consumption in sci-kit learn

