# Importer le fichier et afficher les premières lignes

import pandas as pd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv('df_dataset_energie.csv',sep =';', index_col=0)
df.head()

#Visualisation des colonnes
df.columns

#Visualisation des informations
df.info()

#Réalisation de tableaux de données par année
df.groupby(df["Annee"]).agg({"Consommation (MW)": sum})
#df.groupby(df["Annee"]).agg({"Production_totale": sum})
#df["Ecart"]=df["Production_totale"]- df["Consommation (MW)"]
#df.groupby(df["Annee"]).agg({"Ecart": sum})
#df.groupby(df["Annee"]).agg({"Ech. physiques (MW)": sum})

#Création de df filtré sur des années spécifiques
df_Annee_2018=df.loc[df["Annee"]==2018]
df_Annee_2019=df.loc[df["Annee"]==2019]
df_Annee_2020=df.loc[df["Annee"]==2020]
df["Ecart"]=df["Production_totale"]- df["Consommation (MW)"]

#Création d'un tableau de données par région
df_Annee_2020[["Production_totale", "Consommation (MW)","Région","Ecart","Ech. physiques (MW)"]].groupby("Région").sum()

# Création d'un tableau par année des types de production en % sur base totale production
df_prod = df[["Nucléaire (MW)", "Hydraulique (MW)", "Thermique (MW)", "Eolien (MW)", "Solaire (MW)", "Bioénergies (MW)",
              "Production_totale", "Annee"]].groupby("Annee").sum()

for col in df_prod.columns[:6]:
    df_prod[col] = ((df_prod[col] / df_prod['Production_totale']) * 100).round()

df_prod

# Analyse de la consommation MW par année NIVEAU FRANCE
plt.figure(figsize=(7, 7))
sns.lineplot(x='Annee', y='Consommation (MW)',label= "Consommation (MW)", data=df)
sns.lineplot(x='Annee', y='Production_totale',label= "Productions (MW)", data=df)
plt.xlim(2013,2020)
plt.grid(False)
plt.legend()
plt.title('Production/Consommation (MW) par année en FRANCE')
plt.show();

# Analyse par filière par année NIVEAU FRANCE
plt.figure(figsize=(7, 7))
#sns.lineplot(x='Annee', y='Consommation (MW)',label= "Consommation (MW)", data=df)
sns.lineplot(x='Annee', y='Thermique (MW)',label= "Thermique (MW)", data=df)
sns.lineplot(x='Annee', y='Nucléaire (MW)',label= "Nucléaire (MW)", data=df)
sns.lineplot(x='Annee', y="Eolien (MW)",label= "Eolien (MW)", data=df)
sns.lineplot(x='Annee', y='Solaire (MW)',label= 'Solaire (MW)', data=df)
sns.lineplot(x='Annee', y='Hydraulique (MW)',label= 'Hydraulique (MW)', data=df)
sns.lineplot(x='Annee', y='Bioénergies (MW)',label='Bioénergies (MW)', data=df)
plt.xlim(2013,2020)
plt.grid(False)
plt.legend()
plt.title('Filières (MW) par année en FRANCE')
plt.show();

#Courbe de consommation par jour entre 2013 et 2021
df= df.groupby(['Consommation (MW)', 'Date']).count().reset_index()
df.drop(df.iloc[:,2:],1,inplace=True)
df2=pd.pivot_table(df, index=['Date'], values=['Consommation (MW)'], aggfunc=np.sum)
df2 = df2.rename_axis('Date').reset_index()
df2['Date']= pd.to_datetime(df2['Date'])
values= df2['Date'].value_counts().sort_index()
plt.figure(figsize=(20,4))
plt.plot_date(values.index,df2['Consommation (MW)'], linestyle ='-', marker="");

# Courbe de la consommation par région entre 2013 et 2020
sns.relplot(x="Annee", y="Consommation (MW)",hue="Région",data=df, kind="line", )
plt.xlim(2013,2020)
plt.title("Cumul des consommations par région par an", fontsize=20)
plt.show()

#Courbe de la production éolienne par région entre 2013 et 2020
sns.relplot(x="Annee", y='Eolien (MW)', kind="line", data=df , hue ='Région', row_order="Région")
plt.xlim(2013,2020)
plt.title('production éolien par régions')

#Camembert représentatif de la répartition des différentes productions en France
name = ['Thermique','Nucléaire','Eolien', 'Solaire', 'Hydraulique', 'Bioénergie']
data = [378.7,3694.2,244,83,608,81]
explode=(0, 0.15, 0, 0,0,0)
plt.pie(data, explode=explode, labels=name, autopct='%1.1f%%', startangle=10, )
plt.show()

