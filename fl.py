import folium
import pandas as pd
import os
#
# states = os.path.join('data', 'us-states.json')
# unemployement_data = os.path.join('data', 'us_unemployment.csv')
# state_data = pd.read_csv(unemployement_data)

m = folium.Map(location=[48, -102], zoom_start=15)

folium.LayerControl().add_to(m)#######

m.save('map4.html')