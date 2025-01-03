import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
@st.cache_data
def load_data():
    # Ganti dengan path file Anda jika berbeda
    data = pd.read_csv('Dashboard/alldata.csv')
    return data

# Fungsi utama Streamlit
def main():
    st.title("Dashboard Analisis Data Rental Sepeda")
    st.write(
        """
        Dashboard ini menyediakan analisis data rental sepeda dengan fitur interaktif 
        seperti filtering dan visualisasi data.
        """
    )
    
    # Load data
    data = load_data()

    # Sidebar untuk Filtering
    st.sidebar.header("Filter Data")
    
    # Filter Season
    season = st.sidebar.multiselect(
        "Pilih Season (Musim):",
        options=data['season_x'].unique(),
        default=data['season_x'].unique()
    )

    # Filter Weekday
    weekday = st.sidebar.multiselect(
        "Pilih Weekday (Hari):",
        options=data['weekday_x'].unique(),
        default=data['weekday_x'].unique()
    )

    # Filter Hour
    hour = st.sidebar.slider(
        "Pilih Rentang Jam:",
        min_value=int(data['hour'].min()),
        max_value=int(data['hour'].max()),
        value=(int(data['hour'].min()), int(data['hour'].max()))
    )

    # Filter Workingday
    workingday = st.sidebar.radio(
        "Pilih Status Hari Kerja:",
        options=["Semua", "Hari Kerja", "Bukan Hari Kerja"],
        index=0
    )

    # Filter berdasarkan opsi
    filtered_data = data[
        (data['season_x'].isin(season)) &
        (data['weekday_x'].isin(weekday)) &
        (data['hour'].between(hour[0], hour[1]))
    ]
    
    if workingday == "Hari Kerja":
        filtered_data = filtered_data[filtered_data['workingday_x'] == 1]
    elif workingday == "Bukan Hari Kerja":
        filtered_data = filtered_data[filtered_data['workingday_x'] == 0]

    # Menampilkan Data yang Difilter
    st.subheader("Data yang Difilter")
    st.write(f"Jumlah Data: {len(filtered_data)} baris")
    st.dataframe(filtered_data)

    # Statistik Ringkas
    st.subheader("Statistik Ringkas")
    st.write(filtered_data.describe())

    # Visualisasi
    st.subheader("Visualisasi Data")

    # Total Rentals berdasarkan jam
    st.write("Total Rentals berdasarkan Jam")
    rentals_by_hour = filtered_data.groupby('hour')['total_rental_x'].sum()
    fig, ax = plt.subplots()
    rentals_by_hour.plot(kind='bar', color='skyblue', ax=ax)
    ax.set_xlabel("Jam")
    ax.set_ylabel("Total Rentals")
    ax.set_title("Total Rentals per Jam")
    st.pyplot(fig)

    # Grafik Garis: Total Rentals berdasarkan Hari
    st.write("Total Rentals berdasarkan Hari")
    rentals_by_weekday = filtered_data.groupby('weekday_x')['total_rental_x'].sum()
    fig, ax = plt.subplots()
    rentals_by_weekday.plot(kind='line', marker='o', color='green', ax=ax)
    ax.set_xlabel("Hari")
    ax.set_ylabel("Total Rentals")
    ax.set_title("Total Rentals per Hari")
    st.pyplot(fig)


if __name__ == "__main__":
    main()
