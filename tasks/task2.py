import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv("iris.csv")
(train_set, test_set )= train_test_split(df.values, train_size=0.7, random_state=54940)


def classify_iris(sl, sw, pl, pw):
    if sl>4:
        return("Setosa")
    elif pl<= 5:
        return("Virginica")
    else:
        return("Versicolor")

#algorithm to manually test my answer
good_preds = 0

leng = test_set.shape[0]

for i in range(leng):
    pred_answer=classify_iris(test_set[i, 0], test_set[i, 1], test_set[i, 2], test_set[i, 3])
    real_answer = test_set[i, 4]
    if pred_answer == real_answer:
        good_preds += 1

print(good_preds)
print(good_preds/leng*100, "%")

train_sort = train_set[train_set[:, 4].argsort()]
print(train_sort)
# print(df)

###########This is now after manually training #############

def classify_irisB(sl, sw, pl, pw):
    if pl<2:
        return("Setosa")
    elif pl>= 4.9:
        return("Virginica")
    else:
        return("Versicolor")

good_predsB = 0

leng = test_set.shape[0]

for i in range(leng):
    pred_answerB=classify_irisB(test_set[i, 0], test_set[i, 1], test_set[i, 2], test_set[i, 3])
    real_answer = test_set[i, 4]
    if pred_answerB == real_answer:
        good_predsB += 1

print(good_predsB)
print(good_predsB/leng*100, "%")
