#Ouverture du df énergie population superficie
import pandas as pd

df_pop_sup=pd.read_csv("df_Population_superficie.csv", ";", header=0)
df_pop_sup.head(1)

#df_pop["Consommation (MW)"]=df_pop["Consommation (MW)"].astype(int)
#df_pop['Thermique (MW)']=df_pop['Thermique (MW)'].astype(int)
#df_pop['Nucléaire (MW)']=df_pop['Nucléaire (MW)'].astype(int)
#df_pop['Eolien (MW)']=df_pop['Eolien (MW)'].astype(int)
#df_pop['Solaire (MW)']=df_pop['Solaire (MW)'].astype(int)
#df_pop['Hydraulique (MW)']=df_pop['Hydraulique (MW)'].astype(int)
#df_pop['Bioénergies (MW)']=df_pop['Bioénergies (MW)'].astype(int)
#df_pop['Ech. physiques (MW)']=df_pop['Ech. physiques (MW)'].astype(int)
#df_pop['Production_totale']=df_pop['Production_totale'].astype(int)
#df_pop['Population']=df_pop['Population'].astype(int)

#Visualisation des dolonnes
df_pop_sup.columns

#Modification au format datetime
df_pop_sup['Date_datetime'] = pd.to_datetime(df_pop_sup['Date_datetime'])
df_pop_sup['Annee'] = df_pop_sup['Date_datetime'].dt.year

#Supression de colonnes inutiles
df_pop_sup.drop('Unnamed: 0', axis=1, inplace=True)

#Renommage des colonnes
df_pop_sup=df_pop_sup.rename(columns={"Région": "Libellé Région"})

#Ouverture du fichier conso par secteur d'activité
df_sec=pd.read_csv("df_conso_secteur_activités_annee.csv", ";", header=0)
df_sec.head(1)

#Renommage des colonnes
df_sec=df_sec.rename(columns={"Année": "Annee"})

df_sec=df_sec.rename(columns={"Code Région": "Code INSEE région"})

df_sec=df_sec.rename(columns={"Région": "Libellé Région"})

#Visualisation des infos
df_sec.info()

#Les valeurs uniques des régions
df_sec["Libellé Région"].unique()

#Rapprochement fichier énergie population superficie du fichier conso secteur activités
df_totale=df_pop_sup.merge(right=df_sec, on=["Libellé Région",'Code INSEE région','Annee'], how="outer")
df_totale.shape

df_totale["Libellé Région"].value_counts(dropna=False)

#Ouverture du fichier température
import pandas as pd
df_temp= pd.read_csv("df_temperatures.csv", ";", header=0)
df_temp.head()

#Suppression d'une colonne inutile
df_temp.drop('Unnamed: 0', axis=1, inplace=True)

#Suppression des lignes Corse
Corse= df_temp[df_temp["Libellé Région"]=="Corse"].index
df_temp.drop(Corse, inplace=True)

#Transformation date au format datetime
df_temp['Date_datetime'] = pd.to_datetime(df_temp['Date_datetime'])

#Tri du df sur des variables
df_temp.sort_values(by=['Date_datetime', 'Code INSEE région', 'Libellé Région', 'tmin', 'tmax',
       'tmoy', 'Annee', 'mois'],ascending=True).head(13)

#Rapprochment fichier température du df enrichi
df_totalee=df_totale.merge(right=df_temp, on=['Code INSEE région', "Date_datetime","Libellé Région", "Annee"], how="outer")

#Suppression de la variable mois
df_totalee.drop("mois", axis=1, inplace=True)

#df_totalee["Mois"].value_counts(dropna=False)
#df_totalee["mois"].value_counts(dropna=False)
#pd.crosstab(df_totalee["Mois"],df_totalee["mois"], rownames=["Mois"], colnames=["mois"])

#Ouverture du fichier soleil et vent
df_sv= pd.read_csv("df_soleilvent.csv",";", index_col=0, header=0)
df_sv

#Mise au format datetime
df_sv['Date_datetime'] = pd.to_datetime(df_sv['Date_datetime'])
df_sv["Annee"]=df_sv['Date_datetime'].dt.year

#Suppression de la Corse
Corse= df_sv[df_sv["Libellé Région"]=="Corse"].index
df_sv.drop(Corse, inplace=True)

#Renommer les valeurs
df_sv["Libellé Région"]=df_sv["Libellé Région"].replace(["Ile-de-France", "Grand-Est"], ["Île-de-France", "Grand Est"])

#Définir des index
df_sf=df_sv.set_index(["Libellé Région", "Code INSEE région"])

#Trier le df sur des variables
#df_totalee= df_totalee.sort_values(["Date_datetime", "Code INSEE région", "Libellé Région"], ascending=True)
df_sv=df_sv.sort_values(["Date_datetime", "Code INSEE région", "Libellé Région"], ascending=True)

# Rapprochement du df soleil vent pour création du df final
df_final=df_totalee.merge(right=df_sv, on=["Date_datetime",'Code INSEE région', 'Libellé Région'], how="outer")
df_final.info()

#Formatage de la colonne
df_final["Annee2"]=df_final['Date_datetime'].dt.year

#Réindexation des colonnes du df
df_final=df_final.reindex(columns=['Code INSEE région', 'Libellé Région','Date_datetime', 'Mois', 'Date-heure', 'Annee',
       'Jour_semaine','Consommation (MW)', 'Thermique (MW)', 'Nucléaire (MW)', 'Eolien (MW)',
       'Solaire (MW)', 'Hydraulique (MW)', 'Bioénergies (MW)',
       'Ech. physiques (MW)','Production_totale', 'Population', 'Superficie (km²)',
       'Densite (hab/km²)', 'Consommation Agriculture (MWh)',
       'Consommation Industrie (MWh)', 'Consommation Tertiaire  (MWh)',
       'Consommation Résidentiel  (MWh)', 'Consommation Secteur Inconnu (MWh)',
       'Consommation totale (MWh)', 'tmin', 'tmax', 'tmoy',
       'Vitesse du vent à 100m (m/s)', 'Rayonnement solaire global (W/m2)','Date', 'Heure'])

df_final

#Visualisation des lignes année aux valeurs manquantes
df_final.loc[df_final["Annee2"].isnull()]

#Remplacement des valeurs manquantes par 0
df_final=df_final.fillna(0)

#Passage des colonnes au format int et arrondis
df_final["Consommation (MW)"]=df_final["Consommation (MW)"].round().astype(int)
df_final['Thermique (MW)']=df_final['Thermique (MW)'].round().astype(int)
df_final['Nucléaire (MW)']=df_final['Nucléaire (MW)'].astype(int)
df_final['Eolien (MW)']=df_final['Eolien (MW)'].astype(int)
df_final['Solaire (MW)']=df_final['Solaire (MW)'].astype(int)
df_final['Hydraulique (MW)']=df_final['Hydraulique (MW)'].astype(int)
df_final['Bioénergies (MW)']=df_final['Bioénergies (MW)'].astype(int)
df_final['Ech. physiques (MW)']=df_final['Ech. physiques (MW)'].astype(int)
df_final['Production_totale']=df_final['Production_totale'].astype(int)

df_final['Population']=df_final['Population'].astype(int)
df_final['Superficie (km²)']=df_final['Superficie (km²)'].astype(int)
df_final['Densite (hab/km²)']=df_final['Densite (hab/km²)'].astype(int)


df_final['Heure']=df_final['Heure'].astype(int)
df_final['Mois']=df_final['Mois'].astype(int)
df_final['Jour_semaine']=df_final['Jour_semaine'].astype(int)
df_final["Annee"]=df_final["Annee"].astype(int)

df_final['Consommation Agriculture (MWh)']=df_final['Consommation Agriculture (MWh)'].astype(int)
df_final['Consommation Résidentiel  (MWh)']=df_final['Consommation Résidentiel  (MWh)'].astype(int)
df_final['Consommation Industrie (MWh)']=df_final['Consommation Industrie (MWh)'].astype(int)
df_final['Consommation Tertiaire  (MWh)']=df_final['Consommation Tertiaire  (MWh)'].astype(int)
df_final['Consommation Secteur Inconnu (MWh)']=df_final['Consommation Secteur Inconnu (MWh)'].astype(int)
df_final['Consommation totale (MWh)']=df_final['Consommation totale (MWh)'].astype(int)

#df_final['tmin']=df_final['tmin'].astype(int)
#df_final['tmax']=df_final['tmax'].astype(int)
#df_final['tmoy']=df_final['tmoy'].astype(int)
#df_final['Vitesse du vent à 100m (m/s)']=df_final['Vitesse du vent à 100m (m/s)'].astype(int)
#df_final['Rayonnement solaire global (W/m2)']=df_final['Rayonnement solaire global (W/m2)'].astype(int)

#df_final.isnull().sum()
df_final.info()

#Remplacement des valeurs manquantes de l'heure par 0
df_final["Heure"]=df_final["Heure"].fillna(0)

df_final["Heure"]= df_final["Heure"]+df_final["Heure2"]

df_final["Mois"]=df_final["Mois2"]

df_final["Jour_semaine"]=df_final["Jour_semaine2"]

#Suppression des variables
df_final.drop(["Heure2", "Mois2","Jour_semaine2"], axis=1, inplace=True)

#Croisement des années pour vérification
pd.crosstab(df_final["Annee"],df_final["Annee2"], rownames=["Annee"], colnames=["Annee2"],margins=True, dropna=False)
#Il manque les années 2011 et 2012 et certaines 2021 dans l'année2

#Remplacement valeurs manquantes par 2021
df_final["Annee"]=df_final["Annee"].fillna(2021)

#Suppression de année 2
df_final.drop(["Annee2"], axis=1, inplace=True)

#Remplacement des valeurs manquantes par 0
df_final.fillna(0,inplace=True)

#df_final['Date2'] = pd.to_datetime(df_final['Date_datetime'])
#df_final.drop('Date2', axis=1, inplace=True)

#Enregistrement du df final au format csv
df_final.to_csv (path_or_buf= "df_final.csv",
                 sep= ";",
                 header= True)





