#!/usr/bin/env python
# coding: utf-8

# # Jupyter Notebook Overview

# This is a jupyter notebook. Within it, there are cells that either contain markdown syntax or Python code. This cell contains markdown, while the one underneath it contains code. To execute the Python code below you can either:
# - Click the cell, and click the "Run" button in the above menu
# - Click the cell, and push control+enter

# In[ ]:


print('Hello!')


# Variables that you assign in one cell are available to all other cells, but not to other notebooks (usually).

# In[ ]:


x = 10


# In[ ]:


x


# **Warning!** When using a Jupyter notebook, if the last line of a cell is simply the name of a variable, it will automatically display the value below the cell. When creating `.py` files, you will need to call `print(my_var)` in order to see the variable.

# --- 

# You can also start a cell with `!` and use the cell as a terminal (cmd or powershell, this notebook should be using cmd)

# In[ ]:


get_ipython().system('dir')


# You can also save the output of a terminal command into a python variable.

# In[ ]:


dir_output = get_ipython().getoutput('dir')


# In[ ]:


get_ipython().system('jupyter nbconvert *.ipynb --to python --output-dir=src/')


# You can also run javascript, R, SQL, and lots of other languages using this interface.

# In[ ]:


get_ipython().run_cell_magic('javascript', '', "document.title='Tab Updated!'")