#Boxenplot de la consommation par région
plt.figure(figsize=(20,10))
sns.boxenplot(x="Région", y='Consommation (MW)', data = df, hue_order="Région")
plt.xticks(rotation=45)
plt.xlabel('Région')
plt.ylabel('Consommation (MW)')
plt.title('La consommation par régions');

#Liste des régions uniques du dataset
df["Région"].unique()

#Boxenplot de la consommation par région sur l'année 2018
df_Annee_2018=df.loc[df["Annee"]==2018]

plt.figure(figsize=(25,7))
sns.boxenplot(x='Région', y='Consommation (MW)',data = df_Annee_2018, order=['Bretagne', 'Nouvelle-Aquitaine', 'Île-de-France',
       'Bourgogne-Franche-Comté', 'Auvergne-Rhône-Alpes', 'Normandie',
       'Occitanie', 'Centre-Val de Loire', 'Hauts-de-France', 'Grand Est',
       "Provence-Alpes-Côte d'Azur", 'Pays de la Loire'])
plt.xticks(rotation=45)
plt.xlabel('Région')
plt.ylabel('Consommation (MW)')
plt.title('La consommation 2018 par régions');

#Courbe de la consommation par mois et par région
sns.relplot(
    data=df,
    x="Mois", y="Consommation (MW)",
    hue="Région", col_order="Région",
    kind="line")
plt.title("Cumul des consommations en fonction du mois de l'année", fontsize=20)
plt.xticks(np.arange(12),['Jan', 'Fév', 'Mar', 'Avr', 'Mai', 'Jun', 'Jul', 'Aoû', 'Sep', 'Oct', 'Nov', 'Déc']);

#Courbe de consommation et de productions entre 2013 et 2020
sns.lineplot(x='Annee', y='Consommation (MW)', data=df, label = ' Consommation')
sns.lineplot(x='Annee', y='Thermique (MW)', data=df, label = ' Thermique')
sns.lineplot(x='Annee', y='Nucléaire (MW)', data=df, label = ' Nucléaire ')
sns.lineplot(x='Annee', y='Eolien (MW)', data=df, label = ' Eolien')
sns.lineplot(x='Annee', y='Solaire (MW)', data=df, label = ' Solaire ')
sns.lineplot(x='Annee', y='Bioénergies (MW)', data=df, label = ' Bioénergies')
sns.lineplot(x='Annee', y='Hydraulique (MW)', data=df, label = ' Hydraulique ')
plt.xlim(2013,2020)
plt.title(label='Différentes productions et la consommation')
plt.xlabel('Année')
plt.ylabel('')
plt.legend(loc=2, bbox_to_anchor=(1,1))
plt.show();

#Courbe de consommation par jour de la semaine
sns.relplot(
    data=df,
    x="Jour_semaine", y="Consommation (MW)",
    hue="Région", row_order="Région",
    kind="line")
plt.title("Cumul des consommations en fonction du jour de la semaine", fontsize=20)
plt.xlabel("Jours de la Semaine")
plt.xticks(np.arange(7),['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche']);

#Boxenplot de la consommation par région sur l'année 2019
df_Annee_2019=df.loc[df["Annee"]==2019]
plt.figure(figsize=(20,7))
sns.boxenplot(x='Région', y='Consommation (MW)', data = df_Annee_2019, order= ['Bretagne', 'Nouvelle-Aquitaine', 'Île-de-France',
       'Bourgogne-Franche-Comté', 'Auvergne-Rhône-Alpes', 'Normandie',
       'Occitanie', 'Centre-Val de Loire', 'Hauts-de-France', 'Grand Est',
       "Provence-Alpes-Côte d'Azur", 'Pays de la Loire'])
plt.xticks(rotation=45)
plt.xlabel('Région')
plt.ylabel('Consommation (MW)')
plt.title('La consommation 2019 par régions');

#Boxenplot de la consommation par région sur l'année 2020
df_Annee_2020=df.loc[df["Annee"]==2020]
plt.figure(figsize=(20,7))
sns.boxenplot(x='Région', y='Consommation (MW)', data = df_Annee_2020,order= ['Bretagne', 'Nouvelle-Aquitaine', 'Île-de-France',
       'Bourgogne-Franche-Comté', 'Auvergne-Rhône-Alpes', 'Normandie',
       'Occitanie', 'Centre-Val de Loire', 'Hauts-de-France', 'Grand Est',
       "Provence-Alpes-Côte d'Azur", 'Pays de la Loire'])
plt.xticks(rotation=45)
plt.xlabel('Région')
plt.ylabel('Consommation (MW)')
plt.title('La consommation 2020 par régions');

