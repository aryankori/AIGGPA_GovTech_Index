import matplotlib.pyplot as plt

# Coordinates
places = {
    'AIGGPA': (23.2153, 77.3808),
    'Forest (Van Bhawan)': (23.2248, 77.4151),
    'Health (Satpura Bhawan)': (23.2355, 77.4212),
    'Rural Dev (Vindhyachal)': (23.2361, 77.4210),
    'Revenue (Vallabh Bhawan)': (23.2374, 77.4195),
    'Home (Bagmugaliya)': (23.1860, 77.4792),
}

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 7))

# Plot 1: Overview
lats = [coord[0] for coord in places.values()]
lons = [coord[1] for coord in places.values()]
ax1.scatter(lons, lats, color='blue', s=100)

for label, (lat, lon) in places.items():
    ax1.annotate(label, (lon, lat), textcoords="offset points", xytext=(0,10), ha='center', fontsize=8)

ax1.set_title('Fieldwork Locations Overview')
ax1.set_xlabel('Longitude')
ax1.set_ylabel('Latitude')
ax1.grid(True)

# Plot 2: Zoomed view of Cluster
cluster_places = {
    'Health (Satpura)': (23.2355, 77.4212),
    'Rural Dev (Vindhyachal)': (23.2361, 77.4210),
    'Revenue (Vallabh)': (23.2374, 77.4195),
}

c_lats = [coord[0] for coord in cluster_places.values()]
c_lons = [coord[1] for coord in cluster_places.values()]
ax2.scatter(c_lons, c_lats, color='green', s=150)

for label, (lat, lon) in cluster_places.items():
    ax2.annotate(label, (lon, lat), textcoords="offset points", xytext=(0,10), ha='center', fontsize=10)

ax2.set_title('Zoomed View: Arera Hills Cluster')
ax2.set_xlabel('Longitude')
ax2.set_ylabel('Latitude')
ax2.grid(True)

plt.tight_layout()
output_path = 'fieldwork_map.png'
plt.savefig(output_path)
print(f"Map saved as {output_path}")
