#!/usr/bin/env python
# coding: utf-8

# # Data Visualisation using Charts  

# #Install matplotlib for creating charts and graphs in python 

# In[13]:


pip install matplotlib


# #Create a Sample Data Set 

# In[3]:


#Creating a small sample of countries and their GDP per capita 
Country = ['USA', 'Canada', 'Germany', 'UK', 'France']
GDPPerCapita = [45000, 42000, 52000, 49000, 47000]


# #Create the Column chart in python using matplot

# In[8]:


import matplotlib.pyplot as plt

plt.bar(Country, GDPPerCapita)
plt.title('GDP of Countries')
plt.xlabel('Country')
plt.ylabel('GDP Per Capita')
plt.show()


# #To modify the Column chart let's add some colors and grids 

# In[9]:


import matplotlib.pyplot as plt
   
Country = ['USA','Canada','Germany','UK','France']
GDPPerCapita = [45000,42000,52000,49000,47000]

New_Colors = ['green','blue','purple','brown','teal']
plt.bar(Country, GDPPerCapita, color=New_Colors)
plt.title('Country Vs GDP Per Capita', fontsize=14)
plt.xlabel('Country', fontsize=14)
plt.ylabel('GDP Per Capita', fontsize=14)
plt.grid(True)
plt.show()


# #In case their is alot of data which can not be represented well in vertical columns 
# #A good way to present them is using Bar Charts which are horizontal in nature

# In[24]:


import matplotlib.pyplot as plt
   
Country = ['USA','Canada','Germany','UK','France','India', 'China']
GDPPerCapita = [45000,42000,52000,49000,47000,25000,38000]

New_Colors = ['green','blue','purple','brown','teal', 'orange', 'red']
plt.barh(Country, GDPPerCapita, color=New_Colors)
plt.title('Country Vs GDP Per Capita', fontsize=14)
plt.ylabel('Country', fontsize=14)
plt.xlabel('GDP Per Capita', fontsize=14)
plt.grid(True)
plt.show()


# In[14]:


import seaborn as sns

iris = sns.load_dataset('iris')
ax = sns.barplot('species', 'sepal_width', data=iris)
widthbars = [0.3, 0.6, 1.2]
for bar, newwidth in zip(ax.patches, widthbars):
    x = bar.get_x()
    width = bar.get_width()
    centre = x + width/2.
    bar.set_x(centre - newwidth/2.)
    bar.set_width(newwidth)


# #Let's try to work on Volumn Width Column Charts on some simple data 

# In[28]:


import matplotlib.pyplot as plt
Name = ['Ryan', 'Gerald', 'Heather', 'Krish']
Earnings = [5000, 2800, 7550, 3500] 
w = [0.8, 0.2, 1.1, 0.5 ]

plt.bar(Name, height = Earnings, width = w)
New_Colors = ['green','blue', 'brown', 'orange']
plt.bar(Name, Earnings, color=New_Colors)
plt.title('Earnings per Person', fontsize=14)
plt.ylabel('Name', fontsize=14)
plt.xlabel('Earnings', fontsize=14)


plt.show()


# In[ ]:




