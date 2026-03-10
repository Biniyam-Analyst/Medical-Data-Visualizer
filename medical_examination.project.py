#!/usr/bin/env python
# coding: utf-8

# **Medical_Examination.project**

# In[1]:


#1. loading the file 
import pandas as pd 
import numpy as np
df=pd.read_csv('medical_examination.csv')
df.head()


# In[2]:


# knowing about the all information about data 
df.info()


# In[4]:


df.shape


# In[5]:


# task 2: add a overweighting column,BMI=weight/height^2
BMI=df['weight']/((df['height' ]/100)**2)
df['overweight'] = (BMI > 25).astype(int) # one means True(overweight) and zero means false(not overweight)


# In[6]:


df.head()


# In[8]:


# task 3: normalize chelostrola and gluc column data into zero and one
#1. normailize chelostrol column
df['cholesterol'] =np.where(df['cholesterol']==1,0,1)
# 2.normalize gluc column
df['gluc'] =np.where(df['gluc']==1,0,1)


# In[9]:


# to check whether it is normalized /not
df[['cholesterol','gluc']].head()


# In[ ]:


print(df['gluc'].value_counts())
df[['cholesterol', 'gluc']].head()


# **categorical plot data**

# In[13]:


# task 4: reshaping the data
#melting the data
df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

# 2. counting the data by grouping 
df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')
#


# In[19]:


df_cat.sample(10) # to see randomly data sample


# In[20]:


import seaborn as sns
import matplotlib.pyplot as plt

# to visualize the graph
g = sns.catplot(
    data=df_cat, 
    x='variable', 
    y='total', 
    hue='value', 
    col='cardio', 
    kind='bar'
)

# labeling the x and y axis
g.set_axis_labels("Variable", "Total")
plt.show()


# **Data Cleaning**

# In[21]:


# task 5: data cleaning process
import pandas as pd

# 1. Select only those with valid blood pressure (ap_lo <= ap_hi)
# 2. Select those whose height and weight are within the middle 95%
# 3. We use bitwise AND (&) to keep rows that satisfy ALL conditions

df_heat = df[
    (df['ap_lo'] <= df['ap_hi']) & 
    (df['height'] >= df['height'].quantile(0.025)) &
    (df['height'] <= df['height'].quantile(0.975)) &
    (df['weight'] >= df['weight'].quantile(0.025)) &
    (df['weight'] <= df['weight'].quantile(0.975))
]


# In[25]:


# 1. claculate the correlation matrix
corr = df_heat.corr()

# 2.  mask the upper triangle to show the lower
mask = np.triu(np.ones_like(corr, dtype=bool))

# 3. setting the size of the graph
fig, ax = plt.subplots(figsize=(12, 12))

# 4.ploting with Seaborn Heat Map 
sns.heatmap(corr, annot=True, fmt='.1f', mask=mask, square=True, center=0, linewidths=.5, cbar_kws={'shrink': .5})

plt.show()


# In[ ]:




