#URMILA RATHORE
#201951164 (CSE)



#!/usr/bin/env python
# coding: utf-8

# In[18]:


import pandas as pd
import numpy as np
from random import sample
import matplotlib.pyplot as plt
import math


# In[3]:


df=pd.read_csv('weight-height - weight-height (1).csv')


# In[4]:


df


# ##### Central Limit Theorem statest that the sample distribution turns into normal when more and more sampling is done

# In[15]:


num = [1, 10, 50, 100]
means = []

for j in num:
    np.random.seed(1)
    x = [np.mean(
        sample(list(df["Height"]),j)) for _i in range(1000)]
    means.append(x)
k = 0
fig, ax = plt.subplots(2, 2, figsize =(8, 8))
for i in range(0, 2):
    for j in range(0, 2):
        ax[i, j].hist(means[k], 10, density = True)
        ax[i, j].set_title(label = num[k])
        k = k + 1
plt.show()


# ##### From the above graphs it is clearly visible that the distribution is turning normal as the number of samples are increased from 1 to 100

# ##### Bootstrap performed on "Height"

# In[16]:


data=df["Height"].to_numpy()
number_of_samples=10000 # R times
size_of_sample=300  # n
sample_mean=[]
for i in range(number_of_samples):
    # Calulate mean for n samples
    sample_mean.append(np.mean(np.random.choice(data,size_of_sample,replace=True)))


# In[19]:


_=plt.hist(sample_mean,bins=100)
standard_error=np.std(sample_mean)/math.sqrt(len(sample_mean))
standard_error


# ##### 95% Confidence interval after perfroming bootstrap

# In[20]:


CI=0.95
sorted_means=np.sort(sample_mean)
l=len(sorted_means)
idx=math.floor(l*((1-CI)/2))

print("Lower Confidence level :", sorted_means[idx])
print("Upper Confidence level :", sorted_means[l-idx-1])


# In[ ]:




