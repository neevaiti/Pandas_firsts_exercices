import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Charger les données
airbnb = pd.read_csv('Airbnb_Open_Data.csv')

# Calculer la corrélation entre le nombre de reviews et la taille de la description
sns.jointplot(data=airbnb, x='number_of_reviews', y=airbnb['description'].str.len(), kind='reg')
plt.show()