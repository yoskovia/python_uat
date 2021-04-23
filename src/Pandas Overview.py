#!/usr/bin/env python
# coding: utf-8

# # Manipulating Data with `pandas`

# ### Topic Agenda 
# 
# - Dataframes and their attributes
# - Subsetting
# - Aggregating
# - Reading external files

# In[ ]:


import pandas as pd

pinball = pd.DataFrame({
    'name':['anthony', 'jim', 'tom'],
    'score':[100, 2, 3]
})


# In[ ]:


pinball


# In[ ]:


pinball.shape


# In[ ]:


pinball.dtypes


# In[ ]:


pinball.columns


# In[ ]:


pinball.rename(columns={'name':'persons name'})


# In[ ]:


pinball


# Select a single column using []

# In[ ]:


pinball['score']


# In[ ]:


pinball['score'] > 50


# Pass a boolean array into the index in order to subset

# In[ ]:


bool_array = pinball['score'] > 50
pinball[bool_array]


# In[ ]:


pinball.loc[lambda x: x['score'] > 50]


# ## Reading External Files

# ## Connecting to DW
