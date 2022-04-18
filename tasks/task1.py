import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv("iris.csv")

print(df)

print("next")

print(df.values)

print("all rows, column 0")

print(df.values[:, 0])

print("rows 5 to 10 all columns")

print(df.values[0:12, :])

print("data in the cell [1,4]")
print(df.values[1,1])

#splitting the df.values into training and test set
#splitting the set to test set (30%) and train se (70%)

(train_set, test_set) = train_test_split(df.values, train_size=0.7, random_state=54940)


#checking records in test set and how many there are:
print(test_set)
print(test_set.shape[0])

print(train_set)
print(train_set.shape[0])

print(df.shape[0])


#splitting the test and train sets into colums with inputs and columns with classes

print("Train inputs columns 0 to 4 of all rows")
train_inputs= train_set[:, 0:4]
print(train_inputs)

print("Train classes found in column 4 of each row")
train_classes= train_set[:, 4]
print(train_classes)

print("Test inputs found in column 4 of all row")
test_inputs = test_set[:, 0:4]
print(test_inputs)

print("test classes found in column 4 of each row")
test_classes = test_set[:, 4]


