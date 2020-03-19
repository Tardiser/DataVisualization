import matplotlib.pyplot as plt
import pandas as pd

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
vgs_data_grouped.drop(['GBA', 'PSP','Wii','DS','PS','PS2', 'PS4'], axis=1, inplace = True)
vgs_data_grouped.drop(drop_rows, axis=0, inplace = True)
#vgs_data_grouped.fillna(0, inplace = True) # If necessary 
print(vgs_data_grouped)

''' It's finally time to plot the data. '''
vgs_data_grouped.plot(kind='box', figsize=(15, 9), boxprops = {'linewidth':3}, medianprops = {'linewidth':3}, capprops = {'linewidth':3}, whiskerprops={'linewidth':3}, flierprops = {'markersize':10})
# For more customization: https://matplotlib.org/3.1.0/gallery/statistics/boxplot.html
plt.title('Box plots of Immigrants from China and India (1980 - 2013)', color = 'red', fontsize = 20)
plt.xlabel('Platform', color = 'red', fontsize = 15)
plt.ylabel('Number of Sales(M)', color = 'red', fontsize = 15)
plt.xticks(fontsize = 12)
plt.yticks(fontsize = 12)

plt.savefig('videoGameBox.png')
plt.show()