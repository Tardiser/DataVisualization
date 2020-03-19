import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

vgs_data = pd.read_csv("C:/Users/Erdem/python kodları/Data_Visualization/videoGameSaleData/vgsales.csv")
print(vgs_data.head())


''' Yapmaya çalıştığımız şey, Platform isimleri column ismi olacak, örnek:          PC Wii
                                                                            1980   125 45
                                                                            1981   150 80   '''
vgs_data_grouped = vgs_data.groupby([vgs_data['Year'], vgs_data['Platform']], as_index = False).agg({'Global_Sales':'sum'}).sort_values('Year')
vgs_data_grouped = vgs_data_grouped.pivot(index='Year', columns='Platform', values='Global_Sales')

''' En çok satış yapan 10 platformu bulup diğerlerini dropluyoruz. '''
top10SalesPlatform = vgs_data.groupby('Platform', as_index = False).agg({'Global_Sales':'sum'}).sort_values('Global_Sales', ascending = False)
drop_columns = top10SalesPlatform['Platform'].tail(21).to_numpy()

''' 1980 - 1990 arasında satışlar çok düşük olduğu için, bu yılları grafikten çıkarıyoruz.'''
drop_rows = range(1980, 1990)

vgs_data_grouped.drop(drop_columns, axis=1, inplace = True)
vgs_data_grouped.drop(['GBA', 'PC', 'X360', 'PSP','Wii','DS','PS'], axis=1, inplace = True)
vgs_data_grouped.drop(drop_rows, axis=0, inplace = True)
vgs_data_grouped2 = vgs_data_grouped.fillna(0) # If necessary 
print(vgs_data_grouped)

''' It's finally time to plot the data. '''
count, bin_edges = np.histogram(vgs_data_grouped2, 10)
xmin = bin_edges[0] - 10   #  first bin value is 31.0, adding buffer of 10 for aesthetic purposes 
xmax = bin_edges[-1] + 10  #  last bin value is 308.0, adding buffer of 10 for aesthetic purposes

# stacked Histogram
vgs_data_grouped.plot(kind='hist',
          figsize=(15, 9), 
          bins=10,
          xticks=bin_edges,
          alpha=0.6,
          color=['coral', 'darkslateblue', 'mediumseagreen'],
          stacked=False,
          xlim=(xmin, xmax)
         )

plt.title('Histogram of PS Game Sales Over the Years', color = 'red', fontsize = 20)
plt.ylabel('Number of Years', color = 'red', fontsize = 15)
plt.xlabel('Number of Sales', color = 'red', fontsize = 15) 
plt.xticks(fontsize = 12)
plt.yticks(fontsize = 12)

plt.savefig('videoGameHistogram.png')
plt.show()