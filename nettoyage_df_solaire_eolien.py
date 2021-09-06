# Ouverture du df
import pandas as pd

df_sv=pd.read_csv("rayonnement-solaire-vitesse-vent-tri-horaires-regionaux.csv",";")
df_sv

#Suppresssion des heures associées à la date
df_sv['Date'] = df_sv['Date'].apply(lambda x : x[:10])

from datetime import datetime as dt

#affichage du code
df_sv["Date"]=pd.to_datetime(df_sv.Date)
df_sv.head()

#Renommage des colonnes
df_sv=df_sv.rename(columns={"Date": "Date_datetime", "Région": "Libellé Région"})

#Dimension du df
df_sv.shape

#Création du df soleil et vent
df_sv.to_csv (path_or_buf= "df_soleilvent.csv",
                 sep= ";",
                 header=True)

