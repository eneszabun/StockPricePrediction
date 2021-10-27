from math import tanh
from os import altsep
import numpy as np
import pandas as pd
import pandas_datareader as web
import matplotlib.pyplot as plt
from sklearn import tree
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.utils import validation
plt.style.use('fivethirtyeight')

class Sterlin:
    def grafik3():
        data = web.DataReader('GBPUSD=X',data_source='yahoo',start='2015-01-01',end='2021-10-25')
        data.shape

        data = data[['Close']]
        data.tail()

        gelecek_gunler = 40
        data['Tahmin'] = data[['Close']].shift(-gelecek_gunler)
        data.tail()

        X = np.array(data.drop(['Tahmin'],1))[:-gelecek_gunler]
        Y = np.array(data['Tahmin'])[:-gelecek_gunler]

        x_train, x_test, y_train, y_test = train_test_split(X,Y,test_size=60)

        tree=DecisionTreeRegressor().fit(x_train,y_train)
        lr=LinearRegression().fit(x_train,y_train)

        x_gelecek = data.drop(['Tahmin'],1)[-gelecek_gunler:]
        x_gelecek = x_gelecek.tail(gelecek_gunler)
        x_gelecek = np.array(x_gelecek)

        tree_tahminleri = tree.predict(x_gelecek)
        lr_tahminleri = lr.predict(x_gelecek)

        tahminler = lr_tahminleri
        valid = data[X.shape[0]:]
        valid['Tahminler']=tahminler
        plt.title('GBP')
        plt.ylabel('USD')
        plt.xlabel('YEARS')
        plt.plot(data['Close'])
        plt.plot(valid[['Close','Tahminler']])
        plt.legend(['Orijinal','Değer','Tahmin'])
        plt.show()