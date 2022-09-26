#!/usr/bin/env python
# coding: utf-8

# In[47]:


#!kaggle datasets download -d ruchi798/data-science-job-salaries


# In[48]:


import streamlit as st
import pandas as pd
import numpy as np
import os


# In[49]:


df = pd.read_csv("ds_salaries.csv")


# In[50]:


print(df.describe())
print(df.info())


# In[51]:


st.title("salaries")


# In[52]:


InputYear = st.sidebar.selectbox("Select year", (2020, 2021, 2022))


# In[53]:


YearSelect = df[df["work_year"] == InputYear]


# In[54]:


st.dataframe(YearSelect)


# In[55]:


st.write(YearSelect)

