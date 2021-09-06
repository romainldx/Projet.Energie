#https://machinelearningmastery.com/time-series-forecasting-with-prophet-in-python/
from fbprophet import Prophet
from fbprophet.plot import plot_plotly
import numpy as np
import pandas as pd
import pandas as pdimport
import matplotlib.pyplot as plt
import plotly.offline as py
py.init_notebook_mode()

df=pd.read_csv('tous.csv')
df.head()

indexNames = df[ df['annee'] == 2021 ].index
# Delete these row indexes from dataFrame
df.drop(indexNames , inplace=True)

df.head()
df=df[df['Région']== 'Occitanie']
df.head()

df['Date_datetime'] = pd.to_datetime(df['Date_datetime'])

df.head()
df.info()

df=df[['Date_datetime','Consommation (MW)']]
df.head()

df = df.sort_values(by = 'Date_datetime')

plt.figure(figsize=(20,10))
plt.plot(df['Date_datetime'] , df['Consommation (MW)'])

df.set_index('Date_datetime', inplace = True)

rolling_mean = df.rolling(window = 365).mean()
rolling_std = df.rolling(window = 12).std()
plt.figure( figsize=(8,5))
plt.plot(df, color = 'blue', label = 'Origine')
plt.plot(rolling_mean, color = 'red', label = 'Moyenne mobile')
plt.plot(rolling_std, color = 'black', label = 'Ecart-type mobile')
plt.legend(loc = 'best')
plt.title('Moyenne et Ecart-type mobiles')
plt.show()

from statsmodels.tsa.stattools import adfuller

result = adfuller(df['Consommation (MW)'])

print('Statistiques ADF : {}'.format(result[0]))
print('p-value : {}'.format(result[1]))
print('Valeurs Critiques :')
for key, value in result[4].items():
    print('\t{}: {}'.format(key, value))

df.reset_index('Date_datetime', inplace=True)

print(df[df['Date_datetime']== '2020-02-01'])

df.columns = ['ds', 'y']

model = Prophet()
model.fit(df)

from pandas import DataFrame
from datetime import datetime

# define the period for which we want a prediction
future = list()
for i in range(1, 13):
    date = '2020-%01d-01' % i
    future.append([date])
future = DataFrame(future)
future.columns = ['ds']
future['ds']= pd.to_datetime(future['ds'])

# summarize the forecast
forecast = model.predict(future)
print(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].head())

model.plot(forecast)
plt.show()

df2 = pd.DataFrame({'ymanuelle': [2014559,1867936,1897048,1782988,1348716,1266016,1569453,1395306,1540000,1686389,1517011,2302956]})

forecast['yhat']

from sklearn.metrics import mean_absolute_error
# calculate MAE between expected and predicted values for 2020
y_true = df2['ymanuelle'].values
y_pred = forecast['yhat'].values
mae = mean_absolute_error(y_true, y_pred)
print('MAE: %.3f' % mae)

model.plot_components(forecast)

# define the period for which we want a prediction
future = list()
for i in range(1, 13):
    date = '2021-%01d-01' % i
    future.append([date])
future = DataFrame(future)
future.columns = ['ds']
future['ds']= pd.to_datetime(future['ds'])
# use the model to make a forecast
forecast = model.predict(future)
# summarize the forecast
print(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].head())
# plot forecast
model.plot(forecast)
plt.show()