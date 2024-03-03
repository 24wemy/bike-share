import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

def load_data(filename):
    df = pd.read_csv(filename)

    datetime_columns = ["datetimes"]

    df.sort_values(by="datetimes", inplace=True)
    df.reset_index(inplace=True)

    for column in datetime_columns:
        df[column] = pd.to_datetime(df[column])

    return df

def main():
    st.title("Dashboard Data Bike Share")
    data = load_data("all_data.csv")

    st.sidebar.title("Profile")

    st.sidebar.write("Nama: Ogi Wemy Corinta")
    st.sidebar.write("Deskripsi: Bangkit Accademy - Machine Learning")

    st.sidebar.subheader("Sosial Media")
    st.sidebar.write("LinkedIn: [Ogi Wemy Corinta](https://www.linkedin.com/in/ogi-wemy-corinta-045767261/)")
    st.sidebar.write("GitHub: [Ogi Wemy](https://github.com/24wemy)")

    st.subheader("Informasi DataFrame:")
    st.write(data.info())

    st.subheader("Data Teratas:")
    st.write(data.head())

    st.subheader("Visualisasi Data:")

    daily_total_count = data.groupby(data["datetimes"].dt.date)["total_Count"].sum()
    st.line_chart(daily_total_count)

    st.subheader("Distribusi Suhu:")
    fig, ax = plt.subplots()
    sns.histplot(data["temp"], kde=True, ax=ax)
    st.pyplot(fig)

    st.subheader("Statistik Deskriptif:")
    st.write(data.describe())


    st.sidebar.subheader("Filter Tanggal")
    date_range = st.sidebar.date_input("Pilih Rentang Tanggal:", [data["datetimes"].min().date(), data["datetimes"].max().date()])

    start_date = pd.to_datetime(date_range[0])
    end_date = pd.to_datetime(date_range[1])

    filtered_data = data[(data["datetimes"] >= start_date) & (data["datetimes"] <= end_date)]

    st.subheader("Data setelah difilter:")
    st.write(filtered_data.head())

    selected_columns = st.multiselect("Pilih Kolom untuk divisualisasikan:", data.columns)
    if selected_columns:
        st.subheader("Visualisasi Kolom yang Dipilih:")
        st.line_chart(filtered_data[selected_columns])

if __name__ == "__main__":
    main()
