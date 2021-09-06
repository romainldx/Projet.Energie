# Importer le fichier et afficher les premières lignes :
import pandas as pd
%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
population = pd.read_excel('populationFR.xlsx')
#données de population recceuillies sur le site de l'INED, seule source trouvée disponible
df.head()

#Création des dictionnaires
import pandas as pd
dictionnaire_2018= {"Bretagne": ["3335414"], 'Nouvelle-Aquitaine':[5979778], 'Île-de-France':[12213447],
       'Bourgogne-Franche-Comté':[2807807], 'Auvergne-Rhône-Alpes':[7994459], 'Normandie':[3327477],
       'Occitanie':[5885496], 'Centre-Val de Loire':[2572853], 'Hauts-de-France':[6044108], 'Grand Est':[5550389],
       "Provence-Alpes-Côte d'Azur":[5052832], 'Pays de la Loire':[3781423]}
dictionnaire_2019= {"Bretagne": [3347004], 'Nouvelle-Aquitaine':[5999253], 'Île-de-France':[12252917],
       'Bourgogne-Franche-Comté':[2801577], 'Auvergne-Rhône-Alpes':[8030533], 'Normandie':[3320832],
       'Occitanie':[5918981], 'Centre-Val de Loire':[2569510], 'Hauts-de-France':[5995908], 'Grand Est':[5543407],
       "Provence-Alpes-Côte d'Azur":[5065696], 'Pays de la Loire':[3800348]}
dictionnaire_2020= {"Bretagne": [3358524], 'Nouvelle-Aquitaine':[6018424], 'Île-de-France':[12291557],
       'Bourgogne-Franche-Comté':[2794517], 'Auvergne-Rhône-Alpes':[8064146], 'Normandie':[3313432],
       'Occitanie':[5951850], 'Centre-Val de Loire':[2565726], 'Hauts-de-France':[5987795], 'Grand Est':[5536002],
       "Provence-Alpes-Côte d'Azur":[5077582], 'Pays de la Loire':[3818421]}

#Création du df population entre 2013 et 2020
import numpy as np
df_Population=pd.DataFrame()

df_Population=pd.DataFrame(data=df_Population, index=[53,75,11,27,84,28,76,24,32,44,93,52],columns=["Code INSEE région","Région", "Population_2018","Population_2019","Population_2020"])

df_Population["Code INSEE région"]=[53,75,11,27,84,28,76,24,32,44,93,52]
df_Population["Région"]= ['Bretagne', 'Nouvelle-Aquitaine', 'Île-de-France',
       'Bourgogne-Franche-Comté', 'Auvergne-Rhône-Alpes', 'Normandie',
       'Occitanie', 'Centre-Val de Loire', 'Hauts-de-France', 'Grand Est',
       "Provence-Alpes-Côte d'Azur", 'Pays de la Loire']
df_Population["Population_2013"]=[3258707,5844177,11959807,2819783,7757595,3328364,5683878,2570548,5987883,5552388,4953675,3660852]
df_Population["Population_2014"]=[3276543,5879144,12027565,2820623,7820966,3335645,5730753,2577435,6006156,5554645,4983438,3690833]
df_Population["Population_2015"]=[3293850,5911482,12082144,2820940,7877698,3339131,5774185,2578592,6009976,5559051,5007977,3718512]
df_Population["Population_2016"]=[3306529,5935603,12117132,2818338,7916889,3335929,5808435,2577866,6006870,5555186,5021928,3737632]
df_Population["Population_2017"]=[3318904,5956978,12174880,2811423,7948287,3330478,5845102,2576252,6003815,5549586,5030890,3757600]

df_Population["Population_2018"]=[3335414,5979778,12213447,2807807,7994459,3327477,5885496,2572853,6044108,5550389,5052832,3781423]
df_Population["Population_2019"]=[3347004,5999253,12252917,2801577,8030533,3320832,5918981,2569510,5995908,5543407,5065696,3800348]
df_Population["Population_2020"]=[3358524,6018424,12291557,2794517,8064146,3313432,5951850,2565726,5987795,5536002,5077582,3818421]
#df_Population["ANNEE_2018"]=[2018,2018,2018,2018,2018,2018,2018,2018,2018,2018,2018,2018]
#df_Population["ANNEE_2019"]=[2019,2019,2019,2019,2019,2019,2019,2019,2019,2019,2019,2019]
#df_Population["ANNEE_2020"]=[2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020]
df_Population

