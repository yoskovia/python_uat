#!/usr/bin/env python
# coding: utf-8

# # Python Basics

# ### Topic Agenda
# - Getting Help
# - Operations
# - Lists
# - Functions

# In[ ]:


# Click this cell, and then click the "Run" button above to execute the code within
print('Hello world!')


# ## Getting Help

# - `help(str)` will print out the help page for an object
# - `type(variable)` will show the type of a `variable`
# - `dir(variable)` will show you the things you can do with `variable`

# In[ ]:


my_name = 'Anthony'
# What is the type of my_name?
type(my_name)


# In[ ]:


# What operations can I perform on my_name?
dir(my_name)


# In[ ]:


# upper looks interesting, I'd like to read more about it.
help(my_name.upper)


# In[ ]:


my_name.upper()


# In[ ]:


my_name


# In[ ]:


help(my_name.isupper)


# In[ ]:


my_name.isupper()


# In[ ]:


'32'.zfill(5)


# In[ ]:


foo = 1
foo.zfill(2)


# In[ ]:


str(foo).zfill(2)


# In[ ]:


int('01')


# ### Python is a case sensitive language, so the following will not work.

# In[ ]:


print(My_name)


# ## Operations - Python As A Calculator

# In[ ]:


print(15 + 100)

print(15 - 100)

print(15 * 100)

print(15 ** 2)

print(15 // 3)

print((15 / 15) ** 2)

print(15 % 2) # Mod


# ## Lists - Collecting similar variables

# In[ ]:


fruits = ['apples', 'oranges']


# In[ ]:


for fruit in fruits:
    print('I like ' + fruit)


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


# ## Applying a function to each element of a list

# In[ ]:


[name.upper() for name in ['anthony', 'mittens']]


# ## Functions

# In[ ]:


def add_two(a, b):
    return a + b

add_two(1, 3)


# In[ ]:


def add_two(a, b):
    """
    Add two numbers.
    
    a (int): First number
    b (int): Second number
    
    Example usage:
        add_two(1, 2)
        >>> 3
    """
    return a + b


# In[ ]:


add_two(1, 2)


# In[ ]:


print(add_two.__doc__)


# In[ ]:


help(add_two)

