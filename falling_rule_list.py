#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np


# In[ ]:


mammo_data = pd.read_csv('uci_mammo_data.csv')
mammo_data.describe()


# In[ ]:


mammo_data.head()


# In[ ]:


mammo_data['RoundShape'].value_counts()


# In[ ]:


crosstab = pd.crosstab(mammo_data['RoundShape'], [mammo_data['OvalShape'],mammo_data['LobularShape'], mammo_data['IrregularShape']], margins=True)
crosstab


# In[ ]:


crosstab2 = pd.crosstab(mammo_data['OvalShape'],[mammo_data['RoundShape'],mammo_data['LobularShape'], mammo_data['IrregularShape']], margins=True)
crosstab2


# In[ ]:


crosstab3 = pd.crosstab(mammo_data['LobularShape'],[mammo_data['RoundShape'],mammo_data['OvalShape'], mammo_data['IrregularShape']], margins=True)
crosstab3


# In[ ]:


crosstab4 = pd.crosstab(mammo_data['IrregularShape'],[mammo_data['RoundShape'],mammo_data['OvalShape'], mammo_data['LobularShape']], margins=True)
crosstab4


# In[ ]:


mammo_data.head()


# In[ ]:


type(mammo_data.columns)


# In[ ]:


mammo_data_list = mammo_data.columns
for boob in mammo_data_list[4:9]:
    print(boob)


# In[ ]:


circ = mammo_data['CircumscribedMargin']
micro = mammo_data['MicrolobulatedMargin']
obscur = mammo_data['ObscuredMargin']
ill = mammo_data['IllDefinedMargin']
spic = mammo_data['SpiculatedMargin']

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


mammo_data.iloc[:,0:4].apply()


# In[ ]:


conditions = [
    (mammo_data['RoundShape']==1),
    (mammo_data['OvalShape']==1),
    (mammo_data['LobularShape']==1),
    (mammo_data['IrregularShape']==1)
]
choices = ['round', 'oval','lobular','irregular']
mammo_data['shape'] = np.select(conditions, choices)
mammo_data.head()


# In[ ]:


mammo_data['shape'].value_counts()


# In[ ]:




