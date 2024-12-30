import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Judul Aplikasi
st.title("Dashboard Analisis Data Rental Sepeda")

# Load Dataset
uploaded_file = st.file_uploader("Unggah dataset CSV", type="csv")
if uploaded_file is not None:
    # Membaca dataset
    df = pd.read_csv(uploaded_file)

    # Menampilkan beberapa baris data
    st.subheader("Tampilan Data")
    st.dataframe(df.head())

    # --- PREPROCESSING ---
    # Pastikan kolom datetime diubah ke format datetime
    df['datetime_x'] = pd.to_datetime(df['datetime_x'])
    
    # --- RFM ANALYSIS ---
    st.subheader("RFM Analysis")

    # Menghitung Recency
    terakhir_sewa = df['datetime_x'].max()
    df['Recency'] = (terakhir_sewa - df['datetime_x']).dt.days

    # Menghitung Frequency
    df['Frequency'] = df['casual_x'] + df['registered_x']

    # Menghitung Monetary
    df['Monetary'] = df['total_rental_x']

    # Menampilkan RFM Summary
    rfm_summary = df[['Recency', 'Frequency', 'Monetary']].describe()
    st.write("Ringkasan RFM:")
    st.dataframe(rfm_summary)

    # Visualisasi RFM
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    sns.histplot(df['Recency'], bins=20, kde=True, ax=axes[0], color='blue')
    axes[0].set_title('Distribusi Recency')
    sns.histplot(df['Frequency'], bins=20, kde=True, ax=axes[1], color='green')
    axes[1].set_title('Distribusi Frequency')
    sns.histplot(df['Monetary'], bins=20, kde=True, ax=axes[2], color='red')
    axes[2].set_title('Distribusi Monetary')
    st.pyplot(fig)

    # --- CLUSTERING (MANUAL BINNING) ---
    st.subheader("Clustering (Manual Binning)")

    # Klaster berdasarkan Jam (hour)
    def time_period(hour):
        if 0 <= hour < 6:
            return 'Malam'
        elif 6 <= hour < 12:
            return 'Pagi'
        elif 12 <= hour < 18:
            return 'Siang'
        else:
            return 'Sore'

    df['Time Period'] = df['hour'].apply(time_period)

    # Visualisasi distribusi klaster waktu
    time_group = df.groupby('Time Period')['total_rental_x'].mean().reset_index()
    st.write("Rata-rata Rental Berdasarkan Periode Waktu")
    st.dataframe(time_group)

    # Plot
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.barplot(data=time_group, x='Time Period', y='total_rental_x', palette='viridis', ax=ax)
    ax.set_title('Rata-rata Rental Sepeda Berdasarkan Periode Waktu')
    ax.set_ylabel('Rata-rata Total Rental')
    ax.set_xlabel('Periode Waktu')
    st.pyplot(fig)

    # --- VISUALISASI TAMBAHAN ---
    st.subheader("Visualisasi Tambahan")

    # Grafik jumlah rental berdasarkan hari dalam seminggu
    weekday_group = df.groupby('weekday_x')['total_rental_x'].mean().reset_index()
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.barplot(data=weekday_group, x='weekday_x', y='total_rental_x', palette='coolwarm', ax=ax)
    ax.set_title('Rata-rata Rental Sepeda Berdasarkan Hari dalam Seminggu')
    ax.set_ylabel('Rata-rata Total Rental')
    ax.set_xlabel('Hari dalam Minggu')
    st.pyplot(fig)

    # Grafik heatmap hubungan variabel
    st.write("Heatmap Korelasi")
    correlation = df[['temp_x', 'humidity_x', 'windspeed_x', 'casual_x', 'registered_x', 'total_rental_x']].corr()
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(correlation, annot=True, cmap='coolwarm', ax=ax)
    st.pyplot(fig)

else:
    st.write("Silakan unggah file dataset untuk memulai analisis.")
