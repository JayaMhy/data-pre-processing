#!/usr/bin/env python
# coding: utf-8

# In[145]:


import h5py


# In[146]:


import pandas as pd


# In[147]:


test_file = 'test.hdf5'


# In[148]:


data = h5py.File(test_file,'r')


# In[149]:


df = pd.DataFrame()


# In[150]:


for key in data.keys():
    df[key] = data[key]


# In[151]:


df["CWE-any"]  = df["CWE-120"] | df["CWE-469"] | df["CWE-476"] | df["CWE-other"] | df["CWE-119"]


# In[152]:


df.head()


# In[153]:


import os
for index, row in df.iterrows():
    file_name = f"source_{index}.c"
    is_vulnerable = row["CWE-any"]
    if is_vulnerable:
        folder_name = "new_data_test/vulnerable"
    else:
        folder_name = "new_data_test/all_false"
    file_path = os.path.join(folder_name, file_name)
    with open(file_path, 'wb') as f:
        f.write(row["functionSource"])
    
    


# In[ ]:




