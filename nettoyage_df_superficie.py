# Ouverture du df population nettoyé
import pandas as pd
import numpy as np

df=pd.read_csv("df_Population_nettoye.csv",";")
df.head()

#Création du df superficie
df_superficie=pd.DataFrame()

df_superficie=pd.DataFrame(data=df_superficie, index=[53,75,11,27,84,28,76,24,32,44,93,52],columns=["Code INSEE région","Région", "Superficie (km²)","Densite (hab/km²)"])

df_superficie["Code INSEE région"]=[53,75,11,27,84,28,76,24,32,44,93,52]
df_superficie["Région"]= ['Bretagne', 'Nouvelle-Aquitaine', 'Île-de-France',
       'Bourgogne-Franche-Comté', 'Auvergne-Rhône-Alpes', 'Normandie',
       'Occitanie', 'Centre-Val de Loire', 'Hauts-de-France', 'Grand Est',
       "Provence-Alpes-Côte d'Azur", 'Pays de la Loire']
df_superficie["Superficie (km²)"]=[27208,84036,12011,47784,69711,29907,72724,39151,31806,57441,31400,32082]
df_superficie["Densite (hab/km²)"]=[120,70,1001,59,112,112,79,66,189,97,159,115]

df_superficie

#Rapprochement du df superficie du df population
df_Population_superficie=df.merge(right=df_superficie, left_on=["Code INSEE région","Région"], right_on=["Code INSEE région","Région"], how="outer")
df_Population_superficie.head()

#Suppression d'une colonne inutile
df_Population_superficie.drop('Unnamed: 0', axis=1, inplace=True)

#Controle de la dimension du df population superficie
df_Population_superficie.shape

#Création du df population superficie au format csv
df_Population_superficie.to_csv (path_or_buf= "df_Population_superficie.csv",
                 sep= ";",
                 header= True)

#Vérification de l'enregistrement
df=pd.read_csv("df_Population_superficie.csv",";", index_col=0, header=0)
df.head()

#Visualisation des informations
df.info()

#Variable mise au format int
df["Production_totale"]=df["Production_totale"].astype(int)

df["Population"]=df["Population"].astype(int)

#Visualisation des colonnes
df.columns

#Variable mise au format int
df["Thermique (MW)"]=df["Thermique (MW)"].astype(int)
df["Consommation (MW)"]=df["Consommation (MW)"].astype(int)
df["Nucléaire (MW)"]=df["Nucléaire (MW)"].astype(int)
df["Eolien (MW)"]=df["Eolien (MW)"].astype(int)
df["Solaire (MW)"]=df["Solaire (MW)"].astype(int)
df["Hydraulique (MW)"]=df["Hydraulique (MW)"].astype(int)
df["Bioénergies (MW)"]=df["Bioénergies (MW)"].astype(int)
df["Ech. physiques (MW)"]=df["Ech. physiques (MW)"].astype(int)

#Visualisation des premières lignes
df.head()

#Création du df population superficie au format csv
df.to_csv (path_or_buf= "df_Population_superficie.csv",
                 sep= ";",
                 header= True)

#Vérification de l'enregistrement + dimension df
pd.read_csv("df_Population_superficie.csv",
                 sep= ";",index_col=0, header=0).shape





