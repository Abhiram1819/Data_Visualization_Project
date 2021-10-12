import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("Amazon.csv")
df['Date']=pd.to_datetime(df.Date)
df['Year']=df.Date.dt.year
df1 = df.loc[(df['Year']>=2019)&(df['Year']<=2021)]
x = df1['Date']
y = df1['High']
z = df1['Low']
plt.plot(x,y,color='green',label='High')
plt.plot(x,z,color='red',label='Low')
plt.title('Amazon.com(AMZN) Stock Highest and Lowest Prices from the year 2019 to 2021')
plt.xlabel('Year and Month')
plt.ylabel('Price in USD($)')
plt.legend(loc='upper left')
plt.grid()
plt.show()