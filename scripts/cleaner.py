#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Program to remove comments

import glob
import re

filenames = glob.glob('./vulnerable_clean/*.c', 
                   recursive = True)
for filename in filenames:
    with open(filename, 'r') as f:
        source_code = f.read()
        
    cleaned_filename = re.sub(r'^./vulnerable_clean/', r'new_cleaned/', filename)

    with open(cleaned_filename, 'w') as f:
        clean_source_code = source_code
        #regex to remove all multi line c comments
        clean_source_code = re.sub(r'/\*.*?\*/', '', clean_source_code, flags=re.DOTALL)
        #regex to remove all single line c comments
        clean_source_code = re.sub(r'\/\/.*', '', clean_source_code)

        f.write(clean_source_code)

           


# In[1]:


import glob
import re

filenames = glob.glob('./vulnerable_clean/*.c', 
                   recursive = True)
print(filenames)


# In[ ]:




