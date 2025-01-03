import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
@st.cache_data
def load_data():
    file_path = "Dashboard/alldata.csv" 
    data = pd.read_csv(file_path)
    data['datetime_x'] = pd.to_datetime(data['datetime_x'])
    data['datetime_y'] = pd.to_datetime(data['datetime_y'])
    return data

data = load_data()

# Map nama kategori untuk season
SEASON_MAP = {1: "Spring", 2: "Summer", 3: "Fall", 4: "Winter"}
data['season_name_x'] = data['season_x'].map(SEASON_MAP)
data['season_name_y'] = data['season_y'].map(SEASON_MAP)

# Judul dan deskripsi aplikasi
st.title("Analisis Penggunaan Sepeda")
st.markdown(
    """
    **Aplikasi ini menjawab dua pertanyaan bisnis utama:**
    1. Berapa rata-rata penggunaan sepeda per hari atau per musim?
    2. Bagaimana pola penggunaan sepeda berdasarkan waktu harian?
    """
)

# Sidebar untuk filter
st.sidebar.header("Filter Data")
selected_season = st.sidebar.multiselect(
    "Pilih Musim:",
    options=data['season_name_x'].unique(),
    default=data['season_name_x'].unique()
)
selected_year = st.sidebar.multiselect(
    "Pilih Tahun:",
    options=data['year_x'].unique(),
    default=data['year_x'].unique()
)

# Filter data berdasarkan pilihan pengguna
filtered_data = data[
    (data['season_name_x'].isin(selected_season)) &
    (data['year_x'].isin(selected_year))
]

# Rata-rata penggunaan sepeda per musim
st.subheader("Rata-rata Penggunaan Sepeda Per Hari atau Per Musim")
avg_by_season = (
    filtered_data.groupby('season_name_x')['total_rental_x']
    .mean()
    .reset_index()
    .rename(columns={"season_name_x": "Musim", "total_rental_x": "Rata-rata Penyewaan"})
)

st.table(avg_by_season)

# Pola penggunaan sepeda berdasarkan waktu harian
st.subheader("Pola Penggunaan Sepeda Berdasarkan Waktu Harian")
hourly_pattern = filtered_data.groupby('hour')['total_rental_y'].mean().reset_index()
plt.figure(figsize=(10, 5))
sns.lineplot(data=hourly_pattern, x='hour', y='total_rental_y')
plt.title("Pola Penyewaan Sepeda Berdasarkan Jam")
plt.xlabel("Jam")
plt.ylabel("Rata-rata Penyewaan")
st.pyplot(plt)

# Informasi tambahan
st.markdown("Data yang ditampilkan adalah hasil dari filter yang Anda pilih.")
