#import pandas
import pandas as pd
#impoting dataframe from pandas
from pandas import DataFrame
#Declaring 2d lists
data1=(['Simba','Lays'],['Coke','Fanta'],['Cadbury','Tex'],['Pepper Steak','Chicken'],['Pear','Apple','Orange'],['Vanilla','Chocolate'],['Spinach','Cabbage'])
data2=(['Simba','Coke','Cadbury','Pepper Steak','Pear','Vanilla','Spinach'],['Lays','Fanta','Tex','Chicken','Apple','Chocolate','Cabbage'],['Orange'])
#Creating list with row headings
row=['Chips','Cooldrinks','Chocolates','Pies','Fruit','Cupcakes','Veggies']
#Declaring list with column headings
headers=['Product 1','Product 2','Product 3']
#Declaring dataframes
df=DataFrame(data=data1,index=row,columns=headers)
df2=DataFrame(data=data2,index=headers,columns=row)
#Displaying dataframes
print(df)
print('')
print(df2)





