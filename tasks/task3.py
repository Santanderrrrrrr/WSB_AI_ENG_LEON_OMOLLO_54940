import pandas as pd
from sklearn.model_selection import train_test_split
# from sklearn.datasets import load_iris
from sklearn import tree
import matplotlib.pyplot as plt


df = pd.read_csv('Iris.csv')
# print(df)

all_inputs = df[['sepal.length', 'sepal.width', 'petal.length', 'petal.width']].values
all_classes = df['variety'].values

(train_inputs, test_inputs, train_classes, test_classes) = train_test_split(all_inputs, all_classes, train_size=0.7, random_state=54940)

clf = tree.DecisionTreeClassifier()

clf.fit(train_inputs, train_classes)
print(clf.score(test_inputs, test_classes)*100)

tree.plot_tree(clf)
plt.show()





