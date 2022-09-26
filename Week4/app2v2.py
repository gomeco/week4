#!/usr/bin/env python
# coding: utf-8

# In[24]:


get_ipython().system('kaggle datasets list -s ds_salaries.csv')


# In[26]:


get_ipython().system('kaggle datasets download -d ruchi798/data-science-job-salaries')


# In[27]:


import streamlit as st
import pandas as pd
import numpy as np


# In[28]:


df = pd.read_csv("ds_salaries.csv")


# In[29]:


print(df.describe())
print(df.info())


# In[30]:


st.title("salaries")


# In[31]:


InputYear = st.sidebar.selectbox("Select year", (2020, 2021, 2022))


# In[32]:


YearSelect = df[df["work_year"] == InputYear]


# In[33]:


st.dataframe(YearSelect)

