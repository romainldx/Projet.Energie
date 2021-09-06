# Importer le fichier et afficher les premières lignes :
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv('D:\projet_energie.csv', sep=';', low_memory=False)
df.head()

#Création “Date_datetime” au format date :
from datetime import datetime as dt

df["Date_datetime"]=pd.to_datetime(df.Date)
df.head()

#“Heure” au format heure
from datetime import datetime as dt

df["Heure"]=df.Heure.astype("datetime64")
df["Heure"]=df.Heure.dt.hour
df.head()

#Affichage des colonnes du dataset
df.columns

#Visualisation des informations des colonnes
df.dtypes

#Supression de la variable “Nature”
df=df.drop("Nature", axis=1)
df.head()


#Création “Date_datetime” au format date :
from datetime import datetime as dt

df["Date_datetime"]=pd.to_datetime(df.Date)
df.head()


#Colonne Heure au format Datetime
from datetime import datetime as dt

df["Heure"]=df.Heure.astype("datetime64")
df["Heure"]=df.Heure.dt.hour
df.head()

#Transformation des variables “TCH” au format float
df["TCH Thermique (%)"]=pd.to_numeric(df["TCH Thermique (%)"],errors="coerce")
df["TCH Nucléaire (%)"]=pd.to_numeric(df["TCH Nucléaire (%)"],errors="coerce")
df["TCH Eolien (%)"]=pd.to_numeric(df["TCH Eolien (%)"],errors="coerce")
df["TCH Solaire (%)"]=pd.to_numeric(df["TCH Solaire (%)"],errors="coerce")
df["TCH Hydraulique (%)"]=pd.to_numeric(df["TCH Hydraulique (%)"],errors="coerce")
df["TCH Bioénergies (%)"]=pd.to_numeric(df["TCH Bioénergies (%)"],errors="coerce")


#Controle de la modification des tranformations
df.info()

#Supression de la variable des lignes  01-01-2013  à 00H00 possède que des NA = 11 lignes en moins
df=df.drop(df.index[0:12], axis=0)
df.head()

#Supression de la variable “Pompage MW"
df=df.drop("Pompage (MW)", axis=1)
df.columns

#Suppression de la variable “Date-heure”
df=df.drop("Date - Heure", axis=1)
df.head()

#Supression des 38 variables flux
df=df.drop(df.iloc[:,12:50], axis=1)
df.columns

#Controle des dimensions du dataset
df.shape

#Création de la variable “Mois”
from datetime import datetime as dt
df["Mois"]=pd.to_datetime(df.Date).dt.month
df.Mois.nunique()

#Création de la variable “Date-heure” au format date-1 chiffre
df["Date-heure"]=df["Date"] + "-" + df["Heure"].astype(str)
df.head()

#Création de la variable “Année” à partir de “Date”
df["Annee"]=df.Date_datetime.dt.year
df.head()

#Création de la variable “Jour” à partir de “Date_datetime”
df["Jour_semaine"]=df.Date_datetime.dt.weekday
df.head()
df["Jour_semaine"].nunique()

#Transformation des NA en valeur 0
df=df.fillna(0)
#df.head()

# Création de la variable “Production_totale” à partir des variables par filière MW
df["Production_totale"]=df["Thermique (MW)"]+df["Nucléaire (MW)"]+df["Eolien (MW)"]+df["Solaire (MW)"]+df["Hydraulique (MW)"]+df["Bioénergies (MW)"]
df.head()

#Description des données avec arrondis à 2 chiffres après la virgule
df.describe().round(2)

#Comptage des valeurs manquantes par colonne
df.isna().sum()

#Suppression des colonnes TCH et TCO
df.drop(columns=['TCO Thermique (%)', 'TCH Thermique (%)', 'TCO Nucléaire (%)',
       'TCH Nucléaire (%)', 'TCO Eolien (%)', 'TCH Eolien (%)',
       'TCO Solaire (%)', 'TCH Solaire (%)', 'TCO Hydraulique (%)',
       'TCH Hydraulique (%)', 'TCO Bioénergies (%)', 'TCH Bioénergies (%)'],inplace=True)
df.columns

#Création du csv après traitements
df.to_csv (path_or_buf= "df_dataset_energie.csv",
                 sep= ";",
                 header= True)

#Controle de l'enregistrement du csv
import pandas as pd
df=pd.read_csv("df_dataset_energie.csv",
                 sep= ";", index_col=0, header=0)
df.columns





































