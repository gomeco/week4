#!/usr/bin/env python
# coding: utf-8

# In[14]:


get_ipython().system('kaggle datasets download -d ruchi798/data-science-job-salaries -f ds_salaries.csv')


# In[15]:


import streamlit as st
import pandas as pd
import numpy as np
import os


# In[16]:


df = pd.read_csv("ds_salaries.csv")


# In[17]:


print(df.describe())
print(df.info())


# In[18]:


st.title("salaries")


# In[19]:


InputYear = st.sidebar.selectbox("Select year", (2020, 2021, 2022))


# In[20]:


YearSelect = df[df["work_year"] == InputYear]


# In[21]:


st.dataframe(YearSelect)


# In[ ]:




