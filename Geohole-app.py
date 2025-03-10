import streamlit as st
import folium
from streamlit_folium import st_folium

# Danh sách 5 lỗ khoan với tọa độ và thông tin chi tiết
boreholes = [
    {
        "name": "Lỗ khoan 1",
        "lat": 16.0678,
        "lon": 108.2208,
        "info": """<b>Chiều sâu:</b> 30m<br>
                   <b>Lớp 1:</b> A Cát - 10m<br>
                   <b>Lớp 2:</b> Sét - 15m<br>
                   <b>Lớp 3:</b> Đá góc - 5m"""
    },
    {"name": "Lỗ khoan 2", "lat": 16.0544, "lon": 108.2022, "info": "Thông tin đang cập nhật..."},
    {"name": "Lỗ khoan 3", "lat": 16.0478, "lon": 108.2100, "info": "Thông tin đang cập nhật..."},
    {"name": "Lỗ khoan 4", "lat": 16.0600, "lon": 108.2300, "info": "Thông tin đang cập nhật..."},
    {"name": "Lỗ khoan 5", "lat": 16.0555, "lon": 108.2155, "info": "Thông tin đang cập nhật..."},
]

# Tạo bản đồ trung tâm tại Đà Nẵng
m = folium.Map(location=[16.0544, 108.2022], zoom_start=12)

# Thêm điểm lỗ khoan vào bản đồ
for borehole in boreholes:
    folium.Marker(
        location=[borehole["lat"], borehole["lon"]],
        popup=folium.Popup(borehole["info"], max_width=300),
        icon=folium.Icon(color="blue", icon="info-sign")
    ).add_to(m)

# Hiển thị bản đồ trong Streamlit
st.title("Bản đồ địa chất Đà Nẵng với thông tin lỗ khoan")
st_folium(m, width=700, height=500)
