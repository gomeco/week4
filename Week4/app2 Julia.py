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
data = pd.read_csv(url)


# In[4]:


st.title("Salaris Database")


# In[5]:


input_salaris = st.sidebar.selectbox("select the experience level", ('MI' 'SE' 'EN' 'EX'))


# In[6]:


for col in data:
    print(data[col].unique())


# In[7]:


data_select = data[data["experience_level"] == input_salaris]


# In[8]:


st.dataframe(data_select)


# In[9]:


data['salary_in_euro']= data['salary_in_usd'] * 1.04


# In[10]:


import plotly.graph_objects as go
import plotly.express as px

fig = px.scatter(x=data['salary_in_usd'], color=data["experience_level"])
fig.show()


# In[11]:


fig = px.histogram(x=data['salary_in_usd'])

fig.update_layout(title='Salaris in US Dollars')
fig.update_xaxes(title='Salaris (usd)')
fig.update_yaxes(title='Hoeveelheid')

fig.show()


# In[12]:


fig = px.histogram(x=data['salary_in_euro'])

fig.update_layout(title='Salaris in Euro')
fig.update_xaxes(title='Salaris (euro)')
fig.update_yaxes(title='Hoeveelheid')

fig.show()


# In[13]:


# my_buttons = [{'label': "Bar plot",'method': "update",
#'args': [{"type": "bar"}]},{'label': "scatterplot",'method': "update",'args': [{"type": "scatter", 'mode': 'markers'}]}]


#fig.update_layout({'updatemenus': [{'type': "buttons",'direction': 'down',
#'x': 1.3, 'y': 0.5,'showactive': True,'active': 0,'buttons': my_buttons}]  })
#fig.show()


#'MI' 'SE' 'EN' 'EX'


# In[14]:


#Button interactivity
my_buttons= [{'label': "Bar plot",'method': "update",'args': [{"type": "bar"}]},
             {'label': "scatterplot",'method': "update",'args': [{"type": "scatter", 'mode': 'markers'}]}]

fig = px.bar(data_frame=data,x='job_title', y='salary_in_euro', color='experience_level')

fig.update_layout({'updatemenus': [{'type': "buttons",'direction': 'down',
                                    'x': 1.3, 'y': 0.5,'showactive': True,'active': 0,'buttons': my_buttons}]  })
fig.show()


# In[15]:


#dropdown_buttons = [  {'label': 'Ashfield', 'method': 'update','args': [{'visible': [True, False, False]},           
#{'title': 'Ashfield'}]},  {'label': 'Lidcombe', 'method': 'update','args': [{'visible': [False, True, False]},          
#{'title': 'Lidcombe'}]},  {'label': "Bondi Junction", 'method': "update",'args': [{"visible": [False, False, True]},          
#{'title': 'Bondi Junction'}]}]


#fig.update_layout({'updatemenus':[{'type': "dropdown",'x': 1.3,'y': 0.5,
#'showactive': True,'active': 0,'buttons': dropdown_buttons}]})fig.show()Ourdropdown:


# In[16]:


#dropdown

dropdown_buttons = [  {'label': 'MI', 'method': 'update','args': [{'visible': [True, False, False, False]},{'title': 'MI'}]},  
                    {'label': 'SE', 'method': 'update','args': [{'visible': [False, True, False, False]},{'title': 'SE'}]},  
                    {'label': "EN", 'method': "update",'args': [{"visible": [False, False, True, False]}, {'title': 'EN'}]}, 
                    {'label': 'EX', 'method': 'update','args': [{'visible': [False, False, False, True]},{'title': 'EX'}]}]

fig = px.bar(data_frame=data,x='job_title', y='salary_in_euro', color= 'experience_level')
fig.update_layout({'updatemenus':[{'type': "dropdown",'x': 1.3,'y': 0.5,'showactive': True,'active': 0,'buttons': dropdown_buttons}]})
fig.show()


# In[17]:


#sliders


# In[18]:


fig = px.scatter(  data_frame=data,  y='remote_ratio',   x='salary_in_euro',  color='experience_level', 
                 animation_frame='work_year')

#fig.update_layout({'yaxis': {'range': [0, 5000000]},'xaxis': {'range': [-100000, 2500000]}})
fig.update_layout(title= 'plot slider')
fig['layout'].pop('updatemenus')
fig.show()


# In[19]:


data.head()

