import pandas as pd
from sklearn.model_selection import train_test_split
# from sklearn.datasets import load_iris
from sklearn import tree
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler


df = pd.read_csv('diabetes.csv')
print(df)

all_inputs = df[["pregnant-times","glucose-concentr","blood-pressure","skin-thickness","insulin","mass-index","pedigree-func","age"]].values
all_classes = df["class"].values

(train_inputs, test_inputs, train_classes, test_classes) = train_test_split(all_inputs, all_classes, train_size=0.7, random_state=54940)
scaler = StandardScaler()
scaler.fit(train_inputs)

train_inputs = scaler.transform(train_inputs)
test_inputs = scaler.transform(test_inputs)

clf = tree.DecisionTreeClassifier()

clf.fit(train_inputs, train_classes)
print(clf.score(test_inputs, test_classes)*100)

tree.plot_tree(clf)
plt.show()

