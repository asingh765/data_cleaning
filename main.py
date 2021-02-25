
# coding: utf-8

# In[230]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


# In[231]:


# Open the url into a dataframe. Name the columns.
dataset = "https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data"
df = pd.read_csv(dataset, header=None)
df.columns = ['Symboling','Normalized-losses','Make', 'Fuel-type','Aspiration','Num-of-doors','Body-style', 'Drive-wheels', 'Engine-location', 'Wheel-base', 'Length', 'Width', 'Height', 'Curb-weight', 'Engine-type', 'Num-of-cylinders', 'Engine-size', 'Fuel-system', 'Bore', 'Stroke', 'Compression-ratio', 'Horsepower', 'Peak-rpm', 'City-mpg', 'Highway-mpg', 'Price']


# In[232]:


# Check for ? in the column and replace with the mean
df['Normalized-losses'].loc[df['Normalized-losses'] == '?'].count()
a = df['Normalized-losses'].loc[df['Normalized-losses'] != '?']
a_mean = a.astype(str).astype(int).mean()
df['Normalized-losses'] = df['Normalized-losses'].replace('?',a_mean).astype(int)
df['Normalized-losses'].head()


# In[233]:


# Check for ? in the column and replace with the mean
df['Price'].loc[df['Price'] == '?'].count()
b = df['Price'].loc[df['Price'] != '?']
b_mean = b.astype(str).astype(int).mean()
df['Price'] = df['Price'].replace('?',b_mean).astype(int)
df['Price'].head()


# In[217]:


# Check for ? in the column and replace with the mean
df['Horsepower'].loc[df['Horsepower'] == '?'].count()
n3 = df['Horsepower'].loc[df['Horsepower'] != '?']
n3mean = n3.astype(str).astype(int).mean()
df['Horsepower'] = df['Horsepower'].replace('?',n3mean).astype(int)
df['Horsepower'].head()


# In[218]:


# Change non-numeric values to null type and convert the data type
df['Bore'] = pd.to_numeric(df['Bore'],errors='coerce')
df['Stroke'] = pd.to_numeric(df['Stroke'],errors='coerce')
df['Peak-rpm'] = pd.to_numeric(df['Peak-rpm'],errors='coerce')


# In[197]:


# Remove the ? values from the column
df['Num-of-doors'].loc[df['Num-of-doors'] == '?']
df = df[df['Num-of-doors'] != '?']
df['Num-of-doors'].loc[df['Num-of-doors'] == '?']


# In[198]:


df.Make.value_counts().nlargest(10).plot(kind='bar', figsize=(15,5))
plt.title("Number of vehicles by make")
plt.ylabel('Number of vehicles')
plt.xlabel('Make');


# In[199]:


df.Symboling.hist(bins=6,color='green');
plt.title("Insurance risk ratings of vehicles")
plt.ylabel('Number of vehicles')
plt.xlabel('Risk rating');


# In[219]:


df['Normalized-losses'].hist(bins = 5,color='orange');
plt.title("Normalized losses of vehicles")
plt.ylabel('Number of vehicles')
plt.xlabel('Normalized losses');


# In[201]:


df['Fuel-type'].value_counts().plot(kind='bar',color='purple')
plt.title("Fuel type frequence diagram")
plt.ylabel('Number of vehicles')
plt.xlabel('Fuel type');


# In[202]:


df['Aspiration'].value_counts().plot.pie(figsize=(6, 6), autopct='%.2f')
plt.title("Aspiration type pie diagram")
plt.ylabel('Number of vehicles')
plt.xlabel('Fuel type');


# In[220]:


df.Horsepower[np.abs(df.Horsepower - df.Horsepower.mean()) <= (3 * df.Horsepower.std())].hist(bins = 5,color = 'red');
plt.title("Horse power histogram")
plt.ylabel('Number of vehicles')
plt.xlabel('Horse power');


# In[169]:


df['Curb-weight'].hist(bins=5,color='brown');
plt.title("Curb weight histogram")
plt.ylabel('Number of vehicles')
plt.xlabel('Curb weight');


# In[170]:


df['Drive-wheels'].value_counts().plot(kind='bar',color='grey')
plt.title("Drive wheels diagram")
plt.ylabel('Number of vehicles')
plt.xlabel('Drive wheels');


# In[171]:


df['Num-of-doors'].value_counts().plot(kind='bar',color='purple')
plt.title("Number of doors frequency diagram")
plt.ylabel('Number of vehicles')
plt.xlabel('Number of doors');


# In[221]:


plt.rcParams['figure.figsize']=(10,5)
ax = sns.boxplot(x="Drive-wheels", y="Price", data=df)


# In[236]:




