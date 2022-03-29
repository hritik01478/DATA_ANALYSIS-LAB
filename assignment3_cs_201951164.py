# -*- coding: utf-8 -*-
"""Assignment3_CS_201951164.ipynb
"""

!pip install joypy

import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.graphics.gofplots import qqplot
from joypy import joyplot #!pip install joypy

df = pd.read_csv("/content/drive/MyDrive/Classroom/CS IT312 Data Analytics and Visualization/Assignment 3/grains_production_india_from_2001_to_2017.csv")
df.head()

df.columns

df1 = df[['Year', 'Food Grains (Cereals) - Rice (000 tonnes)',
       'Food Grains (Cereals) - Jowar (000 tonnes)',
       'Food Grains (Cereals) - Bajra (000 tonnes)',
       'Food Grains (Cereals) - Maize (000 tonnes)',
       'Food Grains (Cereals) - Ragi (000 tonnes)',
       'Food Grains (Cereals) - Small Millets (000 tonnes)',
       'Food Grains (Cereals) - Wheat (000 tonnes)',
       'Food Grains (Cereals) - Barley (000 tonnes)']]
df1.rename(columns = {'Food Grains (Cereals) - Rice (000 tonnes)':'Rice',
                      'Food Grains (Cereals) - Jowar (000 tonnes)':'Jowar',
                      'Food Grains (Cereals) - Bajra (000 tonnes)': 'Bajra', 
                      'Food Grains (Cereals) - Maize (000 tonnes)' : 'Maize',
                      'Food Grains (Cereals) - Ragi (000 tonnes)': 'Ragi',
                      'Food Grains (Cereals) - Small Millets (000 tonnes)':'Small Millets',
                      'Food Grains (Cereals) - Wheat (000 tonnes)' : 'Wheat',
                      'Food Grains (Cereals) - Barley (000 tonnes)': 'Barley'}, inplace = True)
#df1

ax = plt.subplots(figsize=(15,6))
sns.boxplot(data=df1)

df2 = df[['Food Grains (Pulses) - Gram (000 tonnes)',
       'Food Grains (Pulses) - Tur (000 tonnes)',
       'Food Grains (Pulses) - Other Pulses (000 tonnes)']]
df2.rename(columns = {'Food Grains (Pulses) - Gram (000 tonnes)':'Gram',
       'Food Grains (Pulses) - Tur (000 tonnes)':'Tur',
       'Food Grains (Pulses) - Other Pulses (000 tonnes)':'Other Pulses'}, inplace = True)
#df2

sns.violinplot(data=df2)

df3 = df[['Oilseeds - Ground-nuts (000 tonnes)',
       'Oilseeds - Sesamum (000 tonnes)',
       'Oilseeds - Rapeseed and Mustard (000 tonnes)',
       'Oilseeds - Linseed (000 tonnes)',
       'Oilseeds - Castor seed (000 tonnes)']]
df3.rename(columns = {'Oilseeds - Ground-nuts (000 tonnes)':'Ground-nuts',
       'Oilseeds - Sesamum (000 tonnes)':'Sesanum',
       'Oilseeds - Rapeseed and Mustard (000 tonnes)':'Rapeseed and Mustard',
       'Oilseeds - Linseed (000 tonnes)':':Linseed',
       'Oilseeds - Castor seed (000 tonnes)':'Castor Seed'}, inplace = True)
#df3

ax = plt.subplots(figsize=(15,6))
sns.stripplot(data=df3)