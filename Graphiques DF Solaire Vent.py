import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv('df_cleaned_merged.csv',sep =';')
df.head()

#suppression de la colonne Unnamed
df = df.drop('Unnamed: 0', axis=1)

#Affichage de l'enseoleillement solaire par régions
plt.figure(figsize=(10,7))
sns.lineplot(x='Région', y='solaire_max', data=df, label='Exposition Solaire')
plt.xlabel('Régions')
plt.xticks(rotation=45)
plt.ylabel('Exposition Solaire')
plt.grid()
plt.title('Ensoleillement des régions');

plt.figure(figsize=(20,10))
sns.barplot(x='Région', y='solaire_max', data=df, label='Exposition Solaire')
plt.xticks(rotation=45)
plt.xlabel('Régions')
plt.ylabel('Exposition Solaire')
plt.title('Ensoleillement des régions');

#Comparatif production solaire et exposition solaire des régions
plt.figure(figsize=(10,7))
sns.set_style("white")
sns.lineplot(x='Région', y='solaire_max', data=df, label='Exposition solaire')
sns.lineplot(x='Région', y='Solaire (MW)', data=df, label='Production d"énergie solaire')
plt.xticks(rotation=45)
plt.xlabel('Régions')
plt.title('Comparatif production solaire et exposition solaire des régions')
plt.show();

#Regroupement des DF de 2016 à 2020
df_2016_2020=df.loc[(df["Année"]==2016) |(df["Année"]==2017)|(df["Année"]==2018)|(df["Année"]==2019)|(df["Année"]==2020)]

df["Région"].unique()

#Production d energie solaire par régions
sns.relplot(x="Année", y='Solaire (MW)', kind="line", data=df_2016_2020 , hue='Région')
sns.xlim((2016,2020)
plt.title('Production energie solaire par régions')

#exposition solaire des régions
sns.relplot(x="Année", y='solaire_max', kind="line", data=df , hue ='Région', row_order="Région")
plt.xlim(2016,2020)
plt.title('Exposition solaire des régions');

#Production solaire par régions
sns.set_style('white')
plt.figure(figsize=(20,8))
sns.barplot(x='Région', y='Solaire (MW)',data=df, hue_order="Région")
plt.xticks(rotation=45)
plt.title('Production Solaire');

#Production eolienne par régions
sns.set_style('white')
plt.figure(figsize=(20,8))
sns.barplot(x='Région', y='Eolien (MW)',data=df, hue_order="Région")
plt.xticks(rotation=45)
plt.title('Production Eolienne');

#Expositions solaires des régions
sns.set_style('darkgrid')
plt.figure(figsize=(20,10))
sns.barplot(x='Région', y='solaire_max',data=df)
plt.xticks(rotation=45)
plt.title('Expositions solaires des régions');

#Moyenne de l'exposition solaire
df['avg_sol'] = df['solaire_min']+df['solaire_max']/2

#Exposition solaire des régions
sns.set_style('darkgrid')
plt.figure(figsize=(20,10))
sns.barplot(x='Région', y='avg_sol',data=df)
plt.xticks(rotation=45)
plt.title('Exposition solaire des régions');

#Table de corrélation
cor = df.corr()
fig, ax = plt.subplots(figsize=(12,12))
sns.heatmap(cor, annot= True, ax= ax, cmap="coolwarm");

#attention code prends beaucoup de temps
sns.regplot(x=df["solaire_max"], y=df["Solaire (MW)"], fit_reg=True)
plt.show(); #brouillon

#Exposition au vent des régions
sns.set_style('white')
plt.figure(figsize=(10,5))
sns.lineplot(x='Région', y='vent_max', data=df)
plt.xlabel('Régions')
plt.xticks(rotation=45)
plt.ylabel('Exposition Vent')
plt.title('Exposition au vent des régions');

#Exposition au vent des régions
plt.figure(figsize=(15,10))
sns.barplot(x='Région', y='vent_max', data=df, label='Vent')
plt.xlabel('Régions')
plt.xticks(rotation=45)
plt.ylabel('Exposition Vent')
plt.title('Exposition au vent des régions');

#Production Eolienne en France
sns.set_style('darkgrid')
plt.figure(figsize=(20,10))
sns.barplot(x='Région', y='Eolien (MW)',data=df)
plt.xticks(rotation=45)
plt.title('Production Eolienne en France');

#Comparatif Production Eolienne et Exposition au vent des régions
plt.figure(figsize=(10,7))
sns.lineplot(x='Région', y='vent_max', data=df, label='Exposition au Vent')
sns.lineplot(x='Région', y='Eolien (MW)', data=df, label='Production d Energie Eolienne')
plt.xticks(rotation=45)
plt.xlabel('Régions')
plt.title('Comparatif Production Eolienne et Exposition au vent des régions')
plt.show();

#Production Eolienne par régions
#df["Année"]=df["Année"].astype(int)
#df["Année"].unique()
sns.set_style("white")
sns.relplot(x="Année", y='Eolien (MW)', kind="line", data=df , hue ='Région', row_order="Région")
#plt.xlim(2016,2020)
#plt.title('Production Eolienne par régions');

#Exposition au vent des régions
sns.relplot(x="Année", y='vent_max', kind="line", data=df , hue ='Région', row_order="Région")
plt.xlim(2016,2020)
plt.title('Exposition au vent des régions');

# Test pearson sur données solaires
from scipy.stats import pearsonr
pd.DataFrame(pearsonr(df['Solaire (MW)'],df['solaire_max']), index = ['pearson_coeff','p-value'], columns = ['resultats_test'])

# Test pearson sur données vent
from scipy.stats import pearsonr
pd.DataFrame(pearsonr(df['Eolien (MW)'],df['vent_max']), index = ['pearson_coeff','p-value'], columns = ['resultats_test'])







