#!/usr/bin/env python
# coding: utf-8

# In[18]:


#pip install streamlit


# In[19]:


import streamlit as st
import pandas as pd
import numpy as np


# In[ ]:





# In[20]:


df = pd.read_csv("ds_salaries.csv")


# In[21]:


print(df.describe())
print(df.info())


# In[22]:


st.title("salaries")


# In[26]:


InputYear = st.sidebar.selectbox("Select year", (2020, 2021, 2022))


# In[27]:


YearSelect = df[df["work_year"] == InputYear]


# In[28]:


st.dataframe(YearSelect)


# In[ ]:





# In[ ]:





# In[ ]:




