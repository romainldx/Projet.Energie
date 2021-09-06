import numpy as np
import pandas as pd
import pandas as pdimport

import matplotlib.pyplot as plt
import plotly.offline as py
from matplotlib import pyplot as plt

df=pd.read_csv('tous.csv')
indexNames = df[ df['annee'] == 2021 ].index
# Delete these row indexes from dataFrame
df.drop(indexNames , inplace=True)
df['Date_datetime'] = pd.to_datetime(df['Date_datetime'])
df=df[df['Région']== 'Occitanie']
df=df[['Date_datetime','Consommation (MW)']]
df = df.sort_values(by = 'Date_datetime')
df.head()

df.set_index('Date_datetime', inplace = True)

data_columns = ['Consommation (MW)' ]
dfmois = df[data_columns].resample('M').mean() #
dfmois.head()

dfmois.to_csv("data2.csv", index = True)

df = pd.read_csv('data2.csv', header=0, parse_dates=[0], index_col=0, squeeze=True)
df.head()

print(df.index)

plt.plot(df)

from statsmodels.tsa.seasonal import seasonal_decompose

res = seasonal_decompose(df)
res.plot()
plt.show()

res = seasonal_decompose(df, model = 'multiplicative')
res.plot()
plt.show()

dflog = np.log(df)
plt.plot(dflog)
plt.show()

# On applique la fonction seasonal_decompose à dflog

# Ici on utilise la transformée en log on est donc dans un modèle additif

mult = seasonal_decompose(dflog)

# On soustrait les coefficients saisonniers à la série dflog

cvs=dflog- mult.seasonal

# On passe à l'exponentielle pour retrouver la série originale

x_cvs=np.exp(cvs)


# On affiche la série

plt.plot(df, label='Série originale')

plt.plot(x_cvs, label='Série corrigée')

plt.title('Graphique de la série originale et la série corrigée')

plt.xlabel('Date')

plt.ylabel('Consommation (MW)')

plt.legend()

#On a une saisonnalité de période 12

df_ma = dflog.rolling(window = 12, center = True).mean()

#Affichage de la série

plt.plot(dflog, color = 'blue', label = 'Origine')
plt.plot(df_ma, color = 'red', label = 'Moyenne mobile')
plt.legend()
plt.title('Moyenne mobiles')
plt.show()

# Affecter à la variable la différence entre la série et sa moyenne mobile

dflog_without_ma = dflog - df_ma


# Affichage des 10 premières valeurs

dflog_without_ma.head(10)

# Suppression des valeurs manquantes

dflog_without_ma = dflog_without_ma.dropna()

# Affichage de la série

dflog_without_ma.head(10)

# Convertir en dataframe

df2=dflog_without_ma.to_frame()

# Ajout d'une colonne month

df2['month'] = (df2.index).month

df2.head(10)

# Moyenne par mois à l'aide du groupby

seasonnality = df2.groupby('month').mean()

# Centrage des coefficients

seasonnality = seasonnality - seasonnality.mean()

pd.plotting.autocorrelation_plot(dflog);

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20,7)) # Création de la figure et des axes
dflog_1 = dflog.diff().dropna() # Différenciation ordre 1
dflog_1.plot(ax = ax1) #Série temporelle différenciée
pd.plotting.autocorrelation_plot(dflog_1, ax = ax2);

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20,7)) #Création de la figure et des axes
dflog_2 = dflog_1.diff(periods = 12).dropna() #Différenciation d'ordre 12
dflog_2.plot(ax = ax1) #Série doublement différenciée
pd.plotting.autocorrelation_plot(dflog_2, ax = ax2);

import statsmodels.api as sm

from statsmodels.graphics.tsaplots import plot_pacf, plot_acf
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20,7))
plot_acf(dflog_2, lags = 36, ax=ax1)
plot_pacf(dflog_2, lags = 16, ax=ax2)
plt.show()

model=sm.tsa.SARIMAX(dflog,order=(1,1,1),seasonal_order=(0,1,1,12))
sarima=model.fit()
print(sarima.summary())

model=sm.tsa.SARIMAX(dflog,order=(1,1,1),seasonal_order=(1,1,1,12))
sarima=model.fit()
print(sarima.summary())

model = sm.tsa.SARIMAX(dflog,order=(0,1,1),seasonal_order=(1,1,0,12))
sarima=model.fit()
print(sarima.summary())

import datetime
pred = np.exp(sarima.predict(47, 59))#Prédiction et passage à l'exponentielle
plt.plot(df)
plt.plot(pred) #Visualisation
plt.axvline(x= datetime.date(2020,1,1), color='red'); # Ajout de la ligne verticale

prediction = sarima.get_forecast(steps =12).summary_frame()  #Prédiction avec intervalle de confiance
fig, ax = plt.subplots(figsize = (15,5))
plt.plot(df)
prediction = np.exp(prediction) #Passage à l'exponentielle
prediction['mean'].plot(ax = ax, style = 'k--') #Visualisation de la moyenne
ax.fill_between(prediction.index, prediction['mean_ci_lower'], prediction['mean_ci_upper'], color='k', alpha=0.1); #Visualisation de l'intervalle de confiance

from sklearn.metrics import mean_absolute_error
# calculate MAE between expected and predicted values for 2020
y_true = df[-13:].values
y_pred = pred.values
mae = mean_absolute_error(y_true, y_pred)
print('MAE: %.3f' % mae)

model = sm.tsa.SARIMAX(dflog,order=(1,1,1),seasonal_order=(1,1,0,12))
sarima=model.fit()
print(sarima.summary())

import datetime
pred = np.exp(sarima.predict(47, 59))#Prédiction et passage à l'exponentielle
plt.plot(df)
plt.plot(pred) #Visualisation
plt.axvline(x= datetime.date(2020,1,1), color='red'); # Ajout de la ligne verticale

from sklearn.metrics import mean_absolute_error
# calculate MAE between expected and predicted values for 2020
y_true = df[-13:].values
y_pred = pred.values
mae = mean_absolute_error(y_true, y_pred)
print('MAE: %.3f' % mae)





