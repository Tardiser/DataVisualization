import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

vgs_data = pd.read_csv("C:/Users/Erdem/python kodları/Data_Visualization/videoGameSaleData/vgsales.csv")

''' Yapmaya çalıştığımız şey, Platform isimleri column ismi olacak, örnek:          PC Wii
                                                                            1980   125 45
                                                                            1981   150 80   '''
vgs_data_grouped = vgs_data.groupby([vgs_data['Year'], vgs_data['Platform']], as_index = False).agg({'Global_Sales':'sum'}).sort_values('Year')
vgs_data_grouped = vgs_data_grouped.pivot(index='Year', columns='Platform', values='Global_Sales')

''' 1980 - 1990 arasında satışlar çok düşük olduğu için, bu yılları grafikten çıkarıyoruz.'''
drop_rows = list(range(1980, 2005))
vgs_data_grouped.drop(drop_rows, axis=0, inplace = True)

''' En çok satış yapan 10 platformu bulup diğerlerini dropluyoruz. '''
top10SalesPlatform = vgs_data.groupby('Platform', as_index = False).agg({'Global_Sales':'sum'}).sort_values('Global_Sales', ascending = False)
drop_columns = top10SalesPlatform['Platform'].tail(21).to_numpy()
vgs_data_grouped.drop(drop_columns, axis=1, inplace = True)
vgs_data_grouped.drop(['GBA', 'PS', 'PSP'], axis = 1, inplace = True) # 2005-2020 arasında az satış yapan platformlar.

vgs_data_grouped.fillna(0, inplace = True)
print(vgs_data_grouped)

plt.figure(figsize=(20,10))
plt.xticks(fontsize = 12)
plt.yticks(fontsize = 12)
plt.xlabel('Platform', color = 'red', fontsize = 15)
plt.ylabel('Year', color = 'red', fontsize = 15)

ax = sns.heatmap(vgs_data_grouped, cmap="YlOrRd")

plt.savefig('videoGameHeatMap.png')
plt.show()

