#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
from pandas import DataFrame
d=(['Simba','Lays'],['Coke','Fanta'],['Cadbury','Tex'],['Pepper Steak','Chicken'],['Pear','Apple','Orange'],['Vanilla','Chocolate'],['Spinach','Cabbage'])
row=['Chips','Cooldrinks','Chocolates','Pies','Fruit','Cupcakes','Veggies']
headers=['Product 1','Product 2','Product 3']
df=DataFrame(data=d,index=row,columns=headers)
print(df)



# In[ ]:




