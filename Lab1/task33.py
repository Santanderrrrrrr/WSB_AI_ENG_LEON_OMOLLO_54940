from pandas import DataFrame, read_csv

import matplotlib.pyplot as plt
import pandas as pd

bills = [10.99, 20.99, 12.80, 21.60]
tips = [1.01, 2.50, 4.80, 0.80]
sex = ["male", "male", "female", "male"]

dataSet = list(zip(bills, tips, sex))

df = pd.DataFrame(data=dataSet,columns=["bills", "tips", "sex"])
print(df["bills"].mean(axis=0))
print(df["tips"].max())