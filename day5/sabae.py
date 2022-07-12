import pandas as pd
import folium

m=folium.Map(location=[35.942957,136.198863],zoom_start=16)
df=pd.read_csv('200.csv',encoding='shift-jis')

hydrant = df[['経度','緯度']].values

for data in hydrant:
    folium.Marker([data[1],data[0]]).add_to(m)
m.save('hydrant.html')
