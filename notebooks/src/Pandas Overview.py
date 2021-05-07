#!/usr/bin/env python
# coding: utf-8

# # Manipulating Data with `pandas`

# In[ ]:


import pandas as pd

pinball = pd.DataFrame({
    'name':['anthony', 'jim', 'tom', 'tom', 'tim'],
    'score':[100, 2, 3, 3, None],
    'nTimes':[1, 15, 15, 16, 8]
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


[x for x in dir(pd.Series) if not x.startswith('_')]


# Online help [here](https://pandas.pydata.org/docs/reference/api/pandas.Series.describe.html).

# In[ ]:


help(pd.Series.describe)


# In[ ]:


help(pd.Series.to_clipboard)


# In[ ]:


pinball.to_clipboard() # Helpful when pasting into excel


# In[ ]:


pinball.to_clipboard(excel=False) # Helpful for email / slack


# In[ ]:


pinball['score'].describe()


# In[ ]:


pinball.describe() # Show all descriptive statistics


# In[ ]:


help(pd.Series.duplicated)


# In[ ]:


pinball['score'].duplicated(keep=False)


# In[ ]:


pinball[ pinball['score'].duplicated(keep=False) ]


# In[ ]:


dups = pinball[ pinball['score'].duplicated(keep=False) ]

# Throw error if there are any duplicate rows in "dups"
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


pinball


# In[ ]:


pinball.nlargest(2, 'score')


# In[ ]:


pinball.nsmallest(3, 'nTimes')


# In[ ]:


games = pd.DataFrame({
    'name':['anthony', 'tom'],
    'fav_color':['red', 'blue']
})


# In[ ]:


pd.merge(pinball, games, how='left', on='name')


# In[ ]:


pd.merge(pinball, games, how='inner', on='name')


# In[ ]:


pd.merge(pinball, games, how='left', on='name', indicator=True)


# In[ ]:


merged = pd.merge(pinball, games, how='left', on='name', indicator=True)

# Throw an error if there are records that are only in the left table
assert 'left_only' not in merged['_merge'].unique(), 'Not all records matched'


# In[ ]:


# Make sure that no rows have a name of steve (sorry steve)
assert 'steve' not in merged['name'].unique()


# In[ ]:


import seaborn as sns

# The seaborn package has lots of useful builtin datasets
# Use `sns.get_dataset_names()` to see a full list of them
iris = sns.load_dataset('iris')


# In[ ]:


# Compute the average sepal_length by species
(
    iris
    .groupby('species')
    ['sepal_length'].mean()
)


# In[ ]:


(
    iris
    .groupby('species')
    
    # Compute the sum, min, and max of a single column
    ['sepal_length'].agg(['sum', 'min', 'max'])
    
    # Compute the sum and min of multiple columns
    #[['sepal_length', 'sepal_width']].agg(['sum', 'min'])
    
    # Use different aggregates for different columns
    #.agg({'sepal_length' : ['sum', 'min'], 'petal_length' : ['max']})
    #.melt() # Easily reshape data into the long format using .melt()
)


# In[ ]:


(
    iris
    .groupby('species')
    
    # Show records with the the 2 largest sepal_lengths by species 
    .apply(pd.DataFrame.nlargest, 2, 'sepal_length')
)


# In[ ]:


from pandasql import sqldf

sqldf('select * from iris limit 5')


# In[ ]:


sqldf('SELECT SUM(sepal_length) FROM iris GROUP BY species')

