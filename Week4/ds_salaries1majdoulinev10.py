#!/usr/bin/env python
# coding: utf-8

# In[1]:


#pip install streamlit


# In[2]:


import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[3]:


url = 'https://raw.githubusercontent.com/gomeco/week4/main/Week4/ds_salaries.csv?token=GHSAT0AAAAAABZHO5T2YXZ4SPATO4N4SW22YZSYYYQ'
df = pd.read_csv(url)


# In[4]:


#Hoevaak elke job voorkomt
job_count=df["job_title"].value_counts()


# In[5]:


#filteren welke job's maar 1 salaris value_cout hebben
een_waarde=df.groupby('job_title').filter(lambda x : len(x)==1)


# In[6]:


#droppen van job's met 1 salaris value_cout 
#df.drop(een_waarde)


# In[7]:


#verwijderen van salarissen met 1 value_count
df_filtered = df[~df.salary_in_usd.isin(een_waarde)]


# In[8]:


st.title("Data Science Salarissen")


# In[10]:


import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px


# In[11]:


#st.title("Salaris Database")


# In[12]:


#input_salaris = st.sidebar.selectbox("select the experience level", ('MI' 'SE' 'EN' 'EX'))


# In[13]:


#data_select = df[df["experience_level"] == input_salaris]


# In[14]:


#st.dataframe(data_select)


# In[15]:


fig= px.scatter(df, x="salary_in_usd", y="job_title", color="experience_level", title="Salaris per baan")
fig.update_xaxes(title='Salaris')
fig.update_yaxes(title='Baantitel')
st.plotly_chart(fig, use_container_width=True)


# In[16]:


#fig = px.bar(df, y="salary_in_usd", x="job_title", color="experience_level", title="Long-Form Input")
#st.plotly_chart(fig, use_container_width=True)


# In[17]:


#g = sns.lmplot(x="job_title", y="salary_in_usd", data=df, hue='experience_level', 
              # markers=['v', 'x', '+'], height=8, ci=None)

#g.set_title("relatie tussen het gewicht en de vleugelgrootte per pinguinsoort.", color="#2D875F")
#g.set_xlabel("Gewicht")
#g.set_ylabel("Vleugelgrootte")

#new_title = ('.')
#g._legend.set_title(new_title)
#plt.title('Relatie tussen gewicht en vleugelgrootte per penguinsoort')
#plt.xlabel('Gewicht in gr')
#plt.ylabel('Vleugellengte in mm')




#plt.show()


# In[18]:


import plotly.graph_objects as go
import plotly.express as px

fig = px.scatter(x=df['salary_in_usd'], color=df["experience_level"], title='Spreiding salaris per werkervaring')
fig.update_xaxes(title='Salaris')
fig.update_yaxes(title='')
st.plotly_chart(fig, use_container_width=True)


# In[19]:


#Salarissen in USDollars - histogram
#fig = px.histogram(x=df['salary_in_usd'])

#fig.update_layout(title='Salaris in US Dollars')
#fig.update_xaxes(title='Salaris (usd)')
#fig.update_yaxes(title='Hoeveelheid')

#st.plotly_chart(fig, use_container_width=True)


# In[20]:


#Data manipulatie USD omzetten in euro's

df['salary_in_euro']= df['salary_in_usd'] * 1.04


# In[21]:


#Salarissen in Euro's - histogram

fig = px.histogram(x=df['salary_in_euro'])

fig.update_layout(title='Salaris in Euro')
fig.update_xaxes(title='Salaris (euro)')
fig.update_yaxes(title='Hoeveelheid')

st.plotly_chart(fig, use_container_width=True)


# In[22]:


#Gemiddelde salarissen in euro's van alle job titles
gemiddelde= df.groupby('job_title')['salary_in_euro'].mean()


# In[23]:


df1= gemiddelde.to_frame()


# In[105]:


#Button interactivity
#gemiddelde= data.groupby('job_title')['salary_in_euro'].mean()
# , color=data['experience_level']

my_buttons= [{'label': "Bar plot",'method': "update",'args': [{"type": "bar"}]},
             {'label': "Scatter plot",'method': "update",'args': [{"type": "scatter", 'mode': 'markers'}]}]

fig = px.bar(df1, y= df1.index , x= 'salary_in_euro', height=1000
            ,
            labels={"company_size": "Bedrijfsgrootte",
                     "salary_in_euro": "Salaris in Euro",
                     "experience_level": "Werkervaring",
                    "job_title": "Baan titel",
                    "work_year": "Werkjaar"
                 },
                title="Gemiddelde salaris per baan")
            
            

fig.update_layout({'updatemenus': [{'type': "buttons",'direction': 'down',
                                    'x': 1.3, 'y': 0.5,'showactive': True,'active': 0,'buttons': my_buttons}]  })
st.plotly_chart(fig, use_container_width=True)


# In[53]:


# Sliders

fig = px.scatter(  data_frame=df,  y='remote_ratio',   x='salary_in_euro',  color='experience_level', 
                 animation_frame='work_year'
                 
                 ,
            labels={"remote_ratio": "Remote ratio",
                     "salary_in_euro": "Salaris in Euro",
                     "experience_level": "Werkervaring",
                    "work_year": "Werkjaar"
                 },
                title="Salarissen per remote ratio op basis van werkervaring ")

fig['layout'].pop('updatemenus')
st.plotly_chart(fig, use_container_width=True)


# In[26]:


#df.head(30)


# In[73]:


# Sliders

fig = px.scatter(  data_frame=df,  x='job_title',   y='salary_in_euro',  color='company_size', 
                 animation_frame='work_year'
                 
                  ,
            labels={"company_size": "Bedrijfsgrootte",
                     "salary_in_euro": "Salaris in Euro",
                     "experience_level": "Werkervaring",
                    "work_year": "Werkjaar"
                 },
                title="Salarissen per banen op basis van bedrijfsgrootte ")
fig.update_xaxes(tickangle=25)
fig['layout'].pop('updatemenus')
st.plotly_chart(fig, use_container_width=True)


# In[38]:


#filteren welke job's >=11 voorkomen
df_filter=df.groupby('job_title').filter(lambda x : len(x)>=11)
df_filterjob = df_filter['job_title'].value_counts()


# In[75]:


# Sliders

#fig = px.scatter(data_frame=df_filter,  x='job_title',   y='salary_in_euro',  color='company_size', 
#                 animation_frame='work_year'
                 
#                  ,
#            labels={"company_size": "Bedrijfsgrootte",
#                     "salary_in_euro": "Salaris in Euro",
#                     "experience_level": "Werkervaring",
#                    "work_year": "Werkjaar",
#                    "job_title": "Baan titel"
#                 },
#                title="Salarissen zeven meest relevante banen op basis van bedrijfsgrootte ")
#fig['layout'].pop('updatemenus')

#st.plotly_chart(fig, use_container_width=True)


# In[98]:


#Slider boxplot
fig = px.box(  data_frame=df_filter,  x='job_title',   y='salary_in_euro',  color='company_size', 
                animation_frame='work_year'
                
                 ,
           labels={"company_size": "Bedrijfsgrootte",
                    "salary_in_euro": "Salaris in Euro",
                    "experience_level": "Werkervaring",
                   "job_title": "Baan titel",
                   "work_year": "Werkjaar"
                },
               title="Salarissen 7 meest relevante banen op basis van bedrijfsgrootte ")


fig['layout'].pop('updatemenus')
st.plotly_chart(fig, use_container_width=True)


# In[97]:


# Slider boxplot

#fig = px.box(  data_frame=df_filter,  x='experience_level',   y='salary_in_euro',  color='job_title', 
#                 animation_frame='work_year'
                 
#                  ,
#            labels={"company_size": "Bedrijfsgrootte",
#                     "salary_in_euro": "Salaris in Euro",
#                     "experience_level": "Werkervaring",
#                    "job_title": "Baan titel",
#                    "work_year": "Werkjaar"
#                 },
#                title="Salarissen 7 meest relevante banen op basis van Werkervaring ")
#fig['layout'].pop('updatemenus')
#st.plotly_chart(fig, use_container_width=True)
#fig.show()


# In[101]:


# Sliders

fig = px.scatter(  data_frame=df,  y='job_title',   x='salary_in_euro',  color='employment_type', 
                 animation_frame='work_year'
                 
                 ,
            labels={"company_size": "Bedrijfsgrootte",
                     "salary_in_euro": "Salaris in Euro",
                     "experience_level": "Werkervaring",
                    "job_title": "Baan titel",
                    "work_year": "Werkjaar",
                    "employment_type": "Contracttype"
                 },
                title="Baanshift van 2020 t/m 2022 op basis van contracttype ")

fig['layout'].pop('updatemenus')
st.plotly_chart(fig, use_container_width=True)
#PT Part-time, FT Full-time, CT Contract, FL Freelance


# In[116]:


#Salarissen per werkervaring in boxplots
fig = plt.figure()
ax = sns.boxplot(x=df["experience_level"], y=df["salary_in_usd"])
plt.title("Salarissen per werkervaring", color="#003333")
plt.xlabel("Werkervaring")
plt.ylabel("Salaris")
st.pyplot(fig)


# In[117]:


#Salarissen per employment type in boxplots
fig = plt.figure()
ax = sns.boxplot(x=df["employment_type"], y=df["salary_in_euro"])
plt.title("Salarissen per employment type", color="#003333")
plt.xlabel("Employment type")
plt.ylabel("Salaris")
st.pyplot(fig)


# In[87]:


medians = df.groupby(df["employment_type"])["salary_in_euro"].median()

st.write('Conclusie: FT heeft hoogste gemiddelde salaris, daarna CT, gevolgd door PT en FL')
# In[88]:


#order=["CT","FT", "FL", "PT"]


# In[102]:


#fig = plt.figure()
#ax = sns.boxplot(x=df["employment_type"], y=df["salary_in_euro"], order=order, width=0.4, palette='Reds')

#selecteren obv index

#medians = medians.reindex(order)

#pos = range(len(medians))
#for tick, label in zip(pos, ax.get_xticklabels()):
#    ax.text(pos[tick], medians[tick] + 100, medians[tick], 
#            horizontalalignment='center', size='x-small', color='b', weight='semibold')
    
#titel en labels
#plt.title("Salarissen in euro per employment type")
#plt.xlabel("Employment type")
#plt.ylabel("Salarissen in Euro")

    
#st.pyplot(fig)


# In[103]:


#fig = plt.figure()
#ax = sns.barplot(x=df["employment_type"], y=df["salary_in_euro"], hue=df["employment_type"])
#ax.set_title("barplots salarissen per employmenttype", color="black")
#ax.set_xlabel("")
#ax.set_ylabel("")
#st.pyplot(fig)


# In[37]:


#Filteren op jobs die 11x of vaker voorkomen
#job_count=df["job_title"].value_counts()
#job_count_filter = job_count >=11


# In[106]:


#Boxplots salarissen van de 7 meest voorkomende jobtitles
fig = px.box(df_filter, x="job_title", y="salary_in_euro", color="job_title",
            category_orders={"job_titles": ["Data Scientist", "Data Engineer", "Data Analyst", 
                                            "Machine Learnin Analyst", "Research Scientist", 
                                            "Data Science Manager", "Data Architect"]},
            labels={
                     "job_title": "Baan titel",
                     "salary_in_euro": "Salaris in Euro",
                     "job_title": "Baan titel"
                 },
                title="Salarissen van zeven meest voorkomende banen")
            



st.plotly_chart(fig, use_container_width=True)


# In[107]:


dropdown_buttons = [  {'label': 'MI', 'method': 'update','args': [{'visible': [True, False, False, False]},{'title': 'MI'}]},  
                    {'label': 'SE', 'method': 'update','args': [{'visible': [False, True, False, False]},{'title': 'SE'}]},  
                    {'label': "EN", 'method': "update",'args': [{"visible": [False, False, True, False]}, {'title': 'EN'}]},
                    {'label': 'EX', 'method': 'update','args': [{'visible': [False, False, False, True]},{'title': 'EX'}]}]



fig = px.box(df_filter, x="job_title", y="salary_in_euro", color="experience_level",
            category_orders={"job_title": ["Data Scientist"]},
            
            labels={
                     "job_title": "Baan titel",
                     "salary_in_euro": "Salaris in Euro",
                     "experience_level": "Werkervaring"
                 },
                title="Salarissen van zeven meest voorkomende banen met werkervaring")
            
fig.update_layout({'updatemenus':[{'type': "dropdown",'x': 1.3,'y': 0.5,'showactive': True,'active': 0,'buttons': dropdown_buttons}]})
st.plotly_chart(fig, use_container_width=True)


# In[41]:


#fig = px.box(df_filter, x="experience_level", y="salary_in_euro", color="job_title",
#            category_orders={"job_titles": ["Data Scientist", "Data Engineer", "Data Analyst", 
 #                                           "Machine Learnin Analyst", "Research Scientist", 
  #                                          "Data Science Manager", "Data Architect"]}
    #        ,
   #         labels={
     #                "job_title": "Baan titel",
      #               "salary_in_euro": "Salaris in Euro",
       #              "job_title": "Baan titel"
        #         },
         #       title="Salarissen van zeven meest voorkomende banen")
            
            

#fig.show()


# In[42]:


#keuzemenu voor verschillende grafieken
#Data Scientist               143
#Data Engineer                132
#Data Analyst                  97
#Machine Learning Engineer     41
#Research Scientist            16
#Data Science Manager          12
#Data Architect                11


# In[109]:


st.title("Selecteer een titel voor visualisatie")
line = st.selectbox("Kies een baantitel:", df_filterjob.index)
werkervaring = "experience_level"
bedrijfsgrootte = "company_size"
kleurkeuze = st.radio("Visualisatie op baseren op:", [werkervaring, bedrijfsgrootte])
fig = px.box(df[df['job_title']==line], x="experience_level", y="salary_in_euro", color=kleurkeuze
                ,
                labels={
                         "salary_in_euro": "Salaris in Euro",
                         "experience_level": "Werkervaring"
                     },
                    title="Spreiding salaris %s op basis van werkervaring"%(line))
st.plotly_chart(fig, use_container_width=True)


# In[112]:


fig = px.box(df_filter, x="experience_level", y="salary_in_euro", color="experience_level"
             
             ,
            labels={
                     "salary_in_euro": "Salaris in Euro",
                     "experience_level": "Werkervaring"
                 },
                title="Spreiding salarissen op basis van werkervaring - Algemeen")
            
            

st.plotly_chart(fig, use_container_width=True)


# In[45]:


gemiddelde= df_filter.groupby('job_title')['salary_in_euro'].mean()


# In[114]:


#fig = px.bar(gemiddelde, x=gemiddelde.index, y="salary_in_euro",
#            category_orders={"job_titles": ["Data Scientist", "Data Engineer", "Data Analyst",
#                                            "Machine Learnin Analyst", "Research Scientist",
#                                            "Data Science Manager", "Data Architect"]}
             
#             ,
#            labels={ "job_title": "Baan titel",
#                     "salary_in_euro": "Salaris in Euro"
#                 },
#                title="Per baan het gemiddelde salaris")
            
            



#st.plotly_chart(fig, use_container_width=True)
#fig.show()

