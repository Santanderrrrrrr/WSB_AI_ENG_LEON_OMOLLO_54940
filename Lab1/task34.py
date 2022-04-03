import matplotlib.pyplot as plt
import pandas as pd


miasta = pd.read_csv("miasta.csv")
print(miasta)

df = pd.DataFrame({'Rok': [2010], 'Gdansk': [460], 'Poznan': [555], 'Szczecin': [405]})

# df.to_csv('miasta.csv', mode='a', index=False, header=False)

df.set_index('Rok').plot()
plt.show()