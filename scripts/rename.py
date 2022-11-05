#!/usr/bin/env python
# coding: utf-8

# In[17]:


import os
path = "/Users/jayamhy/Documents/ML_Project/VDISC_C_code/new_data_train/vulnerable_renamed/"
dir_list = os.listdir(path)
for file in dir_list:   
   os.rename(os.path.join(path, file), os.path.join(path, 'cve_cwe_' + file))
   #print(file)
   


# In[18]:


import os
path = "/Users/jayamhy/Documents/ML_Project/VDISC_C_code/new_data_train/vulnerable_renamed/"
dir_list = os.listdir(path)
print(dir_list)


# In[ ]:





# In[ ]:




