import pandas as pd
import folium

df=pd.read_csv('51a0ab9e-e702-40c2-bc0e-1c5ce1da4e66.csv')

store=df[['緯度','経度','説明']].values

m=folium.Map(location=[36.57234515572543, 136.6568610528364],zoom_start=16)
for data in store:
    folium.Marker([data[0],data[1]],tooltip=data[2]).add_to(m)
m.save('spots.html')

