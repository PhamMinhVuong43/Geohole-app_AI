import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
import matplotlib.pyplot as plt

# Load sample borehole data
def load_data():
    data = {
        "ID": ["BH01", "BH02", "BH03"],
        "Latitude": [16.0471, 16.0505, 16.0453],
        "Longitude": [108.2067, 108.2109, 108.2155],
        "Depth": [30, 25, 40],
        "Soil Type": ["Clay", "Sand", "Silt"]
    }
    return pd.DataFrame(data)

# Sidebar navigation
st.sidebar.title("Geohole App")
page = st.sidebar.radio("Chọn chức năng", ["Trang chủ", "Bản đồ lỗ khoan", "Chi tiết lỗ khoan", "Xuất dữ liệu"])

data = load_data()

if page == "Trang chủ":
    st.title("Tổng quan dự án địa chất")
    st.write("### Số lượng lỗ khoan: ", len(data))
    
    fig, ax = plt.subplots()
    data.groupby("Soil Type").size().plot(kind="bar", ax=ax)
    ax.set_title("Phân loại đất")
    st.pyplot(fig)

elif page == "Bản đồ lỗ khoan":
    st.title("Bản đồ lỗ khoan")
    m = folium.Map(location=[16.05, 108.21], zoom_start=14)
    for _, row in data.iterrows():
        folium.Marker([row["Latitude"], row["Longitude"]],
                      popup=f"Lỗ khoan: {row['ID']}\nĐộ sâu: {row['Depth']}m\nLoại đất: {row['Soil Type']}").add_to(m)
    st_folium(m, width=700, height=500)

elif page == "Chi tiết lỗ khoan":
    st.title("Chi tiết lỗ khoan")
    selected_id = st.selectbox("Chọn lỗ khoan", data["ID"])
    borehole = data[data["ID"] == selected_id].iloc[0]
    st.write(f"**Tọa độ**: {borehole['Latitude']}, {borehole['Longitude']}")
    st.write(f"**Độ sâu**: {borehole['Depth']}m")
    st.write(f"**Loại đất**: {borehole['Soil Type']}")

elif page == "Xuất dữ liệu":
    st.title("Xuất dữ liệu")
    csv = data.to_csv(index=False).encode('utf-8')
    st.download_button("Tải xuống CSV", csv, "boreholes.csv", "text/csv")
    excel = data.to_excel(index=False, engine='xlsxwriter')
    st.download_button("Tải xuống Excel", excel, "boreholes.xlsx")
