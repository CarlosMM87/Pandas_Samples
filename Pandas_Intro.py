#!/usr/bin/env python
# coding: utf-8

# In[15]:


import pandas as pd
import matplotlib.pyplot as plt


# In[16]:


table1 = pd.read_csv(r'C:\Users\Carlos Marin\Desktop\Resumen_ventas.csv', skiprows=[2,4])


# In[17]:


table1


# In[ ]:


#Call one series from the dataframe


# In[18]:


table1['Producto']


# In[19]:


table1.head(3)


# In[20]:


table1.tail(6)


# In[21]:


table1.info()


# In[22]:


table1.Producto.value_counts(ascending=True)


# In[ ]:


#Boolean conditions


# In[23]:


table1[(table1.Producto == 'Libros')]


# In[26]:


table1.Producto.str.contains('Juguetes')


# In[27]:


prod = table1[table1.Producto == 'Libros']


# In[28]:


prod.Meses.value_counts().plot(kind='barh')
plt.show()


# In[32]:


prod = table1[table1.Producto == 'Libros']
prod2 = table1.rename(columns={"Total Venta": "Total_Venta"})
prod2.Total_Venta.value_counts().plot(kind="pie")
plt.show()


# In[33]:


prod3 = table1
prod3.Producto.value_counts().plot(kind="pie")
plt.show()


# In[34]:


prod.Meses.value_counts().plot(kind='barh', color='orange')
plt.show()


# In[35]:


prod3 = table1
prod3.Producto.value_counts().plot(kind="pie", colormap='jet')
plt.show()


# In[37]:


prod.Meses.value_counts().plot(kind='barh', color='blue', figsize=(7,3))
plt.show()


# In[ ]:


#Indexing


# In[39]:


table4 = pd.read_csv(r'C:\Users\Carlos Marin\Desktop\VentasPorProveedor.csv', skiprows=5, delimiter=';')
table4


# In[47]:


table4.index[10]


# In[48]:


table4.set_index('Vendedor').head(5)


# In[54]:


table4.loc[5][3]


# In[56]:


table4.iloc[5][4]


# In[57]:


table4.groupby('Región')


# In[58]:


type(table4.groupby('Región'))


# In[67]:


for group_key, group_value in table4.groupby('Región'):
    print(group_key)
    print(group_value['Categoría'])


# In[69]:


table4.groupby('Categoría').size()


# In[74]:


table4.loc[table4.Vendedor =='Desmond Delaney'].groupby('Vendedor').sum({'Ganancia'})


# In[75]:


table4.loc[table4.Vendedor =='Desmond Delaney']


# In[ ]:




