import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report




df = pd.read_csv('Iris.csv')

X = df[['sepal.length', 'sepal.width', 'petal.length', 'petal.width']].values
Y = df['variety'].values

(X_train, X_test, Y_train, Y_test) = train_test_split(X, Y, test_size=0.3, random_state=54940)
scaler = StandardScaler()
scaler.fit(X_train)

# X_train = scaler.transform(X_train)
# X_test = scaler.transform(X_test)



##################k=1###################
print("k=1")
classifier = KNeighborsClassifier(n_neighbors=1)
classifier.fit(X_train, Y_train)

Y_pred = classifier.predict(X_test)

print(classification_report(Y_test, Y_pred))


###################K=3#################
print("k=3")
classifierB = KNeighborsClassifier(n_neighbors=3)
classifierB.fit(X_train, Y_train)

Y_predB = classifierB.predict(X_test)

print(classification_report(Y_test, Y_predB))



###################K=5#################
print("k=5")
classifierC = KNeighborsClassifier(n_neighbors=5)
classifierC.fit(X_train, Y_train)

Y_predC = classifierC.predict(X_test)

print(classification_report(Y_test, Y_predC))



###################K=11#################
print("k=11")
classifierD = KNeighborsClassifier(n_neighbors=11)
classifierD.fit(X_train, Y_train)

Y_predD = classifierD.predict(X_test)

print(classification_report(Y_test, Y_predD))