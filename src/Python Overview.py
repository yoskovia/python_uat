#!/usr/bin/env python
# coding: utf-8

# # Python Basics

# In[ ]:


# Click this cell, and then click the "Run" button above to execute the code within
print('Hello world!')


# ### In Python you create variables using the `=` sign. 

# In[ ]:


my_name = 'Anthony'
my_name


# ### Use the `type` function to determine the type of a variable
# - `my_name` is a variable of type `str` (String)

# In[ ]:


type(my_name)


# In[ ]:


str.count


# In[ ]:


help(str.count)


# In[ ]:


dir(str) # to see all available methods


# In[ ]:


help(str.upper)


# In[ ]:


my_name.upper()


# In[ ]:


my_name


# In[ ]:


get_ipython().run_line_magic('pinfo', 'str.isupper')


# In[ ]:


my_name.isupper()


# In[ ]:


'32'.zfill(4)


# In[ ]:


get_ipython().run_line_magic('pinfo', 'str')


# ### Python is a case sensitive language, so the following will not work.

# In[ ]:


print(My_name)


# Can also make numbers

# In[ ]:


my_number = 57
my_number


# In[ ]:


type(my_number) # int = integer


# ## Operations

# In[ ]:


my_number + 100


# In[ ]:


my_number - 100


# In[ ]:


my_number * 100


# In[ ]:


my_number ** 2


# In[ ]:


my_number // 3


# In[ ]:


(my_number / 15) ** 2


# In[ ]:


my_number % 2 # Mod


# ## Lists

# In[ ]:


my_list = ['apples', 'oranges']


# Lists can contain different types

# In[ ]:


another_list = ['name', 500]


# In[ ]:


my_list[0]


# In[ ]:


my_list[1]


# In[ ]:


len(my_list)


# In[ ]:


for name in ['anthony', 'mittens']:
    print(name.upper())


# In[ ]:


# Intermediate topic: List comprehensions
[name.upper() for name in ['anthony', 'mittens']]


# ## Loops

# In[ ]:


all_names = ['foo', 'bar']
for name in all_names:
    # name could be anything, but 'all_names' must be a variable
    print(name)


# ## Dictionaries

# In[ ]:


my_dict = {'name':'anthony', 'favorite food':'gorditas'}


# In[ ]:


my_dict['name']


# In[ ]:


my_dict['favorite food']


# Structures can be nested

# In[ ]:


nested = {
    'names':['anthony', 'mittens'],
    'cars':['honda', 'ford'],
    'title':'Here is a sentence.'
}


# In[ ]:


nested['names']


# In[ ]:


nested['cars']


# In[ ]:


nested['title']


# ### Making decisions

# In[ ]:


10 > 5


# In[ ]:


5 < 1


# In[ ]:


1 = 2


# Use `==` to check equality

# In[ ]:


1 == 2


# In[ ]:


age = 10
if age > 50:
    # Use \ to escape quotes
    print('You\'re over 50!')
else:
    print("You're less than 50")


# In[ ]:


if age == 10 or age == 20 or age == 30:
    print('Nice, your age is either 10 or 20 or 30')
else:
    print('Your age isnt in the list')


# In[ ]:


if age in [10, 20, 30]:
    print('Nice, your age is either 10 or 20')
else:
    print('Your age isnt in the list')

