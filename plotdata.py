# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 20:58:21 2020

@author: rufus
"""

import matplotlib.pyplot as plt
plt.style.use('classic')
#matplotlib inline
import numpy as np
import pandas as pd

dataFrame = pd.read_csv("C:\\Thomas\\40_SoftwareDaten\\Python\\10_RawData\\99_otherSampleData\\ImmoscoutCrawler\\Rohdaten\\20-01-19.csv", error_bad_lines=False,sep=';') 

source = ColumnDataSource(df)


plt.hist(dataFrame['obj_purchasePrice'], normed=True, alpha=0.5)