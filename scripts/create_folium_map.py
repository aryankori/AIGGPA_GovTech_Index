import folium

# Coordinates
places = {
    'AIGGPA': (23.2153, 77.3808),
    'Forest (Van Bhawan)': (23.2248, 77.4151),
    'Health (Satpura Bhawan)': (23.2355, 77.4212),
    'Rural Dev (Vindhyachal)': (23.2361, 77.4210),
    'Revenue (Vallabh Bhawan)': (23.2374, 77.4195),
    'Home (Bagmugaliya)': (23.1860, 77.4792),
}

# Create map centered at Bhopal
m = folium.Map(location=[23.2153, 77.4151], zoom_start=13)

# Add markers
for name, (lat, lon) in places.items():
    color = 'red' if name == 'Home (Bagmugaliya)' else ('green' if name == 'AIGGPA' else 'blue')
    folium.Marker(
        [lat, lon],
        popup=name,
        tooltip=name,
        icon=folium.Icon(color=color)
    ).add_to(m)

# Draw lines to show the cluster
cluster_pts = [(23.2355, 77.4212), (23.2361, 77.4210), (23.2374, 77.4195)]
folium.PolyLine(cluster_pts, color="purple", weight=2.5, opacity=1).add_to(m)

# Save to file
output_path = 'fieldwork_map.html'
m.save(output_path)
print(f"Interactive map saved as {output_path}")
