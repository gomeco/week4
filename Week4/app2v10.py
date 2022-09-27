#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import pandas as pd
import numpy as np
import IPython


# In[2]:


get_ipython().system('kaggle datasets download -d ruchi798/data-science-job-salaries -f ds_salaries.csv')


# In[3]:


df = pd.read_csv("ds_salaries.csv")


# In[4]:


print(df.describe())
print(df.info())


# In[5]:


st.title("salaries")


# In[6]:


InputYear = st.sidebar.selectbox("Select year", (2020, 2021, 2022))


# In[7]:


YearSelect = df[df["work_year"] == InputYear]


# In[8]:


st.dataframe(YearSelect)


# In[ ]:




