import matplotlib.pyplot as plt
import pandas as pd
from pywaffle import Waffle

covid_data = pd.read_csv("C:/Users/Erdem/python kodları/Data_Visualization/covid19Datas/covid_19_data.csv")

cd_grouped = covid_data[['Country/Region', 'Confirmed']]
cd_grouped = cd_grouped.groupby('Country/Region', as_index = False).sum().sort_values('Confirmed', ascending = False)

cd_grouped_top5 = cd_grouped.iloc[:5]
cd_grouped_top5['Confirmed']  = cd_grouped_top5['Confirmed'].astype(int)
print(cd_grouped_top5)

fig = plt.figure(
    FigureClass=Waffle, 
    rows=5,
    title = {'label':'Waffle Chart of Top 5 Infected Countries', 'fontsize':20}, 
    figsize=(15, 9),
    values=list(cd_grouped_top5['Confirmed']/20000),
    labels=list(cd_grouped_top5['Country/Region']),
    legend={'loc': 'upper left', 'bbox_to_anchor': (1.1, 1), 'prop':{'size': 15}}
)

plt.savefig('covidWaffle.png')
plt.show()