import folium

map = folium.Map(
    location = [40.20234, 28.80561],
    titles = "Ev", 
    zoom_start = 16
)

folium.Marker(
    [40.20234, 28.80561],
    popup = "<i>Bursa/Nilufer Kizilcikli Mahallesi</i>",
    tooltip = "Vatansever Ailesi"
).add_to(map)

map.save("C:\\Users\\doguk\\Desktop\\DGKN\\Software\\Codes\\Python\\Import\\Maps\\map.html")