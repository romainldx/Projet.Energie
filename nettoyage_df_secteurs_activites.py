#Ouverture du fichier
import pandas as pd
df=pd.read_csv('conso-elec-gaz-annuelle-par-secteur-dactivite-agregee-departement.csv',sep=';')
df.head(50)

#les valeurs uniques de la variable année
df["Année"].unique()

#Les valeurs de la variable filière
df["Filière"].value_counts()

#df.info()

#Suppression de la valeur gaz
indexNames = df[ df['Filière'] == 'Gaz' ].index
# Delete these row indexes from dataFrame
df.drop(indexNames , inplace=True)
df.head(50)

#Vérification des valerus de filière
df["Filière"].unique()


# Comptage des valeurs manquantes
def valeur_maquante(df):
    flag = 0
    for col in df.columns:
        if df[col].isna().sum() > 0:
            flag = 1
            print(f' "{col}": {df[col].isna().sum()} valeurs manquantes')
    if flag == 0:
        print("Aucune valeur manquante dans le dataset.")


valeur_maquante(df)

#Visualisation des lignes aux valeurs manquantes
nan_rows = df[df['Libellé Région'].isnull()]
nan_rows

#Suppression de la colonne geom
df.drop(columns=["geom"],inplace=True)
df.head()


# Comptage des valeurs manquantes
def valeur_maquante(df):
    flag = 0
    for col in df.columns:
        if df[col].isna().sum() > 0:
            flag = 1
            print(f' "{col}": {df[col].isna().sum()} valeurs manquantes')
    if flag == 0:
        print("Aucune valeur manquante dans le dataset.")


valeur_maquante(df)

#Suppression des valeurs manquantes
df=df.dropna()


# Comptage des valeurs manquantes
def valeur_maquante(df):
    flag = 0
    for col in df.columns:
        if df[col].isna().sum() > 0:
            flag = 1
            print(f' "{col}": {df[col].isna().sum()} valeurs manquantes')
    if flag == 0:
        print("Aucune valeur manquante dans le dataset.")


valeur_maquante(df)

#Visualisation des premières lignes
df.head()

#Comptage des valeurs par région
df["Libellé Région"].value_counts()

#Visualisation des colonnes
df.columns

#Suppression des colonnes inutiles à notre étude
df.drop(columns=['Filière','Opérateur','Nombre de points Agriculture','Nombre de mailles secretisées (agriculture)',
       'Indique qualité Agriculture','Nombre de points Industrie',
       'Nombre de mailles secretisées (industrie)', 'Indice qualité Industrie','Nombre de points Tertiaire',
       'Nombre de mailles secretisées (tertiaire)', 'Indice qualité Tertiaire','Nombre de points Résidentiel',
       'Nombre de mailles secretisées (résidentiel)',
       'Indice qualité Résidentiel','Nombre de points Secteur Inconnu',
       'Nombre de mailles secretisées (secteur inconnu)',
       'Indice qualité Non Affecté','Code Département','Libellé Département','id_filiere'],inplace=True)
df.head()

#df.columns
#df["Libellé Région"].unique()
#df.info()


#Régions à supprimer
REGION_sup= df.loc[(df['Libellé Région'] =='Corse') |
                   (df['Libellé Région'] =='Guadeloupe')|
                   (df['Libellé Région'] =='La Réunion')|
                   (df['Libellé Région'] =='Martinique') |
                   (df['Libellé Région'] =='Guyane') |
                   (df['Libellé Région'] =='Mayotte')].index
# Delete these row indexes from dataFrame
df.drop(REGION_sup, inplace=True)
df.head()


#Tableau des consos par région, code insee et année
import numpy as np
#df3=pd.pivot_table(df, index=['Libellé Région','Année'], values=['Consommation Agriculture (MWh)',
       #'Consommation Industrie (MWh)', 'Consommation Tertiaire  (MWh)',
       #'Consommation Résidentiel  (MWh)', 'Consommation Secteur Inconnu (MWh)',
       #'Code Région', 'Consommation totale (MWh)'], aggfunc=np.sum)
df3=pd.pivot_table(df, index=['Libellé Région', "Code Région", "Année"], values=['Consommation Agriculture (MWh)',
       'Consommation Industrie (MWh)', 'Consommation Tertiaire  (MWh)',
       'Consommation Résidentiel  (MWh)', 'Consommation Secteur Inconnu (MWh)', 'Consommation totale (MWh)'], aggfunc=np.sum)
df3.head(15).round().astype(int)

#Création d'un df réorganisé
df_SA_annee=pd.DataFrame(data=df3,
                         #index=['Libellé Région', "Code Région", "Année"],
                   columns=["Consommation Agriculture (MWh)",
       'Consommation Industrie (MWh)', 'Consommation Tertiaire  (MWh)',
       'Consommation Résidentiel  (MWh)', 'Consommation Secteur Inconnu (MWh)', 'Consommation totale (MWh)'])
#df_SA_annee["Année"]=[2011,2012,2013,2014,2015,2016,2017,2018,2019]
#df_SA_annee['Code Région']=[53,75,11,27,84,28,76,24,32,44,93,52]
#df_SA_annee['Libellé Région']=['Bretagne', 'Nouvelle-Aquitaine', 'Île-de-France',
       #'Bourgogne-Franche-Comté', 'Auvergne-Rhône-Alpes', 'Normandie',
       #'Occitanie', 'Centre-Val de Loire', 'Hauts-de-France', 'Grand Est',
       #"Provence-Alpes-Côte d'Azur", 'Pays de la Loire']
df_SA_annee.head(12).round()

#df dont les valeurs en ligne sont passées au format int
df_SA_annee.astype(int)
#df_SA_annee["Code Région"]=df_SA_annee["Code Région"].astype(int)

#Création du df conso secteur d'activités
df_SA_annee.to_csv (path_or_buf= "df_conso_secteur_activités_annee.csv",
                 sep= ";",
                 header=True)

#Vérification de son enregistrement
import pandas as pd
df_SA_annee= pd.read_csv("df_conso_secteur_activités_annee.csv",
                 sep= ";",index_col="Libellé Région")
df_SA_annee.head()

# Renommage des colonnes
df_SA_annee.rename(columns={"Code Région": "Code INSEE région", "Année": "Annee"})

#idem
df_SA_annee.rename(index = {"Libellé Région": 'Région'}, inplace = True)

#agrégé moyen des consommations par région entre 2011 et 2019
df2=pd.pivot_table(df, index=['Libellé Région'], values=['Consommation Agriculture (MWh)',
       'Consommation Industrie (MWh)', 'Consommation Tertiaire  (MWh)',
       'Consommation Résidentiel  (MWh)', 'Consommation Secteur Inconnu (MWh)',
       'Code Région', 'Consommation totale (MWh)'], aggfunc=np.mean)
df2.head(15).round()
df2.astype(int)

#Agrégé moyen des consommations des 12 régions (échelle France)
df2.describe().round().astype(int)

#Cammembert de la répartition des consos par secteur en France
name = ['Industrie','Agriculture','Tertiaire', 'Résidentiel', 'inconnu']
#data = [8294969,315008,8324294,14202430,246303]
data=[466137,23245,500310,849719,13235]

plt.pie(data, labels=name, autopct='%1.0f%%', startangle=10, )
plt.show()

#Histogramme des conso par région

%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

barWidth = 0.8
df2.plot.bar(x="Libellé Région",y=['Consommation Agriculture (MWh)','Consommation Industrie (MWh)','Consommation Tertiaire  (MWh)','Consommation Résidentiel  (MWh)','Consommation Secteur Inconnu (MWh)'],figsize=(20,10),width = barWidth)
plt.title("Consommation  par secteurs d'activités en fonction des régions")
plt.show()

#Création d'un df
df_SA=pd.DataFrame(data=df2,
                   columns=['Libellé Région','Consommation Agriculture (MWh)',
       'Consommation Industrie (MWh)', 'Consommation Tertiaire  (MWh)',
       'Consommation Résidentiel  (MWh)', 'Consommation Secteur Inconnu (MWh)',
       'Code Région', 'Consommation totale (MWh)'])
#df_SA['Code Région']=[53,75,11,27,84,28,76,24,32,44,93,52]
df_SA['Libellé Région']=['Bretagne', 'Nouvelle-Aquitaine', 'Île-de-France',
       'Bourgogne-Franche-Comté', 'Auvergne-Rhône-Alpes', 'Normandie',
       'Occitanie', 'Centre-Val de Loire', 'Hauts-de-France', 'Grand Est',
       "Provence-Alpes-Côte d'Azur", 'Pays de la Loire']
df_SA.head(12).round()

#Modification du format
df_SA["Code Région"]=df_SA["Code Région"].astype(int)

#Affichage des premières lignes du df arrondis
df_SA.head(12).round()

#Passage de Libellé Région en index
df_SA= df_SA.set_index('Libellé Région')

#valeur de la consommation à l'échelle France
df_SA.agg("sum")

#Création du df conso secteur d'activités
df_SA.to_csv (path_or_buf= "df_conso_secteur_activités.csv",
                 sep= ";",
                 header=True)

#Vérification
df_SA= pd.read_csv("df_conso_secteur_activités.csv",
                 sep= ";",index_col="Libellé Région")
df_SA.head()




