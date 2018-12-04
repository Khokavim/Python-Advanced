import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn import neighbors
from sklearn.naive_bayes import GaussianNB
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans


X = np.random.random((10,5))

#shape of X
print(X.shape)
print(X)

y = np.array(['M','F','M','M','M','F','M','F','M','F'])
#shape of y
print(y.shape)

#for simplified X(feature-set)
X[X < 0.7] = 0

#Split data into train set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

#Initialize and fit data into models

#support vector machines(svm)
svc = SVC(kernel='linear')
svc.fit(X_train, y_train)
pred = svc.predict(X_test)
print(pred)

#KNN
knn = neighbors.KNeighborsClassifier(n_neighbors=4)
knn.fit(X_train, y_train)
pred = svc.predict(X_test)
#print(pred)

#Naive Bayes
gnb = GaussianNB()
gnb.fit(X_train, y_train)
pred = gnb.predict(X_test)
#print(pred)

# Principal Component Analysis(PCA)
pca = PCA(n_components=0.95)
pca_model = pca.fit_transform(X_train)

# K-Means
k_means = KMeans(n_clusters=4, random_state=0)
k_means.fit(X_train)
pred = k_means.predict(X_test)
#print(pred)


