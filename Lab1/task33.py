from pandas import DataFrame, read_csv

import matplotlib.pyplot as plt
import pandas as pd

firstTips=pd.read_csv(r'C:\Users\csyn\Documents\leon school\SCHOOL school\semester 6\ai\AIClass\Lab1\task33.csv')
print(firstTips)

# name=firstTips.loc[:,"name"]
# print(name)
# tip=firstTips.loc[:,"tip"]
# sex=firstTips.loc[:,"sex"]
# total_bill=firstTips.loc[:,"total_bill"]

tipDataSet = list(zip(firstTips["name"], firstTips["sex"], firstTips["tip"], firstTips["total_bill"]))
tipDataSet

tp = pd.DataFrame(data = tipDataSet, columns=['name','sex', 'tip', 'total_bill'])

tp.to_csv("tips", index=False, header=['name', 'sex', 'tip',  'total_bill'])


print(tp["total_bill"].mean(axis=0))
# print((16.99+10.34+21.01+23.68+24.59)/5)

print(tp["tip"].max())
# print(max(firstTips["tip"]))





