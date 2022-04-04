import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


miasta = pd.read_csv(r"C:\Users\csyn\Documents\leon school\SCHOOL school\semester 6\ai\AIClass\Lab1\miasta.csv")
print(miasta)

data2010 = {"Rok": [2010], "Gdansk": [460], "Poznan": [555], "Szczecin": [405]}
nuData = pd.DataFrame(data2010)
print(nuData)

cities = pd.DataFrame(data=miasta, columns=["Rok","Gdansk","Poznan","Szczecin"])
cities = cities.append([nuData], ignore_index=True)
print(cities)

def gdanskPlot():
    xAxisG = np.array(cities["Rok"])
    yAxisG = np.array(cities["Gdansk"])

    xAxisP = np.array(cities["Rok"])
    yAxisP = np.array(cities["Poznan"])

    xAxisS = np.array(cities["Rok"])
    yAxisS = np.array(cities["Szczecin"])

    # plt.plot(xAxisG, yAxisG, 'g' , xAxisP, yAxisP, 'b' ,xAxisS, yAxisS, 'r')
    plt.plot(xAxisG, yAxisG, label='Gdansk', color='r', marker='o')
    plt.plot(xAxisG, yAxisP, label='Poznan', color='g', marker='^')
    plt.plot(xAxisG, yAxisS,  label='Szczecin', color='b')
    plt.xlabel('Years')
    plt.ylabel('Demography')
    plt.title('Demography in major polish cities')
    plt.legend()
    plt.show()

gdanskPlot();


