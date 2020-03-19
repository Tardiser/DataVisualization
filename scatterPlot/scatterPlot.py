import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

vgs_data = pd.read_csv("C:/Users/Erdem/python kodları/Data_Visualization/videoGameSaleData/vgsales.csv")

vgs_data_grouped = vgs_data.groupby([vgs_data['Platform'], vgs_data['Year']], as_index = False).agg({'Global_Sales':'sum'}).sort_values('Year')
vgs_data_grouped = vgs_data_grouped.drop(vgs_data_grouped[vgs_data_grouped['Platform'] != 'PC'].index)
print(vgs_data_grouped)

vgs_data_grouped.plot(kind='scatter', x='Year', y='Global_Sales', figsize=(15, 9), color='cyan', s = 100)

fit = np.polyfit(vgs_data_grouped['Year'], vgs_data_grouped['Global_Sales'], deg=1) # To calculate the regression line.
plt.plot(vgs_data_grouped['Year'], fit[0] * vgs_data_grouped['Year'] + fit[1], color='red') # To plot the regression line.


plt.title('Global PC Sales from 1985-2016', color = 'red', fontsize = 20)
plt.xlabel('Year', color = 'red', fontsize = 15)
plt.ylabel('Number of Sales(M)', color = 'red', fontsize = 15)
plt.xticks(fontsize = 12)
plt.yticks(fontsize = 12)

plt.savefig('videoGameScatter.png')
plt.show()

''' Scatter'da axisler numeric olmalı, bu da bizim dataya uymuyor, farklı bir data bulalım. '''