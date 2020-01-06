#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np


# In[ ]:


boobs = pd.read_csv('uci_mammo_data.csv')
boobs.describe()


# In[ ]:


boobs.head()


# In[ ]:


boobs['RoundShape'].value_counts()


# In[ ]:


crosstab = pd.crosstab(boobs['RoundShape'], [boobs['OvalShape'],boobs['LobularShape'], boobs['IrregularShape']], margins=True)
crosstab


# In[ ]:


crosstab2 = pd.crosstab(boobs['OvalShape'],[boobs['RoundShape'],boobs['LobularShape'], boobs['IrregularShape']], margins=True)
crosstab2


# In[ ]:


crosstab3 = pd.crosstab(boobs['LobularShape'],[boobs['RoundShape'],boobs['OvalShape'], boobs['IrregularShape']], margins=True)
crosstab3


# In[ ]:


crosstab4 = pd.crosstab(boobs['IrregularShape'],[boobs['RoundShape'],boobs['OvalShape'], boobs['LobularShape']], margins=True)
crosstab4


# In[ ]:


boobs.head()


# In[ ]:


type(boobs.columns)


# In[ ]:


boobs_list = boobs.columns
for boob in boobs_list[4:9]:
    print(boob)


# In[ ]:


circ = boobs['CircumscribedMargin']
micro = boobs['MicrolobulatedMargin']
obscur = boobs['ObscuredMargin']
ill = boobs['IllDefinedMargin']
spic = boobs['SpiculatedMargin']

list1 = [circ, micro, obscur, ill, spic]
i = 0

for margin in list1:
    list2 = list(list1)
    del(list2[i])
    crosstab = pd.crosstab(margin, list2, margins=True).apply(lambda r: (r/r.sum())*100, axis = 1)
    i = i + 1
    print(crosstab)


# In[ ]:


for item in list1:
    print(item.name)


# In[ ]:


pd.crosstab(circ, [micro, obscur, ill, spic]).apply(lambda r: r/r.sum(), axis = 1)


# In[ ]:


boobs.iloc[:,0:4].apply()


# In[ ]:


conditions = [
    (boobs['RoundShape']==1),
    (boobs['OvalShape']==1),
    (boobs['LobularShape']==1),
    (boobs['IrregularShape']==1)
]
choices = ['round', 'oval','lobular','irregular']
boobs['shape'] = np.select(conditions, choices)
boobs.head()


# In[ ]:


boobs['shape'].value_counts()


# In[ ]:




