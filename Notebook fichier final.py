#Ouverture du fichier final
import pandas as pd

df=pd.read_csv("df_final.csv", ";", index_col=0, header=0)

df.head(1)

#Visualisation des colonnes du df
df.columns

#Visualisation des informations du df
df.info()

#Tableau présentant par région les données superficie, population et densité
df.groupby("Libellé Région").agg({"Superficie (km²)": "max", "Population": "max", "Densite (hab/km²)": "max"})

#Filtrage du df sur les années 2016-2020
df_2016_2020=df.loc[(df["Annee"]==2016) | (df["Annee"]==2017) | (df["Annee"]==2018) | (df["Annee"]==2019) |(df["Annee"]==2020)]
#df_2016_2020.groupby("Libellé Région").agg({'tmin': "min", 'tmax': "max", 'tmoy': "mean"})
#Tableau par région des températures moyennes
df_2016_2020.groupby("Libellé Région").agg({'tmoy': "mean"})
#,df_2016_2020.agg({'tmoy': "mean"})

# Tableau par région des températures moyennes et des productions solaires
df_2016_2020.groupby("Libellé Région").agg({'tmoy': "mean", "Solaire (MW)": "mean"})

#Tableau par région des indicateurs ci-dessous
df_2016_2020.groupby("Libellé Région").agg({'tmoy': "mean", "Solaire (MW)": "mean", "Rayonnement solaire global (W/m2)": "mean","Eolien (MW)": "mean", "Vitesse du vent à 100m (m/s)":"mean"})

#Filtrage du df sur les années 2013-2019
df_2013_2019=df.loc[(df["Annee"]==2013) | (df["Annee"]==2014) | (df["Annee"]==2015) | (df["Annee"]==2016) |(df["Annee"]==2017)|(df["Annee"]==2018)|(df["Annee"]==2019)]

#Indicateurs moyennisés à l'echelle France
df_2013_2019.agg({'Consommation Agriculture (MWh)':"mean",
       'Consommation Industrie (MWh)':"mean", 'Consommation Tertiaire  (MWh)': "mean",
       'Consommation Résidentiel  (MWh)':"mean", 'Consommation Secteur Inconnu (MWh)':"mean"}).round().astype(int)

#"Consommation totale (MWh)":"sum"

#Echelle régions
#df_2013_2019.groupby("Libellé Région").agg({'Consommation Agriculture (MWh)':"sum",
       #'Consommation Industrie (MWh)':"sum", 'Consommation Tertiaire  (MWh)': "sum",
       #'Consommation Résidentiel  (MWh)':"sum", 'Consommation Secteur Inconnu (MWh)':"sum"})

#Camembert de la répartition des consommations par secteur d'activités
import matplotlib.pyplot as plt

plt.pie(df_conso, labels= ["Consommation Agriculture (MWh)",
       'Consommation Industrie (MWh)', 'Consommation Tertiaire  (MWh)',
       'Consommation Résidentiel  (MWh)', 'Consommation Secteur Inconnu (MWh)'], autopct='%1.0f%%', startangle=15)
plt.show()

#Consommation moyenne par secteur d'activités entre 2013 et 2019
df_conso2=df_2013_2019.agg({'Consommation Agriculture (MWh)':"mean",
       'Consommation Industrie (MWh)':"mean", 'Consommation Tertiaire  (MWh)': "mean",
       'Consommation Résidentiel  (MWh)':"mean", 'Consommation Secteur Inconnu (MWh)':"mean","Consommation totale (MWh)":"mean"})
df_conso2.round().astype(int)

#Echelle régions
df_conso3=df_2013_2019.groupby("Libellé Région").agg({'Consommation Agriculture (MWh)':"mean",
       'Consommation Industrie (MWh)':"mean", 'Consommation Tertiaire  (MWh)': "mean",
       'Consommation Résidentiel  (MWh)':"mean", 'Consommation Secteur Inconnu (MWh)':"mean", "Consommation totale (MWh)":"mean"})
df_conso3.round().astype(int)

#Filtrage du df sur les années 2013-2020
df_2013_2020=df.loc[(df["Annee"]==2013) | (df["Annee"]==2014) | (df["Annee"]==2015) | (df["Annee"]==2016) |(df["Annee"]==2017)|(df["Annee"]==2018)|(df["Annee"]==2019)|(df["Annee"]==2020)]

#Tableau des indicateurs ci-dessous par région entre 2013 et 2020
df_2013_2020.groupby("Libellé Région").agg({"Consommation (MW)":"mean", "Production_totale":"mean","Ech. physiques (MW)":"mean"})

# Conso, production totale et echelle physique entre 2013 et 2020
df_cs=df_2013_2020.agg({"Consommation (MW)":"mean", "Production_totale":"mean","Ech. physiques (MW)":"mean"})
df_cs.round()

#Répartition en % des différentes productions sur production totale par année
df_prod=df_2013_2020[["Nucléaire (MW)","Thermique (MW)","Hydraulique (MW)", "Eolien (MW)", "Solaire (MW)","Bioénergies (MW)","Production_totale","Annee"]].groupby("Annee").mean()
for col in df_prod.columns[:6]:
    df_prod[col]=((df_prod[col]/df_prod['Production_totale'])*100).round()
df_prod.round()

#Productions moyenne entre 2013 et 2020 échelle France
df_prd=df_2013_2020[["Nucléaire (MW)","Thermique (MW)","Hydraulique (MW)", "Eolien (MW)", "Solaire (MW)","Bioénergies (MW)",'Production_totale']].agg("mean")
df_prd.round()

#Consommation mensuelle moyenne entre 2013 et 2020
df_2013_2020[["Consommation (MW)","Mois"]].groupby(["Mois"]).agg("mean")

#Consommation journalière moyenne entre 2013 et 2020 échelle France
df_2013_2020[["Consommation (MW)","Jour_semaine"]].groupby(["Jour_semaine"]).agg("mean")

#Consommation à l'heure moyenne entre 2013 et 2020 à l'échelle France
df_2013_2020[["Consommation (MW)","Heure"]].groupby(["Heure"]).agg("mean")

#Productions moyenne par région entre 2013 et 2020
df_2013_2020.groupby("Libellé Région").agg({'Thermique (MW)':"mean", 'Nucléaire (MW)':"mean", 'Eolien (MW)':"mean", 'Solaire (MW)':"mean",
       'Hydraulique (MW)':"mean", 'Bioénergies (MW)':"mean"})

#Consommation moyenne par région et mois entre 2013 et 2020
df_2013_2020.groupby(["Libellé Région", "Mois"]).agg({"Consommation (MW)":"mean"})

#Consommation moyenne et Population par région entre 2013 et 2020
df_2013_2020.groupby(["Libellé Région"]).agg({"Population":"max", "Consommation (MW)": "mean"}).sort_values(["Population"], ascending=False).round().astype(int)

#TEST corrélation entre consommation et population
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.DataFrame(data=df_2013_2020, index=None, columns=["Consommation (MW)", "Population"], dtype=None, copy=None)
cor=df.corr(method="pearson")

fig, ax = plt.subplots(figsize=(5,5))
sns.heatmap(cor, annot= True, ax= ax, cmap="coolwarm");

import scipy.stats as stats

stats.f_oneway(df["Consommation (MW)"],df['Population'])

import statsmodels.api as sm
from statsmodels.formula.api import ols
df["Consommation"]=df["Consommation (MW)"]
ols("Consommation ~ Population", data= df).fit()

model = ols("Consommation ~ Population", data=df).fit()
aov_table = sm.stats.anova_lm(model, typ=2)
aov_table

#Test Anova
import statsmodels.api
result = statsmodels.formula.api.ols('Consommation ~ Population', data = df).fit()
table = statsmodels.api.stats.anova_lm(result)
table

# Test pearson
from scipy.stats import pearsonr
pd.DataFrame(pearsonr(df['Consommation'],df['Population']), index = ['pearson_coeff','p-value'], columns = ['resultat_test'])

#TEST corrélation entre consommation et densite
df1=pd.DataFrame(data=df_2013_2020, index=None, columns=["Consommation (MW)", "Densite (hab/km²)"], dtype=None, copy=None)
cor=df1.corr(method="pearson")

fig, ax = plt.subplots(figsize=(5,5))
sns.heatmap(cor, annot= True, ax= ax, cmap="coolwarm");

import scipy.stats as stats

stats.f_oneway(df1["Consommation (MW)"],df1['Densite (hab/km²)'])

import statsmodels.api as sm
from statsmodels.formula.api import ols
df1["Consommation"]=df1["Consommation (MW)"]
df1["Densite"]=df1["Densite (hab/km²)"]
ols("Consommation ~ Densite", data= df1).fit()

model = ols("Consommation ~ Densite", data=df1).fit()
aov_table = sm.stats.anova_lm(model, typ=2)
aov_table

import statsmodels.api as sm
from statsmodels.formula.api import ols
df1["Consommation"]=df1["Consommation (MW)"]
df1["Densite"]=df1["Densite (hab/km²)"]
ols("Consommation ~ Densite", data= df1).fit()

model = ols("Consommation ~ Densite", data=df1).fit()
aov_table = sm.stats.anova_lm(model, typ=2)
aov_table

# Test pearson
from scipy.stats import pearsonr
pd.DataFrame(pearsonr(df1['Consommation'],df1['Densite']), index = ['pearson_coeff','p-value'], columns = ['resultat_test'])

#Consommation moyenne et densité par région entre 2013 et 2020
df_2013_2020.groupby(["Libellé Région"]).agg({"Densite (hab/km²)":"max", "Consommation (MW)": "mean"}).sort_values(["Densite (hab/km²)"], ascending=False).round().astype(int)

#TEST corrélation entre consommation et Superficie
df2=pd.DataFrame(data=df_2013_2020, index=None, columns=["Consommation (MW)", "Superficie (km²)"], dtype=None, copy=None)
cor=df2.corr(method="pearson")

fig, ax = plt.subplots(figsize=(5,5))
sns.heatmap(cor, annot= True, ax= ax, cmap="coolwarm");

import scipy.stats as stats

stats.f_oneway(df2["Consommation (MW)"],df2['Superficie (km²)'])

import statsmodels.api as sm
from statsmodels.formula.api import ols
df2["Consommation"]=df2["Consommation (MW)"]
df2["Superficie"]=df2["Superficie (km²)"]
ols("Consommation ~ Superficie", data= df2).fit()

model = ols("Consommation ~ Superficie", data=df2).fit()
aov_table = sm.stats.anova_lm(model, typ=2)
aov_table

# Test pearson
from scipy.stats import pearsonr
pd.DataFrame(pearsonr(df2['Consommation'],df2['Superficie']), index = ['pearson_coeff','p-value'], columns = ['resultat_test'])

#Consommation moyenne et superficie par région entre 2013 et 2020
df_2013_2020.groupby(["Libellé Région"]).agg({"Superficie (km²)":"max", "Consommation (MW)": "mean"}).sort_values(["Superficie (km²)"], ascending=False).round().astype(int)

#Filtrage du df sur les années 2016-2020
df_2016_2020=df.loc[(df["Annee"]==2016) | (df["Annee"]==2017) | (df["Annee"]==2018) | (df["Annee"]==2019) |(df["Annee"]==2020)]
#Consommation et température moyenne par région entre 2016 et 2020
df4=df_2016_2020.groupby(["Libellé Région"]).agg({"Consommation (MW)": "mean", "tmoy":"mean"})

#TEST corrélation entre consommation et température moyenne
df5=pd.DataFrame(data=df4, index=None, columns=["Consommation (MW)", "tmoy"], dtype=None, copy=None)
cor=df5.corr(method="pearson")

fig, ax = plt.subplots(figsize=(5,5))
sns.heatmap(cor, annot= True, ax= ax, cmap="coolwarm");

import scipy.stats as stats

stats.f_oneway(df5["Consommation (MW)"],df5['tmoy'])

import statsmodels.api as sm
from statsmodels.formula.api import ols
df5["Consommation"]=df5["Consommation (MW)"]

ols("Consommation ~ tmoy", data= df5).fit()

model = ols("Consommation ~ tmoy", data=df5).fit()
aov_table = sm.stats.anova_lm(model, typ=2)
aov_table

# Test pearson
from scipy.stats import pearsonr
pd.DataFrame(pearsonr(df5['Consommation'],df5['tmoy']), index = ['pearson_coeff','p-value'], columns = ['resultat_test'])

#Consommation et température moyenne par région entre 2016 et 2020 (trié sur tmoy)
df_2016_2020.groupby(["Libellé Région"]).agg({"tmoy":"mean", "Consommation (MW)": "mean"}).sort_values(["tmoy"], ascending=False)

#Filtrage du df sur années 2016-2020
df_2016_2020=df.loc[(df["Annee"]==2016) | (df["Annee"]==2017) | (df["Annee"]==2018) | (df["Annee"]==2019) |(df["Annee"]==2020)]
#Consommation et température moyenne par mois entre 2016 et 2020
df5=df_2016_2020.groupby(["Mois"]).agg({"Consommation (MW)": "mean", "tmoy":"mean"})

#TEST corrélation entre consommation et température moyenne par mois
df6=pd.DataFrame(data=df5, index=None, columns=["Consommation (MW)", "tmoy"], dtype=None, copy=None)
cor=df6.corr(method="pearson")

fig, ax = plt.subplots(figsize=(5,5))
sns.heatmap(cor, annot= True, ax= ax, cmap="coolwarm");

#Test de linéarité entre la consommation et la température moyenne par mois
sns.regplot(x=df6["tmoy"], y=df6["Consommation (MW)"], fit_reg=True)

#Les régions uniques du df
df["Libellé Région"].unique()

#Filtrage du df sur les années 2016-2020 et la région Provence
df_2016_2020_PROVENCE=df.loc[(df["Annee"]==2016) | (df["Annee"]==2017) | (df["Annee"]==2018) | (df["Annee"]==2019) |(df["Annee"]==2020) & (df["Libellé Région"]=="Provence-Alpes-Côte d'Azur")]
#Consommation et température moyenne par mois en Provence entre 2016 et 2020
df_2016_2020_PROVENCE.groupby(["Mois"]).agg({"Consommation (MW)": "mean", "tmoy":"mean"})

#Tableau par région des indicateurs ci-dessous entre 2016 et 2020
df7=df_2016_2020.groupby("Libellé Région").agg({'tmoy': "mean", "Solaire (MW)": "mean", "Rayonnement solaire global (W/m2)": "mean","Eolien (MW)": "mean", "Vitesse du vent à 100m (m/s)":"mean"})

#TEST corrélation entre production solaire et rayonnement
df8=pd.DataFrame(data=df7, index=None, columns=["Solaire (MW)", "Rayonnement solaire global (W/m2)"], dtype=None, copy=None)
cor=df8.corr(method="pearson")

fig, ax = plt.subplots(figsize=(5,5))
sns.heatmap(cor, annot= True, ax= ax, cmap="coolwarm");

import scipy.stats as stats

stats.f_oneway(df8["Solaire (MW)"],df8["Rayonnement solaire global (W/m2)"])

import statsmodels.api as sm
from statsmodels.formula.api import ols
df8["Solaire"]=df8["Solaire (MW)"]
df8["Rayonnement"]=df8["Rayonnement solaire global (W/m2)"]

ols("Rayonnement ~ Solaire", data= df8).fit()

model = ols("Rayonnement ~ Solaire", data=df8).fit()
aov_table = sm.stats.anova_lm(model, typ=2)
aov_table

# Test pearson
from scipy.stats import pearsonr
pd.DataFrame(pearsonr(df8["Solaire"],df8["Rayonnement"]), index = ['pearson_coeff','p-value'], columns = ['resultat_test'])

#TEST corrélation entre production éolienne et vitesse du vent
df9=pd.DataFrame(data=df7, index=None, columns=["Eolien (MW)", "Vitesse du vent à 100m (m/s)"], dtype=None, copy=None)
cor=df9.corr(method="pearson")

fig, ax = plt.subplots(figsize=(5,5))
sns.heatmap(cor, annot= True, ax= ax, cmap="coolwarm");

import scipy.stats as stats

stats.f_oneway(df9["Eolien (MW)"],df9["Vitesse du vent à 100m (m/s)"])

import statsmodels.api as sm
from statsmodels.formula.api import ols
df9["Eolien"]=df9["Eolien (MW)"]
df9["Vent"]=df9["Vitesse du vent à 100m (m/s)"]

ols("Vent ~ Eolien", data= df9).fit()

model = ols("Vent ~ Eolien", data=df9).fit()
aov_table = sm.stats.anova_lm(model, typ=2)
aov_table

# Test pearson
from scipy.stats import pearsonr
pd.DataFrame(pearsonr(df9["Eolien"],df9["Vent"]), index = ['pearson_coeff','p-value'], columns = ['resultat_test'])

#Production totale moyenne et échelle physique par région entre 2013 et 2020
df11=df_2013_2020.groupby(["Libellé Région"]).agg({"Production_totale":"mean", "Ech. physiques (MW)":"mean"})

#TEST corrélation entre echelle physique et production totale
df10=pd.DataFrame(data=df11, index=None, columns=["Ech. physiques (MW)", "Production_totale"], dtype=None, copy=None)
cor=df10.corr(method="pearson")

fig, ax = plt.subplots(figsize=(5,5))
sns.heatmap(cor, annot= True, ax= ax, cmap="coolwarm");

import scipy.stats as stats

stats.f_oneway(df10["Ech. physiques (MW)"],df10["Production_totale"])

import statsmodels.api as sm
from statsmodels.formula.api import ols
df10["Echellephys"]=df10["Ech. physiques (MW)"]
df10["Production"]=df10["Production_totale"]

ols("Production ~ Echellephys", data= df10).fit()

model = ols("Production ~ Echellephys", data=df10).fit()
aov_table = sm.stats.anova_lm(model, typ=2)
aov_table

# Test pearson
from scipy.stats import pearsonr
pd.DataFrame(pearsonr(df10["Ech. physiques (MW)"],df10["Production_totale"]), index = ['pearson_coeff','p-value'], columns = ['resultat_test'])

#Filtrage du df sur années 2013 à 2019
df_2013_2019=df.loc[(df["Annee"]==2013) | (df["Annee"]==2014) | (df["Annee"]==2015) | (df["Annee"]==2016) |(df["Annee"]==2017) |(df["Annee"]==2018 |(df["Annee"]==2019))]

#les consommations par secteur d'activités par région entre 2013 et 2019
df_2013_2019.groupby(["Libellé Région"]).agg({'Consommation Agriculture (MWh)':"mean",
       'Consommation Industrie (MWh)':"mean", 'Consommation Tertiaire  (MWh)':"mean",
       'Consommation Résidentiel  (MWh)':"mean", 'Consommation Secteur Inconnu (MWh)':"mean",
       'Consommation totale (MWh)':"mean"}).round().astype(int)

#les consommations par secteur d'activités entre 2013 et 2019
df_2013_2019.agg({'Consommation Agriculture (MWh)':"mean",
       'Consommation Industrie (MWh)':"mean", 'Consommation Tertiaire  (MWh)':"mean",
       'Consommation Résidentiel  (MWh)':"mean", 'Consommation Secteur Inconnu (MWh)':"mean",
       'Consommation totale (MWh)':"mean"}).round().astype(int)

#Les consommations par secteur d'activités et la densité par région entre 2013 et 2019
df12=df_2013_2019.groupby(["Libellé Région"]).agg({'Consommation Agriculture (MWh)':"mean",
       'Consommation Industrie (MWh)':"mean", 'Consommation Tertiaire  (MWh)':"mean",
       'Consommation Résidentiel  (MWh)':"mean", "Densite (hab/km²)":"max"}).round().astype(int)

#TEST corrélation entre chaque consommation par secteur d'activités et la densité
df13=pd.DataFrame(data=df12, index=None, columns=['Consommation Agriculture (MWh)',
       'Consommation Industrie (MWh)', 'Consommation Tertiaire  (MWh)',
       'Consommation Résidentiel  (MWh)', "Densite (hab/km²)"], dtype=None, copy=None)
cor=df13.corr(method="pearson")

fig, ax = plt.subplots(figsize=(5,5))
sns.heatmap(cor, annot= True, ax= ax, cmap="coolwarm");

import statsmodels.api as sm
from statsmodels.formula.api import ols
df13["Agriculture"]=df13["Consommation Agriculture (MWh)"]
df13["Industrie"]=df13["Consommation Industrie (MWh)"]
df13["Tertiaire"]=df13["Consommation Tertiaire  (MWh)"]
df13["Résidentiel"]=df13["Consommation Résidentiel  (MWh)"]
df13["Densite"]=df13["Densite (hab/km²)"]

ols("Densite ~ Agriculture", data= df13).fit()

model = ols("Densite ~ Agriculture", data=df13).fit()
aov_table = sm.stats.anova_lm(model, typ=2)
aov_table

ols("Densite ~ Industrie", data= df13).fit()

model = ols("Densite ~ Industrie", data=df13).fit()
aov_table = sm.stats.anova_lm(model, typ=2)
aov_table

ols("Densite ~ Tertiaire", data= df13).fit()

model = ols("Densite ~ Tertiaire", data=df13).fit()
aov_table = sm.stats.anova_lm(model, typ=2)
aov_table

ols("Densite ~ Résidentiel", data= df13).fit()

model = ols("Densite ~ Résidentiel", data=df13).fit()
aov_table = sm.stats.anova_lm(model, typ=2)
aov_table

#Renommage des variables
df13["Agriculture"]=df13["Consommation Agriculture (MWh)"]
df13["Industrie"]=df13["Consommation Industrie (MWh)"]
df13["Tertiaire"]=df13["Consommation Tertiaire  (MWh)"]
df13["Résidentiel"]=df13["Consommation Résidentiel  (MWh)"]
df13["Densite"]=df13["Densite (hab/km²)"]

# Test pearson
from scipy.stats import pearsonr
pd.DataFrame(pearsonr(df13["Densite (hab/km²)"],df13["Consommation Agriculture (MWh)"]), index = ['pearson_coeff','p-value'], columns = ['resultat_test'])

# Test pearson
from scipy.stats import pearsonr
pd.DataFrame(pearsonr(df13["Densite (hab/km²)"],df13["Consommation Industrie (MWh)"]), index = ['pearson_coeff','p-value'], columns = ['resultat_test'])

# Test pearson
from scipy.stats import pearsonr
pd.DataFrame(pearsonr(df13["Densite (hab/km²)"],df13["Consommation Tertiaire  (MWh)"]), index = ['pearson_coeff','p-value'], columns = ['resultat_test'])

# Test pearson
from scipy.stats import pearsonr
pd.DataFrame(pearsonr(df13["Densite (hab/km²)"],df13["Consommation Résidentiel  (MWh)"]), index = ['pearson_coeff','p-value'], columns = ['resultat_test'])





