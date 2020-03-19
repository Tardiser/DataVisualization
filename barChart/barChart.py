import matplotlib.pyplot as plt
import pandas as pd

covid_data = pd.read_csv("C:/Users/Erdem/python kodları/Data_Visualization/covid19Datas/covid_19_data.csv")

cd_grouped = covid_data[['Country/Region', 'Confirmed']]
cd_grouped = cd_grouped.groupby('Country/Region').sum().sort_values('Confirmed', ascending = False)

cd_grouped_top5 = cd_grouped.iloc[1:6]
print(cd_grouped_top5)

cd_grouped_top5.plot(kind = 'bar', figsize = (15,9))
plt.ylabel('Number of Infection', color = 'red', fontsize = 20)
plt.xlabel('Country', color = 'red', fontsize = 20)
plt.title('Top 5 Infected Countries\n(Other than China)', color = 'red', fontsize = 25)
plt.xticks(color='purple', wrap = True, rotation = 0, fontsize = 15)
plt.yticks(color='purple', wrap = True, rotation = 0, fontsize = 15)

plt.savefig('covidBar.png')
plt.show()