#Création du df population au format csv
df_Population.to_csv (path_or_buf= "df_Population.csv",
                 sep= ";",
                 header= True)

#Création du df population 2018
df_Population_2018=pd.DataFrame()

df_Population_2018=pd.DataFrame(data=df_Population, index=[53,75,11,27,84,28,76,24,32,44,93,52],columns=["Code INSEE région","Région", "Population_2018","ANNEE_2018"])

df_Population_2018["Code INSEE région"]=[53,75,11,27,84,28,76,24,32,44,93,52]
df_Population_2018["Région"]= ['Bretagne', 'Nouvelle-Aquitaine', 'Île-de-France',
       'Bourgogne-Franche-Comté', 'Auvergne-Rhône-Alpes', 'Normandie',
       'Occitanie', 'Centre-Val de Loire', 'Hauts-de-France', 'Grand Est',
       "Provence-Alpes-Côte d'Azur", 'Pays de la Loire']
df_Population_2018["Population_2018"]=[3335414,5979778,12213447,2807807,7994459,3327477,5885496,2572853,6044108,5550389,5052832,3781423]
df_Population_2018["ANNEE_2018"]=[2018,2018,2018,2018,2018,2018,2018,2018,2018,2018,2018,2018]
df_Population_2018

#Création du df population 2018 ua format csv
df_Population_2018.to_csv (path_or_buf= "df_Population_2018.csv",
                 sep= ";",
                 header= True)

#Création du df population 2019
df_Population_2019=pd.DataFrame()

df_Population_2019=pd.DataFrame(data=df_Population, index=[53,75,11,27,84,28,76,24,32,44,93,52],columns=["Code INSEE région","Région", "Population_2019","ANNEE_2019"])

df_Population_2019["Code INSEE région"]=[53,75,11,27,84,28,76,24,32,44,93,52]
df_Population_2019["Région"]= ['Bretagne', 'Nouvelle-Aquitaine', 'Île-de-France',
       'Bourgogne-Franche-Comté', 'Auvergne-Rhône-Alpes', 'Normandie',
       'Occitanie', 'Centre-Val de Loire', 'Hauts-de-France', 'Grand Est',
       "Provence-Alpes-Côte d'Azur", 'Pays de la Loire']
df_Population_2019["Population_2019"]=[3347004,5999253,12252917,2801577,8030533,3320832,5918981,2569510,5995908,5543407,5065696,3800348]
df_Population_2019["ANNEE_2019"]=[2019,2019,2019,2019,2019,2019,2019,2019,2019,2019,2019,2019]
df_Population_2019

#Création du df population 2019 au format csv
df_Population_2019.to_csv (path_or_buf= "df_Population_2019.csv",
                 sep= ";",
                 header= True)

#Création du df population 2020
df_Population_2020=pd.DataFrame()

df_Population_2020=pd.DataFrame(data=df_Population, index=[53,75,11,27,84,28,76,24,32,44,93,52],columns=["Code INSEE région","Région", "Population_2020","ANNEE_2020"])

df_Population_2020["Code INSEE région"]=[53,75,11,27,84,28,76,24,32,44,93,52]
df_Population_2020["Région"]= ['Bretagne', 'Nouvelle-Aquitaine', 'Île-de-France',
       'Bourgogne-Franche-Comté', 'Auvergne-Rhône-Alpes', 'Normandie',
       'Occitanie', 'Centre-Val de Loire', 'Hauts-de-France', 'Grand Est',
       "Provence-Alpes-Côte d'Azur", 'Pays de la Loire']
df_Population_2020["Population_2020"]=[3358524,6018424,12291557,2794517,8064146,3313432,5951850,2565726,5987795,5536002,5077582,3818421]
df_Population_2020["ANNEE_2020"]=[2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020]
df_Population_2020

#Création du df population 2020 au format csv
df_Population_2020.to_csv (path_or_buf= "df_Population_2020.csv",
                 sep= ";",
                 header= True)

#Création du df population 2013
df_Population_2013=pd.DataFrame()

df_Population_2013=pd.DataFrame(data=df_Population, index=[53,75,11,27,84,28,76,24,32,44,93,52],columns=["Code INSEE région","Région", "Population_2013","ANNEE_2013"])

