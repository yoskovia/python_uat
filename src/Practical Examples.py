#!/usr/bin/env python
# coding: utf-8

# ## Practical Examples of Python

# ### Formatting Column Names: `AMERICAN_INDIAN_ENROLLMENT` -> `American Indian`

# In[ ]:


import pandas as pd

dat = {'AMERICAN_INDIAN_ENROLLMENT': 'American Indian',
       'ASIAN_ENROLLMENT': 'Asian',
       'AFRICAN_AMERICAN_ENROLLMENT': 'African American',
       'HISPANIC_ENROLLMENT': 'Hispanic',
       'HAWAIIAN_ENROLLMENT': 'Hawaiian',
       'WHITE_ENROLLMENT': 'White',
       'TWO_OR_MORE_RACES_ENROLLMENT': 'Two or More Races'}

df = (
    pd.DataFrame.from_dict(dat, orient='index')
    .reset_index()
    .rename(columns={'index':'my_name', 0:'wanted_name'})
)
df


# In[ ]:


'AMERICAN_INDIAN_ENROLLMENT'.replace('_', ' ').title().replace(' Enrollment', '')


# Perform the above processing to each row of the dataset with `apply`.

# In[ ]:


df['my_name'].apply(lambda x: x.replace('_', ' ').title().replace(' Enrollment', ''))


# Most of them look good, except for the "Two Or More Races" category doesn't need the 'O' capitalized. I'll create a function that uses an if statement to deal with this.

# In[ ]:


def clean_name(name):
    """ Clean up race names. 
    
    Example:
        clean_name('HAWAIIAN_ENROLLMENT')
        >>> Hawaiian
    """
    if name == 'TWO_OR_MORE_RACES_ENROLLMENT':
        return 'Two or More Races'
    
    return (
        name.replace('_', ' ').title().replace(' Enrollment', '')
    )


# In[ ]:


df['my_name'].apply(clean_name)


# In[ ]:


help(clean_name)


# ### Multiple String Or: Find records where `animals` contains any of the strings in `wanted_animals`

# In[ ]:


wanted_animals = ['cats', 'dogs']

df = pd.DataFrame({
    'name':['bob', 'jim', 'steve'],
    'animals':['cats, dogs, turtles', 'dogs', 'turtles']
}); 

print('Input Frame')
display(df)
print(f'Finding: {wanted_animals}')

print('Output Frame')
(
    df.loc[lambda x: x['animals'].apply(lambda x: 
        any([name in x for name in wanted_animals])
    )]
)


# ### Table Styling - Read more [here](https://pandas.pydata.org/pandas-docs/stable/user_guide/style.html)

# In[ ]:


import seaborn as sns
# sns.get_dataset_names()
(
    sns.load_dataset('gammas')
    .head(20)
    .sort_values(by='BOLD signal')
    .style.bar(subset='BOLD signal', align='mid', color=['green', 'red'])
)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




