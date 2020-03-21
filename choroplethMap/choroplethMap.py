import folium
import pandas as pd


world_geo = r'C:/Users/Erdem/python kodları/Data_Visualization/world_countries.json' # geojson file

# create a plain world map
world_map = folium.Map(location=[0, 0], zoom_start=2, tiles='Mapbox Bright')

# Preparing the data.
covid_data = pd.read_csv("C:/Users/Erdem/python kodları/Data_Visualization/covid19Datas/covid_19_data.csv")

cd_grouped = covid_data[['Country/Region', 'Confirmed']]
cd_grouped = cd_grouped.groupby('Country/Region', as_index = False).max().sort_values('Country/Region', ascending = True)
print(cd_grouped)

cd_grouped.at[106,'Country/Region'] = 'China'
cd_grouped.at[179,'Country/Region'] = 'United Kingdom'
cd_grouped.at[180,'Country/Region'] = 'United States of America'
cd_grouped.at[128,'Country/Region'] = 'Macedonia'
cd_grouped.at[155,'Country/Region'] = 'Republic of Serbia'
cd_grouped.at[190,'Country/Region'] = 'West Bank'
cd_grouped.at[171,'Country/Region'] = 'United Republic of Tanzania'
cd_grouped.at[38,'Country/Region'] = 'Republic of the Congo'
cd_grouped.at[39,'Country/Region'] = 'Democratic Republic of the Congo'

pd.set_option('display.max_rows', 200)
print(cd_grouped)

# To compare by the population.
'''
world_pop = pd.read_csv("C:/Users/Erdem/python kodları/Data_Visualization/worldPopulationData/worldPop.csv")
world_pop = world_pop[['Country/Region', '2018']]

result = pd.concat([cd_grouped, world_pop], axis=1, join='outer')
result = pd.merge(cd_grouped, world_pop, how='left', on='Country/Region')
print(result)

cd_grouped['Confirmed'] = cd_grouped['Confirmed'] / result['2018']
print(cd_grouped)
'''

# create the Choropleth map.
folium.Choropleth(
    geo_data=world_geo,
    data=cd_grouped,
    columns=['Country/Region', 'Confirmed'],
    key_on='feature.properties.name',
    fill_color='YlOrRd', 
    fill_opacity=0.7, 
    line_opacity=0.3,
    legend_name='Confirmed Covid-19 Cases Across the Globe',
#    legend_name='Confirmed Covid-19 Cases rated by Population', 
    nan_fill_color = 'white',
    reset = True
).add_to(world_map)


# display world map
world_map.save('mapOfCases.html')
#world_map.save('mapByPopulation.html')