import pandas as pd

df_air_bnb = pd.read_csv("Airbnb_Open_Data.csv")

"""
**`Exercice`**: 
- créez une table à partir de la table airbnb en ne concervant que les annonces disponibles plus de 100 jours par an ou 100 jours exactement.
- selectionner parmi cette table créée les 15 annonces ayant le plus de revues et pour ces annonces ne conserver que les colonnes "host id",	"host name" et "neighbourhood"
- renommez ces colonnes "host_id",	"host_name"	et "neighbourhood"
- faite de host_id l'index puis triez la table en fonction de l'index.
"""

print(df_air_bnb.dtypes)

df_air_bnb_100_days = df_air_bnb.loc[ (df_air_bnb["availability 365"] > 100) | (df_air_bnb["availability 365"] == 100)]

print(df_air_bnb_100_days.head(3))

df_air_bnb_100_days_sort = df_air_bnb_100_days.nlargest(15, "number of reviews")[["host_id", "host_name", "neighbourhood"]].head(15)

df_air_bnb_100_days_sort =