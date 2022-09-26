#!/usr/bin/env python
# coding: utf-8

# In[29]:


pip install streamlit


# In[30]:


import streamlit as st
import pandas as pd
import numpy as np


# In[ ]:





# In[31]:


df = pd.read_csv("ds_salaries.csv")


# In[32]:


print(df.describe())
print(df.info())


# In[33]:


st.title("salaries")


# In[34]:


InputYear = st.sidebar.selectbox("Select year", (2020, 2021, 2022))


# In[35]:


YearSelect = df[df["work_year"] == InputYear]


# In[36]:


st.dataframe(YearSelect)


# In[ ]:





# In[ ]:





# In[ ]:




