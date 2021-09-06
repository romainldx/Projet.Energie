#https://www.kaggle.com/limyunjie1999/time-series-forecasting-on-energy-consumption-data

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df=pd.read_csv('tous.csv')
df.head()

indexNames = df[ df['annee'] == 2021 ].index
# Delete these row indexes from dataFrame
df.drop(indexNames , inplace=True)

df=df[df['Région'] == 'Occitanie']
df.head()

df.info()

df['Date_datetime'] = pd.to_datetime(df['Date_datetime'])
df=df[['Date_datetime','Consommation (MW)' ]]
df.set_index('Date_datetime', inplace = True)

split_date = '2020-01-01'
df_train = df.loc[df.index <= split_date].copy()
df_test = df.loc[df.index > split_date].copy()

_ = df_test \
    .rename(columns={'Consommation (MW)': 'TEST SET'}) \
    .join(df_train.rename(columns={'Consommation (MW)': 'TRAINING SET'}), how='outer') \
    .plot(figsize=(15,5), title='Consommation (MW)', style='.')


def create_features(df, label=None):
    """
    Creates time series features from datetime index
    """
    df['date'] = df.index

    df['dayofweek'] = df['date'].dt.dayofweek

    df['month'] = df['date'].dt.month
    df['year'] = df['date'].dt.year
    df['dayofyear'] = df['date'].dt.dayofyear
    df['dayofmonth'] = df['date'].dt.day
    df['weekofyear'] = df['date'].dt.weekofyear

    X = df[['dayofweek', 'month', 'year',
            'dayofyear', 'dayofmonth', 'weekofyear']]
    if label:
        y = df[label]
        return X, y
    return X

X_train, y_train = create_features(df_train, label='Consommation (MW)')
X_test, y_test = create_features(df_test, label='Consommation (MW)')

pip install xgboost
import xgboost as xgb
from xgboost import plot_importance, plot_tree
import sklearn.preprocessing
from sklearn.metrics import mean_squared_error, mean_absolute_error

reg = xgb.XGBRegressor(n_estimators=1000)
reg.fit(X_train, y_train,
        eval_set=[(X_train, y_train), (X_test, y_test)],
        early_stopping_rounds=50,
       verbose=False) # Change verbose to True if you want to see it train

output = reg.predict(X_test)

reg = xgb.XGBRegressor(n_estimators=1000)
reg.fit(X_train, y_train,
        eval_set=[(X_train, y_train), (X_test, y_test)],
        early_stopping_rounds=50,
       verbose=False) # Change verbose to True if you want to see it train

output = reg.predict(X_test)

#Predicted output will be in new colomn called MW Prediction
df_test['MW_Prediction'] =reg.predict(X_test)

PJM_all = pd.concat([df_test, df_train], sort=False)

_ = PJM_all[['Consommation (MW)','MW_Prediction']].plot(figsize=(15, 5))

from sklearn.metrics import r2_score

lstm_score = r2_score(y_test, output)
print("R^2 Score of XGBoost model = ",lstm_score)

mean_squared_error = mean_squared_error(y_true=df_test['Consommation (MW)'],
                   y_pred=df_test['MW_Prediction'])
print("Mean_squared_error =", mean_squared_error)

mean_absolute_error = mean_absolute_error(y_true=df_test['Consommation (MW)'],
                   y_pred=df_test['MW_Prediction'])
print("Mean_absolute_error =", mean_absolute_error)

def mean_absolute_percentage_error(y_true, y_pred):
    """Calculates MAPE given y_true and y_pred"""
    y_true, y_pred = np.array(y_true), np.array(y_pred)
    return np.mean(np.abs((y_true - y_pred) / y_true)) * 100

mean_absolute_percentage_error = mean_absolute_percentage_error(y_true=df_test['Consommation (MW)'],
                   y_pred=df_test['MW_Prediction'])

print("Mean_absolute_error = " + str(mean_absolute_percentage_error) + " %")









