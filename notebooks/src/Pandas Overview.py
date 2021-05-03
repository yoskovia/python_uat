#!/usr/bin/env python
# coding: utf-8

# # Manipulating Data with `pandas`

# - Dataframes and their attributes
# - Subsetting
# - Aggregating
# - Reading external files

# In[ ]:


import pandas as pd

pinball = pd.DataFrame({
    'name':['anthony', 'jim', 'tom', 'tom', 'tim'],
    'score':[100, 2, 3, 3, None]
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


dir(pd.Series)


# Online help [here](https://pandas.pydata.org/docs/reference/api/pandas.Series.describe.html).

# In[ ]:


help(pd.Series.describe)


# In[ ]:


get_ipython().run_line_magic('pinfo2', 'pd.Series.to_clipboard')


# In[ ]:


pinball.to_clipboard() # Helpful when pasting into excel


# In[ ]:


pinball.to_clipboard(excel=False) # Helpful for email / slack


# In[ ]:


pinball['score'].describe()


# In[ ]:


pinball.describe() # Show all descriptive statistics


# In[ ]:


get_ipython().run_line_magic('pinfo', 'pd.Series.duplicated')


# In[ ]:


pinball['score'].duplicated(keep=False)


# In[ ]:


pinball[ pinball['score'].duplicated(keep=False) ]


# In[ ]:


pinball[ pinball['score'].duplicated(keep=False) ]


# In[ ]:


dups = pinball[ pinball['score'].duplicated(keep=False) ]

assert len(dups) == 0, 'Stop!!! There are duplicate values!!'


# In[ ]:


pinball['score'].mean()


# In[ ]:


pinball['score'] > 50


# Pass a boolean array into the index in order to subset

# In[ ]:


bool_array = pinball['score'] > 50
pinball[bool_array]


# In[ ]:


pinball.loc[lambda x: x['score'] > 50]


# In[ ]:




