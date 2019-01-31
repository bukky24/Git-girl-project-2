#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
movies_metadata = pd.read_csv('movies_metadata.csv', index_col =None)
m = movies_metadata
Grumpier_Old_Men = m[ m['title'] ==  'Grumpier Old Men']
Grumpier_Old_Men.head()


# In[13]:


import pandas as pd
movies_metadata = pd.read_csv('movies_metadata.csv', usecols=['title', 'release_date', 'budget', 'revenue', 'runtime'])
m = movies_metadata
pm = m.sort_values(by='release_date')
pm.head(8)


# In[5]:


result = m[(m['revenue'] > 2000000 ) &  (m['budget'] < 1000000) ]
result.head()


# In[ ]:




