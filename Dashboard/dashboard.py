import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
DATA_URL = 'Dashboard/alldata.csv'
data = pd.read_csv(DATA_URL)

# Filtering
season_mapping = {1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'}
data['season_x'] = data['season_x'].map(season_mapping)
data['season_y'] = data['season_y'].map(season_mapping)
weekday_mapping = {
    0: 'Sunday', 1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday'
}
data['weekday_x'] = data['weekday_x'].map(weekday_mapping)
data['weekday_y'] = data['weekday_y'].map(weekday_mapping)

# Set up Streamlit
st.title("Dashboard Penggunaan Sepeda")
st.sidebar.header("Opsi Filter")

# Opsi filter
filter_season = st.sidebar.multiselect(
    "Pilih Season:", options=data['season_x'].unique(), default=data['season_x'].unique()
)
filter_weekday = st.sidebar.multiselect(
    "Pilih Weekday:", options=data['weekday_x'].unique(), default=data['weekday_x'].unique()
)

# Menambahkan Filter
filtered_data = data[(data['season_x'].isin(filter_season)) & (data['weekday_x'].isin(filter_weekday))]

# Question 1: Rata-rata penggunaan sepeda per hari atau musim
st.header("Rata-rata penggunaan sepeda per hari atau musim")

average_usage_per_day = filtered_data.groupby('datetime_x')['total_rental_x'].mean()
average_usage_per_season = filtered_data.groupby('season_x')['total_rental_x'].mean()

# Hasil Display
view_option = st.radio("Pilih tampilan:", ("Daily", "Seasonal"))
if view_option == "Daily":
    st.line_chart(average_usage_per_day, use_container_width=True)
elif view_option == "Seasonal":
    st.bar_chart(average_usage_per_season, use_container_width=True)

# Question 2: Pola Penggunaan Sepeda Berdasarkan Waktu
st.header("Pola Penggunaan Sepeda Berdasarkan Waktu")

hourly_pattern = filtered_data.groupby('hour')['total_rental_x'].mean()
plt.figure(figsize=(10, 6))
sns.lineplot(x=hourly_pattern.index, y=hourly_pattern.values, marker='o', color='blue')
plt.title('Average Bike Usage By Hour')
plt.xlabel('Hour of Day')
plt.ylabel('Average Bike Usage')
plt.xticks(range(0, 24))
st.pyplot(plt.gcf())
