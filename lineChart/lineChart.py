import matplotlib.pyplot as plt
import pandas as pd

vgs_data = pd.read_csv("C:/Users/Erdem/python kodları/Data_Visualization/videoGameSaleData/vgsales.csv")

vgs_data_grouped = vgs_data.groupby([vgs_data['Platform'], vgs_data['Year']], as_index = False).agg({'Global_Sales':'sum'}).sort_values('Year')
vgs_data_grouped2 = vgs_data_grouped.drop(vgs_data_grouped[vgs_data_grouped['Platform'] != 'PS2'].index)
vgs_data_grouped = vgs_data_grouped.drop(vgs_data_grouped[vgs_data_grouped['Platform'] != 'PC'].index)
print(vgs_data_grouped)

plt.figure(figsize=(15,9))
plt.plot('Year','Global_Sales', data = vgs_data_grouped, color='cyan', lw = 5)
plt.plot('Year','Global_Sales', data = vgs_data_grouped2, color='red', lw = 5)

plt.title('Global PC and PS2 Sales from 1985-2016', color = 'red', fontsize = 20)
plt.xlabel('Year', color = 'red', fontsize = 15)
plt.ylabel('Number of Sales(M)', color = 'red', fontsize = 15)
plt.xticks(fontsize = 12)
plt.yticks(fontsize = 12)
plt.legend(labels=['PC', 'PS2'], loc='upper left', prop={'size': 15}) 

plt.savefig('videoGameLine.png')
plt.show()

# İnat edip her şeyi plt ile yaptım ama multiple line plotlarda axes kullanmak daha mantıklı.