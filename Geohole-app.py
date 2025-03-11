import streamlit as st
import folium
from streamlit_folium import st_folium
import pandas as pd
import matplotlib.pyplot as plt

# Sample data for borehole locations
boreholes = pd.DataFrame({
    "Name": ["BH1", "BH2", "BH3"],
    "Latitude": [16.0471, 16.0545, 16.0608],
    "Longitude": [108.2063, 108.2102, 108.2150],
    "Soil Type": ["Clay", "Sand", "Silt"],
    "Depth (m)": [20, 30, 25]
})

st.title("Geohole - Geological Data Viewer")

# Select borehole
selected_bh = st.selectbox("Select a Borehole:", boreholes["Name"])
bh_data = boreholes[boreholes["Name"] == selected_bh].iloc[0]

# Display map
st.subheader("Borehole Location")
map_center = [bh_data["Latitude"], bh_data["Longitude"]]
map_ = folium.Map(location=map_center, zoom_start=15)
folium.Marker(map_center, popup=f"{selected_bh} - {bh_data['Soil Type']}").add_to(map_)
st_folium(map_, width=700, height=400)

# Display borehole details
st.subheader("Borehole Details")
st.write(f"**Name:** {bh_data['Name']}")
st.write(f"**Latitude:** {bh_data['Latitude']}")
st.write(f"**Longitude:** {bh_data['Longitude']}")
st.write(f"**Soil Type:** {bh_data['Soil Type']}")
st.write(f"**Depth:** {bh_data['Depth (m)']} meters")

# Sample chart
st.subheader("Soil Depth Comparison")
fig, ax = plt.subplots()
ax.bar(boreholes["Name"], boreholes["Depth (m)"], color=['red', 'blue', 'green'])
ax.set_ylabel("Depth (m)")
st.pyplot(fig)
