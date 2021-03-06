#!/usr/bin/env python
# coding: utf-8

# # Practical Examples

# ### Formatting Column Names: Turning `AMERICAN_INDIAN_ENROLLMENT` into `American Indian`

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


# Apply the above processing to each row of the dataset with `apply`.

# In[ ]:


df['my_name'].apply(lambda x: x.replace('_', ' ').title().replace(' Enrollment', ''))


# Most of them look good, except for the "Two Or More Races" category doesn't need the 'O' capitalized. I'll create a function that uses an if statement to deal with this.

# In[ ]:


def clean_name(name):
    """ Clean up race names. 
    
    >>> clean_name('HAWAIIAN_ENROLLMENT')
    Hawaiian
    """
    if name == 'TWO_OR_MORE_RACES_ENROLLMENT':
        return 'Two or More Races'
    
    return (
        name.replace('_', ' ').title().replace(' Enrollment', '')
    )


# In[ ]:


help(clean_name)


# In[ ]:


df['my_name'].apply(clean_name)


# In[ ]:


df.assign(cleaned = lambda x: x['my_name'].apply(clean_name))


# <br>
# <br>
# <br>
# <br>
# <br>

# ### Multiple String Or: Find records where the `animals` column contains _any_ of the strings in `wanted_animals`

# In[ ]:


wanted_animals = ['cats', 'dogs']

df = pd.DataFrame({
    'name':['bob', 'jim', 'steve'],
    'animals':['cats, dogs, turtles', 'dogs', 'turtles']
});
display(df)


# In[ ]:


print(f'Finding: {wanted_animals}')
print('Output Frame')
(
    df.loc[lambda x: x['animals'].apply(lambda x: 
        any([name in x for name in wanted_animals])
    )]
)


# In[ ]:


# Are any of these values true?
any([False, True])


# In[ ]:


any([False, False])


# In[ ]:


# Are all values true?
all([True, True])


# In[ ]:


all([False, True])


# <br>
# <br>
# <br>
# <br>
# <br>

# ### Table Styling

# In[ ]:


import seaborn as sns
# sns.get_dataset_names()
gammas = sns.load_dataset('gammas').head(20)
display(gammas.head())
# Styler 
gammas.head().style.set_properties(**{
                            'background-color': 'green',
                            'color': 'white'
})


# In[ ]:


(
    gammas
    .sort_values(by='BOLD signal')
    .style.bar(subset='BOLD signal', align='mid', color=['green', 'red'])
)


# In[ ]:


def highlight_max(s):
    """
    Highlight the maximum in a Series green.
    
    s (pd.Series): Input series
    """
    is_max = s == s.max()
    return ['background-color: green' if v else '' for v in is_max]


def highlight_min(s):
    """
    Highlight the minimum in a Series red.
    
    s (pd.Series): Input series
    """
    is_min = s == s.min()
    return ['background-color: red' if v else '' for v in is_min]


(
    gammas.style
    .apply(highlight_max, subset=['subject', 'BOLD signal'])
    .apply(highlight_min, subset=['subject', 'BOLD signal'])
)


# In[ ]:


disp_tab = gammas.style.set_caption('Here is some text that describes the table.')


# <br>
# <br>
# <br>
# <br>
# <br>

# ## SQL -> pd.DataFrame

# In[ ]:


# See local notebook


# <br>
# <br>
# <br>
# <br>
# <br>

# ## Generating Fake Data

# In[ ]:


from faker import Faker
import numpy as np

fake = Faker()

[Faker().name() for _ in np.arange(5)]


# In[ ]:


[op for op in dir(fake) if not op.startswith('_')]


# In[ ]:


[Faker().email() for _ in np.arange(5)]


# In[ ]:


[Faker().ipv4() for _ in np.arange(5)]


# In[ ]:


[Faker().street_address() for _ in np.arange(5)]


# In[ ]:


[Faker().sentence() for _ in np.arange(5)]


# In[ ]:


[Faker().job() for _ in np.arange(5)]


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




