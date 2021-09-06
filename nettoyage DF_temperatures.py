import pandas as pd
import seaborn as sns
sns.set_theme()

# Lecture du fichier températures
df_temperatures = pd.read_csv("temperature-quotidienne-regionale.csv", sep=";")

# Renommage des colonnes qui seront utilisées pour le merge
df_temperatures.rename(columns = {'date': 'Date_datetime', 'code_insee_region': 'Code INSEE région'}, inplace = True, errors="raise")

#transformation de la colonne Date au format datetime
df_temperatures['Date_datetime'] = pd.to_datetime(df_temperatures['Date_datetime'], format = "%Y-%m-%d")
df_temperatures['annee'] = df_temperatures['Date_datetime'].dt.year
df_temperatures['mois'] = df_temperatures['Date_datetime'].dt.month

# Récupération du df consommations
df_consommations = pd.read_csv('df_nettoyé_2.csv', sep=';')
df_consommations['Date_datetime'] = pd.to_datetime(df_consommations['Date_datetime'])


# Merge df consommations avec df températures sur les dates et codes régions
inner_merged_conso_temperatures = pd.merge(df_temperatures, df_consommations, on=["Date_datetime", "Code INSEE région"])

# création du df consommations et températures à partir du merge
df_conso_temperatures_regions = pd.DataFrame(data = inner_merged_conso_temperatures, columns = ['Date_datetime', 'Code INSEE région', 'Région', 'tmin', 'tmax', 'tmoy', 'annee', 'mois', 'Jour_semaine', 'Date-heure ', 'Consommation (MW)'])

df_temperatures

#Renommage des colonnes
df_temperatures= df_temperatures.rename(columns = {'annee': 'Annee', 'region': 'Libellé Région'})

#Visualisation
df_temperatures.head()

#Création du df température
df_temperatures.to_csv (path_or_buf= "df_temperatures.csv",
                 sep= ";",
                 header= True)

#Dimension du df
df_temperatures.shape

#Tableau des températures par région
df=df_temperatures.groupby(["region"])

df.agg("mean")