#Courbe de consommation par mois et par région année 2018
df_Annee_2018=df.loc[df["Annee"]==2018]
sns.relplot(
    data=df_Annee_2018,
    x="Mois", y="Consommation (MW)",
    hue="Région", kind="line",hue_order= ['Bretagne', 'Nouvelle-Aquitaine', 'Île-de-France',
       'Bourgogne-Franche-Comté', 'Auvergne-Rhône-Alpes', 'Normandie',
       'Occitanie', 'Centre-Val de Loire', 'Hauts-de-France', 'Grand Est',
       "Provence-Alpes-Côte d'Azur", 'Pays de la Loire'])
plt.title("Cumul des consommations en fonction du mois de l'année", fontsize=20)
plt.xticks(np.arange(12),['Jan', 'Fév', 'Mar', 'Avr', 'Mai', 'Jun', 'Jul', 'Aoû', 'Sep', 'Oct', 'Nov', 'Déc']);

#Courbe de consommation par mois et par région année 2019
df_Annee_2019=df.loc[df["Annee"]==2019]
sns.relplot(
    data=df_Annee_2019,
    x="Mois", y="Consommation (MW)",hue_order= ['Bretagne', 'Nouvelle-Aquitaine', 'Île-de-France',
       'Bourgogne-Franche-Comté', 'Auvergne-Rhône-Alpes', 'Normandie',
       'Occitanie', 'Centre-Val de Loire', 'Hauts-de-France', 'Grand Est',
       "Provence-Alpes-Côte d'Azur", 'Pays de la Loire'],
    hue="Région",
    kind="line")
plt.title("Cumul des consommations en fonction du mois de l'année", fontsize=20)
plt.xticks(np.arange(12),['Jan', 'Fév', 'Mar', 'Avr', 'Mai', 'Jun', 'Jul', 'Aoû', 'Sep', 'Oct', 'Nov', 'Déc']);

#Courbe de consommation par mois et par région année 2020
df_Annee_2020=df.loc[df["Annee"]==2020]
sns.relplot(
    data=df_Annee_2020,
    x="Mois", y="Consommation (MW)",
    hue="Région",
    kind="line",hue_order= ['Bretagne', 'Nouvelle-Aquitaine', 'Île-de-France',
       'Bourgogne-Franche-Comté', 'Auvergne-Rhône-Alpes', 'Normandie',
       'Occitanie', 'Centre-Val de Loire', 'Hauts-de-France', 'Grand Est',
       "Provence-Alpes-Côte d'Azur", 'Pays de la Loire'])
plt.title("Cumul des consommations en fonction du mois de l'année", fontsize=20)
plt.xticks(np.arange(12),['Jan', 'Fév', 'Mar', 'Avr', 'Mai', 'Jun', 'Jul', 'Aoû', 'Sep', 'Oct', 'Nov', 'Déc']);

#Courbe de consommation par jour de la semaine et par région
sns.relplot(x="Jour_semaine", y="Consommation (MW)",data=df,hue="Région",kind="line")

plt.title("Cumul des consommations en fonction du jour de la semaine", fontsize=20)
plt.xlabel("Jours de la Semaine")
plt.xticks(np.arange(7),['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche']);

#Courbe de consommation par mois et par région année 2018
df_Annee_2018=df.loc[df["Annee"]==2018]
sns.relplot(
    data=df_Annee_2018,
    x="Mois", y="Consommation (MW)",
    hue="Région", kind="line")
plt.title("Cumul des consommations en fonction du mois de l'année", fontsize=20)
plt.xticks(np.arange(12),['Jan', 'Fév', 'Mar', 'Avr', 'Mai', 'Jun', 'Jul', 'Aoû', 'Sep', 'Oct', 'Nov', 'Déc'])

#Courbe de consommation par mois et par région
sns.relplot(
    data=df,
    x="Mois", y="Consommation (MW)",
    hue="Région",
    kind="line", row_order="Région")
plt.title("Cumul des consommations en fonction du mois de l'année", fontsize=20)
plt.xticks(np.arange(12),['Jan', 'Fév', 'Mar', 'Avr', 'Mai', 'Jun', 'Jul', 'Aoû', 'Sep', 'Oct', 'Nov', 'Déc']);

#Courbe de consommation et de production_totale par mois
sns.lineplot(x='Mois', y='Production_totale', data=df, label = ' Productions (MW)')
sns.lineplot(x='Mois', y='Consommation (MW)', data=df, label = ' Consommation (MW) ')
plt.xticks([2,4,6,8,10,12],['Février', 'Avril','Juin', 'Août', 'Octobre', 'Décembre']);

#Courbe de consommation et de production_totale par mois année 2020
df_Annee_2020=df.loc[df["Annee"]==2020]
sns.lineplot(x='Mois', y='Production_totale', data=df_Annee_2020, label = ' Productions (MW)')
sns.lineplot(x='Mois', y='Consommation (MW)', data=df_Annee_2020, label = ' Consommation (MW) ')
plt.xticks([2,4,6,8,10,12],['Février', 'Avril','Juin', 'Août', 'Octobre', 'Décembre']);

#Courbe de consommation et de production_totale par jour de la semaine année 2018
df_Annee_2018=df.loc[df["Annee"]==2018]
sns.lineplot(x='Jour_semaine', y='Production_totale', data=df_Annee_2018, label = ' Productions (MW)')
sns.lineplot(x='Jour_semaine', y='Consommation (MW)', data=df_Annee_2018, label = ' Consommation (MW) ')
plt.xticks(np.arange(7),['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche'])

#Courbe de consommation et de production_totale par heure année 2020
df_Annee_2020=df.loc[df["Annee"]==2020]
sns.lineplot(x='Heure', y='Production_totale', data=df_Annee_2020, label = ' Productions (MW)')
sns.lineplot(x='Heure', y='Consommation (MW)', data=df_Annee_2020, label = ' Consommation (MW) ')
plt.show();

#Graphique en barre de l'échelle physique par région
sns.set_style('darkgrid')
plt.figure(figsize=(15,8))
sns.barplot(x='Région', y='Ech. physiques (MW)',data=df)
plt.xticks(rotation=45)
plt.title('Ech.physiques par régions')

#Description des variables par année 2018,2019 et 2020
#df_Annee_2020.describe()
#df_Annee_2019.describe()
df_Annee_2018.describe()

#Camembert repartition des productions en 2018
name = ['Thermique','Nucléaire','Eolien', 'Solaire', 'Hydraulique', 'Bioénergie']
data = [361,3738,268,101,641,91]
explode=(0, 0.15, 0, 0,0,0)
plt.pie(data, explode=explode, labels=name, autopct='%1.1f%%', startangle=10)
plt.title("Répartition production 2018")
plt.show()

#Camembert repartition des productions en 2019
name = ['Thermique','Nucléaire','Eolien', 'Solaire', 'Hydraulique', 'Bioénergie']
data = [391,3608,322,115,566,92]
explode=(0, 0.15, 0, 0,0,0)
plt.pie(data, explode=explode, labels=name, autopct='%1.1f%%', startangle=10)
plt.title("Répartition production 2019")
plt.show()

#Camembert repartition des productions en 2020
name = ['Thermique','Nucléaire','Eolien', 'Solaire', 'Hydraulique', 'Bioénergie']
data = [348,3180,372,120,611,89]
explode=(0, 0.15, 0, 0,0,0)
plt.pie(data, explode=explode, labels=name, autopct='%1.1f%%', startangle=10)
plt.title("Répartition production 2020")
plt.show()

#Histogramme des productions par région
df_group = df.groupby(['Région', 'Eolien (MW)', 'Solaire (MW)', 'Thermique (MW)', 'Bioénergies (MW)']).count().reset_index()
df_group.drop(df_group.iloc[:,7:],1,inplace=True)
df_group=pd.pivot_table(df_group, index=['Région'], values=['Eolien (MW)', 'Solaire (MW)', 'Thermique (MW)', 'Bioénergies (MW)'], aggfunc=np.sum)
df_sum = df_group.rename_axis('Région').reset_index()
barWidth = 0.8
df_sum.plot.bar(x='Région',y=['Eolien (MW)', 'Solaire (MW)', 'Thermique (MW)', 'Bioénergies (MW)'],figsize=(10,5),width = barWidth)

#Production hydraulique par région et année
sns.relplot(x="Annee", y='Hydraulique (MW)', kind="line", data=df , hue ='Région')
plt.xlim(2013,2020)
plt.title('Production Hydraulique par région')

#Histogramme des productions nucléaire et hydraulique par région
df_group = df.groupby(['Région', 'Nucléaire (MW)','Hydraulique (MW)']).count().reset_index()
df_group.drop(df_group.iloc[:,7:],1,inplace=True)
df_group=pd.pivot_table(df_group, index=['Région'], values=['Nucléaire (MW)','Hydraulique (MW)'], aggfunc=np.sum)
df_sum = df_group.rename_axis('Région').reset_index()
barWidth = 0.8
df_sum.plot.bar(x='Région',y=['Nucléaire (MW)','Hydraulique (MW)'],figsize=(5,5),width = barWidth)



