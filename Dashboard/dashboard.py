import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
DATA_URL = 'data/alldata.csv'
data = pd.read_csv(DATA_URL)

# filtering
season_mapping = {1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'}
data['season_x'] = data['season_x'].map(season_mapping)
data['season_y'] = data['season_y'].map(season_mapping)
weekday_mapping = {
    0: 'Sunday', 1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday'
}
data['weekday_x'] = data['weekday_x'].map(weekday_mapping)
data['weekday_y'] = data['weekday_y'].map(weekday_mapping)

# Set up Streamlit app
st.title("Bike Usage Dashboard")
st.sidebar.header("Filter Options")

# Opsi Filtering
filter_season = st.sidebar.multiselect(
    "Select Season:", options=data['season_x'].unique(), default=data['season_x'].unique()
)
filter_weekday = st.sidebar.multiselect(
    "Select Weekday:", options=data['weekday_x'].unique(), default=data['weekday_x'].unique()
)

# Menambahkan Filter
filtered_data = data[(data['season_x'].isin(filter_season)) & (data['weekday_x'].isin(filter_weekday))]

# Pertanyaan 1: Rata rata penggunaan sepeda per season dan hari
st.header("Average Bike Usage Per Day or Season")

average_usage_per_day = filtered_data.groupby('datetime_x')['total_rental_x'].mean()
average_usage_per_season = filtered_data.groupby('season_x')['total_rental_x'].mean()

# Hasil display
view_option = st.radio("Choose a view:", ("Daily", "Seasonal"))
if view_option == "Daily":
    st.line_chart(average_usage_per_day, use_container_width=True)
elif view_option == "Seasonal":
    st.bar_chart(average_usage_per_season, use_container_width=True)

# Pertanyaan 2: Penggunaan sepeda berdasarkan waktu harian
st.header("Bike Usage Pattern By Time of Day")

hourly_pattern = filtered_data.groupby('hour')['total_rental_x'].mean()
plt.figure(figsize=(10, 6))
sns.lineplot(x=hourly_pattern.index, y=hourly_pattern.values, marker='o', color='blue')
plt.title('Average Bike Usage By Hour')
plt.xlabel('Hour of Day')
plt.ylabel('Average Bike Usage')
plt.xticks(range(0, 24))
st.pyplot(plt.gcf())

# Footer
st.write("### Notes")
st.write("- Data is filtered based on the selected season and weekday.")
st.write("- Use the sidebar to customize the filters.")
