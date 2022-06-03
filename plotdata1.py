# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 20:58:21 2020

@author: rufus
"""
#https://www.kaggle.com/pmarcelino/comprehensive-data-exploration-with-python

#invite people for the Kaggle party
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy.stats import norm
from sklearn.preprocessing import StandardScaler
from scipy import stats
#import warnings
#warnings.filterwarnings('ignore')
#%matplotlib inline


df_train = pd.read_csv("C:\\Thomas\\40_SoftwareDaten\\Python\\10_RawData\\99_otherSampleData\\ImmoscoutCrawler\\Rohdaten\\20-01-19.csv", error_bad_lines=False,sep=';') 
df_train.columns
df_train['obj_purchasePrice'].describe()

#***********histogram sales price
sns.distplot(df_train['obj_purchasePrice']);


#********boxplot sales prices vs construction year
var = 'obj_yearConstructed'

df_train['obj_yearConstructed'] = [str(x).replace(',', '.') for x in df_train['obj_yearConstructed']]
df_train['obj_yearConstructed'] = df_train['obj_yearConstructed'].astype(float)

data = pd.concat([df_train['obj_purchasePrice'], df_train[var]], axis=1)
f, ax = plt.subplots(figsize=(16, 8))
fig = sns.boxplot(x=var, y="obj_purchasePrice", data=data)
fig.axis(xmin=40, xmax=120);
fig.axis(ymin=0, ymax=1500000);
plt.xticks(rotation=90);

#box plot overallqual/saleprice
var = 'obj_regio3'
data = pd.concat([df_train['obj_purchasePrice'], df_train[var]], axis=1)
f, ax = plt.subplots(figsize=(20, 6))
fig = sns.boxplot(x=var, y="obj_purchasePrice", data=data)
fig.axis(ymin=0, ymax=1200000);
plt.xticks(rotation=90);


#scatterplot
sns.set()
cols = ['obj_purchasePrice', 'obj_yearConstructed', 'obj_livingSpace', 'obj_lotArea','obj_noRooms']
sns.pairplot(df_train[cols], size = 2.5)
plt.show();