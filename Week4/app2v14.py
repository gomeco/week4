#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import pandas as pd
import numpy as np


# In[2]:


#!kaggle datasets download -d ruchi798/data-science-job-salaries -f ds_salaries.csv


# In[3]:


url = 'https://raw.githubusercontent.com/gomeco/week4/main/Week4/ds_salaries.csv?token=GHSAT0AAAAAABZHO5T2YXZ4SPATO4N4SW22YZSYYYQ'
df = pd.read_csv(url)


# In[4]:


#df = pd.read_csv("ds_salaries.csv")


# In[5]:


print(df.describe())
print(df.info())


# In[6]:


st.title("salaries")


# In[7]:


InputYear = st.sidebar.selectbox("Select year", (2020, 2021, 2022))


# In[8]:


YearSelect = df[df["work_year"] == InputYear]


# In[9]:


st.dataframe(YearSelect)


# In[ ]:




