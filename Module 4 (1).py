#!/usr/bin/env python
# coding: utf-8

# In[15]:


#Pandas program to get the details of the movie with title 'Grumpier Old Men'
import pandas as pd
movies_metadata = pd.read_csv('movies_metadata.csv', index_col =None)
m = movies_metadata
Grumpier_Old_Men = m[ m['title'] ==  'Grumpier Old Men']
Grumpier_Old_Men.head()


# In[18]:


# Pandas program to sort the DataFrame based on release_date
# The Framework only display the following columns: 'title', 'release_date', 'budget', 'revenue', 'runtime'
movies_metadata = pd.read_csv('movies_metadata.csv', usecols=['title', 'release_date', 'budget', 'revenue', 'runtime'])
m = movies_metadata
pm = m.sort_values(by='release_date')
pm.head(8)


# In[19]:


# This program get those movies whose revenue is more than 2 million and spent less than 1 million
# The framework only display the following columns: 'title', 'release_date', 'budget', 'revenue', 'runtime'
result = m[(m['revenue'] > 2000000 ) &  (m['budget'] < 1000000) ]
result.head()