df_Population_2013["Code INSEE région"]=[53,75,11,27,84,28,76,24,32,44,93,52]
df_Population_2013["Région"]= ['Bretagne', 'Nouvelle-Aquitaine', 'Île-de-France',
       'Bourgogne-Franche-Comté', 'Auvergne-Rhône-Alpes', 'Normandie',
       'Occitanie', 'Centre-Val de Loire', 'Hauts-de-France', 'Grand Est',
       "Provence-Alpes-Côte d'Azur", 'Pays de la Loire']
df_Population_2013["Population_2013"]=[3258707,5844177,11959807,2819783,7757595,3328364,5683878,2570548,5987883,5552388,4953675,3660852]
df_Population_2013["ANNEE_2013"]=[2013,2013,2013,2013,2013,2013,2013,2013,2013,2013,2013,2013]
df_Population_2013

df_Population_2013.to_csv (path_or_buf= "df_Population_2013.csv",
                 sep= ";",
                 header= True)

#Création du df population 2014 + format csv
df_Population_2014=pd.DataFrame()

df_Population_2014=pd.DataFrame(data=df_Population, index=[53,75,11,27,84,28,76,24,32,44,93,52],columns=["Code INSEE région","Région", "Population_2014","ANNEE_2014"])

df_Population_2014["Code INSEE région"]=[53,75,11,27,84,28,76,24,32,44,93,52]
df_Population_2014["Région"]= ['Bretagne', 'Nouvelle-Aquitaine', 'Île-de-France',
       'Bourgogne-Franche-Comté', 'Auvergne-Rhône-Alpes', 'Normandie',
       'Occitanie', 'Centre-Val de Loire', 'Hauts-de-France', 'Grand Est',
       "Provence-Alpes-Côte d'Azur", 'Pays de la Loire']
df_Population_2014["Population_2014"]=[3276543,5879144,12027565,2820623,7820966,3335645,5730753,2577435,6006156,5554645,4983438,3690833]
df_Population_2014["ANNEE_2014"]=[2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014,2014]


df_Population_2014.to_csv (path_or_buf= "df_Population_2014.csv",
                 sep= ";",
                 header= True)
df_Population_2014

#Création du df population 2015 + format csv
df_Population_2015=pd.DataFrame()

df_Population_2015=pd.DataFrame(data=df_Population, index=[53,75,11,27,84,28,76,24,32,44,93,52],columns=["Code INSEE région","Région", "Population_2015","ANNEE_2015"])

df_Population_2015["Code INSEE région"]=[53,75,11,27,84,28,76,24,32,44,93,52]
df_Population_2015["Région"]= ['Bretagne', 'Nouvelle-Aquitaine', 'Île-de-France',
       'Bourgogne-Franche-Comté', 'Auvergne-Rhône-Alpes', 'Normandie',
       'Occitanie', 'Centre-Val de Loire', 'Hauts-de-France', 'Grand Est',
       "Provence-Alpes-Côte d'Azur", 'Pays de la Loire']
df_Population_2015["Population_2015"]=[3293850,5911482,12082144,2820940,7877698,3339131,5774185,2578592,6009976,5559051,5007977,3718512]
df_Population_2015["ANNEE_2015"]=[2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015,2015]


df_Population_2015.to_csv (path_or_buf= "df_Population_2015.csv",
                 sep= ";",
                 header= True)
df_Population_2015

#Création du df population 2016 + format csv
df_Population_2016=pd.DataFrame()

df_Population_2016=pd.DataFrame(data=df_Population, index=[53,75,11,27,84,28,76,24,32,44,93,52],columns=["Code INSEE région","Région", "Population_2016","ANNEE_2016"])

df_Population_2016["Code INSEE région"]=[53,75,11,27,84,28,76,24,32,44,93,52]
df_Population_2016["Région"]= ['Bretagne', 'Nouvelle-Aquitaine', 'Île-de-France',
       'Bourgogne-Franche-Comté', 'Auvergne-Rhône-Alpes', 'Normandie',
       'Occitanie', 'Centre-Val de Loire', 'Hauts-de-France', 'Grand Est',
       "Provence-Alpes-Côte d'Azur", 'Pays de la Loire']
df_Population_2016["Population_2016"]=[3306529,5935603,12117132,2818338,7916889,3335929,5808435,2577866,6006870,5555186,5021928,3737632]
df_Population_2016["ANNEE_2016"]=[2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016]


df_Population_2016.to_csv (path_or_buf= "df_Population_2016.csv",
                 sep= ";",
                 header= True)
df_Population_2016

#Création du df population 2017 + format csv
df_Population_2017=pd.DataFrame()

df_Population_2017=pd.DataFrame(data=df_Population, index=[53,75,11,27,84,28,76,24,32,44,93,52],columns=["Code INSEE région","Région", "Population_2017","ANNEE_2017"])

df_Population_2017["Code INSEE région"]=[53,75,11,27,84,28,76,24,32,44,93,52]
df_Population_2017["Région"]= ['Bretagne', 'Nouvelle-Aquitaine', 'Île-de-France',
       'Bourgogne-Franche-Comté', 'Auvergne-Rhône-Alpes', 'Normandie',
       'Occitanie', 'Centre-Val de Loire', 'Hauts-de-France', 'Grand Est',
       "Provence-Alpes-Côte d'Azur", 'Pays de la Loire']
df_Population_2017["Population_2017"]=[3318904,5956978,12174880,2811423,7948287,3330478,5845102,2576252,6003815,5549586,5030890,3757600]
df_Population_2017["ANNEE_2017"]=[2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017]


df_Population_2017.to_csv (path_or_buf= "df_Population_2017.csv",
                 sep= ";",
                 header= True)
df_Population_2017

# Importer le fichier et afficher les premières lignes du dataset énergie :
import pandas as pd
%matplotlib inline
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv('D:\projet_energie.csv',sep =';', index_col=0)
df.head(12)

#Affichage
print(df_Population_2018.columns)
print(df.columns)
df.shape

#Rapprochement des données 2013 du df population 2018-2020
df_Population_nettoye=df.merge(right=df_Population_2013, left_on=["Code INSEE région","Région","Annee"], right_on=["Code INSEE région","Région","ANNEE_2013"], how="outer")
df_Population_nettoye.head()

#Rapprochement des données 2014 du df population 2018-2020
df_Population_nettoye=df_Population_nettoye.merge(right=df_Population_2014, left_on=["Code INSEE région","Région","Annee"], right_on=["Code INSEE région","Région","ANNEE_2014"], how="outer")
df_Population_nettoye.head()

#Rapprochement des données 2015 du df population 2018-2020
df_Population_nettoye=df_Population_nettoye.merge(right=df_Population_2015, left_on=["Code INSEE région","Région","Annee"], right_on=["Code INSEE région","Région","ANNEE_2015"], how="outer")
df_Population_nettoye.head()

#Rapprochement des données 2016 du df population 2018-2020
df_Population_nettoye=df_Population_nettoye.merge(right=df_Population_2016, left_on=["Code INSEE région","Région","Annee"], right_on=["Code INSEE région","Région","ANNEE_2016"], how="outer")
df_Population_nettoye.head()

#Rapprochement des données 2017 du df population 2018-2020
df_Population_nettoye=df_Population_nettoye.merge(right=df_Population_2017, left_on=["Code INSEE région","Région","Annee"], right_on=["Code INSEE région","Région","ANNEE_2017"], how="outer")
df_Population_nettoye.head()

#Rapprochement des données 2018 du df population 2018-2020
df_Population_nettoye=df_Population_nettoye.merge(right=df_Population_2018, left_on=["Code INSEE région","Région","Annee"], right_on=["Code INSEE région","Région","ANNEE_2018"], how="outer")
df_Population_nettoye.head()

#Rapprochement des données 2019 du df population 2018-2020
df_Population_nettoye=df_Population_nettoye.merge(right=df_Population_2019, left_on=["Code INSEE région","Région","Annee"], right_on=["Code INSEE région","Région","ANNEE_2019"], how="outer")
df_Population_nettoye.head()

#Rapprochement des données 2020 du df population 2018-2020
df_Population_nettoye=df_Population_nettoye.merge(right=df_Population_2020, left_on=["Code INSEE région","Région","Annee"], right_on=["Code INSEE région","Région","ANNEE_2020"], how="outer")
df_Population_nettoye.head()

#Affichage
print(df_Population_2019.columns)
print(df_Population_nettoye.columns)
df_Population_2019.head()
print(df_Population_nettoye["Annee"].unique())

#Rapprochement des données 2020 du df population 2018-2020
df_Population_nettoye=df_Population_nettoye.merge(right=df_Population_2020, left_on=["Code INSEE région","Région","Annee"], right_on=["Code INSEE région","Région","ANNEE_2020"], how="outer")
df_Population_nettoye.columns

#Vérification par année du rapprochement des données
df_Population_nettoye.groupby(["Annee"]).agg({"Population_2018":sum})
#df_Population_nettoye.groupby(["Annee"]).agg({"Population_2019":sum})
#df_Population_nettoye.groupby(["Annee"]).agg({"Population_2020":sum})

#Suppression des colonnes années
df_Population_nettoye=df_Population_nettoye.drop(["ANNEE_2018", "ANNEE_2019","ANNEE_2020"], axis=1)
df_Population_nettoye.columns

#Remplacement des NA par la valeur 0
df_Population_nettoye["Population_2013"]=df_Population_nettoye["Population_2013"].fillna(0)
df_Population_nettoye["Population_2014"]=df_Population_nettoye["Population_2014"].fillna(0)
df_Population_nettoye["Population_2015"]=df_Population_nettoye["Population_2015"].fillna(0)
df_Population_nettoye["Population_2016"]=df_Population_nettoye["Population_2016"].fillna(0)
df_Population_nettoye["Population_2017"]=df_Population_nettoye["Population_2017"].fillna(0)
df_Population_nettoye["Population_2018"]=df_Population_nettoye["Population_2018"].fillna(0)
df_Population_nettoye["Population_2019"]=df_Population_nettoye["Population_2019"].fillna(0)
df_Population_nettoye["Population_2020"]=df_Population_nettoye["Population_2020"].fillna(0)

#Affichage des informations du df
df_Population_nettoye.info()

#Création de la variable population totale
df_Population_nettoye["Population"]=df_Population_nettoye["Population_2013"]+df_Population_nettoye["Population_2014"]+df_Population_nettoye["Population_2015"]+df_Population_nettoye["Population_2016"]+df_Population_nettoye["Population_2017"]+df_Population_nettoye["Population_2018"]+df_Population_nettoye["Population_2019"]+df_Population_nettoye["Population_2020"]
df_Population_nettoye["Population"].unique()

#Visualisation des premières lignes du df
df_Population_nettoye.head()

#Affichage des populations sommées par année
df_Population_nettoye.groupby(["Annee"]).agg({"Population":sum})

#Suppression des variables TCH et TCO (redite)
df_Population_nettoye.drop(columns=['TCO Thermique (%)', 'TCH Thermique (%)', 'TCO Nucléaire (%)',
       'TCH Nucléaire (%)', 'TCO Eolien (%)', 'TCH Eolien (%)',
       'TCO Solaire (%)', 'TCH Solaire (%)', 'TCO Hydraulique (%)',
       'TCH Hydraulique (%)', 'TCO Bioénergies (%)', 'TCH Bioénergies (%)'], axis=1, inplace=True)
df_Population_nettoye.columns

#Suppression des variables années
df_Population_nettoye.drop(columns=['ANNEE_2013', 'ANNEE_2014', 'ANNEE_2015',
       'ANNEE_2016', 'ANNEE_2017', 'ANNEE_2018', 'ANNEE_2019', 'ANNEE_2020'], axis=1, inplace=True)
df_Population_nettoye.columns

#Création du df population au format csv
df_Population_nettoye.to_csv (path_or_buf= "df_Population_nettoye.csv",
                 sep= ";",
                 header= True)

#Vérification de l'enregistrement
df_Population_nettoye.tail(100000)

#Filtrage du df par année
df_Annee_2018=df_Population_nettoye.loc[df_Population_nettoye["Annee"]==2018]
df_Annee_2019=df_Population_nettoye.loc[df_Population_nettoye["Annee"]==2019]
df_Annee_2020=df_Population_nettoye.loc[df_Population_nettoye["Annee"]==2020]

#Valeurs uniques de la variable année
df_Population_nettoye.Annee.unique()

#Visualisation des colonnes du df
df_Population_nettoye.columns

#Matrice de corrélation entre les différentes productions
df_Population_nettoye_matrice=df_Population_nettoye[['Consommation (MW)','Thermique (MW)', 'Nucléaire (MW)', 'Eolien (MW)', 'Solaire (MW)',
       'Hydraulique (MW)', 'Bioénergies (MW)', 'Ech. physiques (MW)']]




plt.figure(figsize=(10,5))
sns.heatmap(df_Population_nettoye_matrice.corr(),annot=True, cmap="viridis")









