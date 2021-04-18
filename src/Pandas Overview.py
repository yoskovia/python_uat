#!/usr/bin/env python
# coding: utf-8

# # Manipulating Data with `pandas`

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


pinball['score'] > 50


# In[ ]:


pinball[pinball['score'] > 50]


# In[ ]:


pinball.loc[lambda x: x['score'] > 50]

