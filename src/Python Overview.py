#!/usr/bin/env python
# coding: utf-8

# # Python Basics

# ### Topic Agenda
# - Getting Help
# - Operations
# - Lists
# - Loops
# - Dictionaries
# - Conditional Logic
# - Functions

# In[ ]:


# Click this cell, and then click the "Run" button above to execute the code within
print('Hello world!')


# ## Getting Help

# Sample situation: I'd like to capitalize all the letters in a variable.
# 
# - `help(str)` will print out the help page for an object
# - `type(variable)` will show the type of a `variable`
# - `dir(variable)` will show you the things you can do with `variable`

# In[ ]:


my_name = 'Anthony'
type(my_name)


# In[ ]:


# What operations can I perform on my_name?
dir(my_name)


# In[ ]:


# upper looks like what I want to do, I'd like to read more about it.
help(str.upper)


# In[ ]:


my_name.upper()


# In[ ]:


my_name


# In[ ]:


get_ipython().run_line_magic('pinfo', 'str.isupper')


# In[ ]:


help(str.isupper)


# In[ ]:


my_name.isupper()


# In[ ]:


'32'.zfill(4)


# ### Python is a case sensitive language, so the following will not work.

# In[ ]:


print(My_name)


# Can also make numbers

# In[ ]:


my_number = 57
my_number


# In[ ]:


type(my_number) # int = integer


# ## Operations - Python As A Calculator

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


# ## Lists - Collecting similar variables

# In[ ]:


fruits = ['apples', 'oranges']


# Lists can contain different types

# In[ ]:


another_list = ['name', 500]


# In[ ]:


another_list


# In[ ]:


fruits[0]


# In[ ]:


fruits[1]


# In[ ]:


len(fruits)


# ## Loops - Doing something multiple times

# In[ ]:


for name in ['anthony', 'mittens']:
    print(name.upper())


# In[ ]:


all_names = ['foo', 'bar']
for name in all_names:
    # name could be anything, but 'all_names' must be a variable
    print(name)


# ## What if I want to apply a function / method to each element of a list?

# In[ ]:


# Intermediate topic: List comprehensions
[name.upper() for name in ['anthony', 'mittens']]


# ## Dictionaries - Collecting similar variables with names

# In[ ]:


my_dict = {'name':'anthony', 'favorite food':'gorditas'}
my_dict


# In[ ]:


my_dict['name']


# In[ ]:


my_dict['favorite food']


# ### Structures can be nested

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


# ## Conditional Logic: Making decisions

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


# ## Functions
