#Data Visualization of Amazon.com Stock Price between 2019 and 2021

#Importing the required libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Reading Data from 'Amazon.csv' File and storing it in 'df' variable

df = pd.read_csv('Amazon.csv')
df.head()


#Describing the data types of each column in the dataset

df.dtypes


#Changing the data type of Date Column in Dataset to get year as Ticks on x-axis in the plot

df['Date']=pd.to_datetime(df.Date)


#Extracting Year and creating a separate column for Year in the dataset

df['Year']=df.Date.dt.year


#Selecting Data from the Year 2019 to 2021 for plotting and storing it in a new variable 'df1'

df1 = df.loc[(df['Year']>=2019)&(df['Year']<=2021)]
df1.head()


#Plot showing the Highest and Lowest Prices of Amazon Stock

x = df1['Date']
y = df1['High']
z = df1['Low']
plt.plot(x,y,color='green',label='High')
plt.plot(x,z,color='red',label='Low')
plt.title('Amazon.com(AMZN) Stock Highest and Lowest Prices from the year 2019 to 2021')
plt.xlabel('Date')
plt.ylabel('Price in USD($)')
plt.legend(loc='upper left')
plt.xticks(rotation=90)
plt.grid()
plt.show()


#Subplots

#Sub-plot showing the Highest prices of Amazon Stock between 2019 and 2021

plt.subplot(2,1,1)
plt.plot(x,y,color='green',label='High')
plt.title('Amazon.com(AMZN) Stock Highest Prices between 2019 and 2021')
plt.ylabel('Price in USD($)')
plt.xlabel('Year and Month')
plt.legend(loc='upper left')
plt.xticks(rotation=90)
plt.grid()
plt.show()


#Sub-plot showing the Lowest prices of Amazon Stock between 2019 and 2021

plt.subplot(2,1,2)
plt.plot(x,z,color='red',label='Low')
plt.title('Amazon.com(AMZN) Stock Lowest Prices between 2019 and 2021')
plt.ylabel('Price in USD($)')
plt.xlabel('Year and Month')
plt.legend(loc='upper left')
plt.xticks(rotation=90)
plt.grid()
plt.show()

