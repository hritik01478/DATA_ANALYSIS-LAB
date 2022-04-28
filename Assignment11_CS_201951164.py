#!/usr/bin/env python
# coding: utf-8
# LAB ASSIGNMENT 11
# Urmila Rathore
# 201951164 [CSE]


# In[ ]:





# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
import random
import seaborn as sns
import numpy as np


# In[3]:


data = pd.read_csv('C:/Users/Hp/Desktop/SHAPEAI/DATA_ANALYSIS-LAB/cookie_cats.csv')
data.head()


# In[4]:


ax = data.boxplot(by='version', column='sum_gamerounds')
ax.set_xlabel('')
ax.set_ylabel('sum_grounds')
plt.suptitle('')


# In[5]:


mean_gate30=data[data['version']=='gate_30'].sum_gamerounds.mean()
mean_gate40=data[data['version']=='gate_40'].sum_gamerounds.mean()

print(mean_gate30)
print(mean_gate40)


# In[6]:


diff=mean_gate30-mean_gate40
diff


# In[7]:


ngate_30=(data[data['version']=='gate_30']).shape[0]
ngate_40=(data[data['version']=='gate_40']).shape[0]


# In[8]:


print(ngate_30)
print(ngate_40)


# In[9]:


def perm_fun(x, nA, nB):
    n = nA + nB
    idx_B = set(random.sample(range(n), nB))
    idx_A = set(range(n)) - idx_B
    return x.loc[idx_B].mean() - x.loc[idx_A].mean()

perm_diffs = [perm_fun(data.sum_gamerounds, ngate_30, ngate_40) for _ in range(1000)]


# In[10]:


fig, ax = plt.subplots(figsize=(5, 5))
ax.hist(perm_diffs, bins=11, rwidth=0.9)

ax.axvline(x = mean_gate30 - mean_gate40, color='black', lw=2)

ax.text(0.5, 180, 'Observed\ndifference',bbox={'facecolor':'white'})

ax.set_xlabel('Difference of sum_gamerounds')
ax.set_ylabel('Frequency')


# In[11]:


a=[]
for i in range(len(perm_diffs)):
    if(perm_diffs[i] >mean_gate30 - mean_gate40):
      a.append(perm_diffs[i])


np.mean(a)

