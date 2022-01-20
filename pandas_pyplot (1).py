#!/usr/bin/env python
# coding: utf-8

# In[2]:


#nesscary libraries 
#seaborn extends matplotlib libraries

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
sns.set (color_codes= True)


# In[3]:


car = pd.read_csv('car.csv')


# In[22]:


car.head(5)


# In[5]:


car.dtypes


# In[6]:


car.columns.values


# In[7]:


#Analytical Summary of dataset

car.describe(include= "all")


# In[8]:


#Chart type hist= Histogram

car.hist(figsize =(20,30))


# In[46]:


#Relationship between categorical and continuous variables
sns.boxplot(x='Vehicle Size', y='Engine HP', data= car)


# In[10]:


sns.pairplot(car)


# In[11]:


# drop irrelevant data

car =car.drop(['Engine Fuel Type','Market Category', 'Vehicle Size','Popularity', 'Number of Doors', 'Vehicle Size' ],axis=1)


# In[12]:


car.head(5)


# In[13]:


car=car.rename(columns={'Engine HP': 'HP', 'Engine Cylinders' : 'Cylinders', 'Transmission Type': 'Transmission', 'Driven_Wheels': 'Drive Type', 'highway MPG': 'H-MPG', 'city mpg': 'C-MPG','MSRP': 'Price'})
car.head(5)


# In[14]:


# number of total rows and columns
car.shape


# In[15]:


#Duplicate rows

duplicate_rows_car = car[car.duplicated()]
print('Number of duplicate rows:', duplicate_rows_car.shape)


# In[16]:


#Count rows before deleting

car.count()


# In[17]:


#Drop duplicates

car = car.drop_duplicates()
car


# In[21]:


car.count()


# In[26]:


car.head()


# In[27]:


car.count()


# In[28]:


#Find null values
print(car.isnull().sum())


# In[30]:


#drop null values
car=car.dropna()
car.count()


# In[31]:


print(car.isnull().sum())


# In[32]:


sns.boxplot(x=car['Price'])


# In[33]:


sns.boxplot(x=car['HP'])


# In[39]:


# Plotting histogram by car brand
#plt.title = Title
#plt.label = x/y labels
car.Make.value_counts().nlargest(40).plot(kind='bar', figsize=(10,5))
plt.title('Number of Cars by Make')
plt.xlabel('Make')
plt.ylabel('Number of cars');


# In[45]:


#Find the relationships between variables
#.corr = correlations
plt.figure(figsize=(20,10))
c= car.corr()
sns.heatmap(c,cmap='BrBG',annot=True)
c


# In[ ]:




