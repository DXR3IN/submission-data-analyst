import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

def filter_data_by_station(data, station_name):
    filtered_data = data[data['station'] == station_name]
    return filtered_data

all_df = pd.read_csv("all_data.csv")

st.set_option('deprecation.showPyplotGlobalUse', False)

PSRA_Tiantan_df = filter_data_by_station(all_df, "Tiantan")
PSRA_Shunyi_df = filter_data_by_station(all_df, "Shunyi")
PSRA_Wanliu_df = filter_data_by_station(all_df, "Wanliu")

st.title('Submission Analisis Data')

st.subheader('''Apakah ada hubungan antara kondisi cuaca seperti hujan (RAIN) dengan tingkat polutan?''')
with st.expander('Conclusion'):
  st.write('Hujan, Arah angin dan Kecepatan angin sangat mempengaruhi tingkat polusi di Udara, semakin kuat Hujan atau Kecepatan Angin semakin menurun polusi udaranya. Sedangkan dari sisi Arah Angin jika dilihat dari tabel yang didapatkan, NE adalah arah angin yang paling banyak membawa Polusi sedangkan SSW adalah yang paling kecil.')
  

tab1, tab2, tab3, tab4 = st.tabs(['Tiantan', 'Wanliu', 'Shunyi', 'Gabungan Data'])

with tab1:
    st.text('Data Tiantan')
    plt.figure(figsize=(10, 6))
    plt.scatter(PSRA_Tiantan_df['RAIN'], PSRA_Tiantan_df['PM2.5'], alpha=0.5)
    plt.title('Hubungan Antara Hujan dan Tingkat PM2.5 (Tiantan)')
    plt.xlabel('Hujan (mm)')
    plt.ylabel('Tingkat PM2.5 (µg/m³)')
    plt.grid(True)
    st.pyplot()

with tab2:
    st.text('Data Wanliu')
    plt.figure(figsize=(10, 6))
    plt.scatter(PSRA_Wanliu_df['RAIN'], PSRA_Wanliu_df['PM2.5'], alpha=0.5)
    plt.title('Hubungan Antara Hujan dan Tingkat PM2.5 (Wanliu)')
    plt.xlabel('Hujan (mm)')
    plt.ylabel('Tingkat PM2.5 (µg/m³)')
    plt.grid(True)
    st.pyplot()

with tab3:
    st.text('Data Shunyi')
    plt.figure(figsize=(10, 6))
    plt.scatter(PSRA_Shunyi_df['RAIN'], PSRA_Shunyi_df['PM2.5'], alpha=0.5)
    plt.title('Hubungan Antara Hujan dan Tingkat PM2.5 (Shunyi)')
    plt.xlabel('Hujan (mm)')
    plt.ylabel('Tingkat PM2.5 (µg/m³)')
    plt.grid(True)
    st.pyplot()

with tab4:
    st.text('Gabungan Data')
    plt.figure(figsize=(10, 6))
    plt.scatter(all_df['RAIN'], all_df['PM2.5'], alpha=0.5, label='Tiantan')
    plt.title('Hubungan Antara Hujan dan Tingkat PM2.5 (Gabungan)')
    plt.xlabel('Hujan (mm)')
    plt.ylabel('Tingkat PM2.5 (µg/m³)')
    plt.legend()
    plt.grid(True)
    st.pyplot()
    
st.subheader('''Pada tahun berapa polusi udara mencapai puncaknya?''')
with st.expander('Conclusion'):
  st.write('2017 adalah tahun yang paling berpolusi, sedangkan tahun sebelumnya 2016 adalah tahun yang paling bersih dari polusi.')

with st.container():
  yearly_avg_pm25 = all_df.groupby(all_df['year'])['PM2.5'].mean()
  plt.figure(figsize=(10, 6))
  yearly_avg_pm25.plot(color='skyblue', marker='o', linestyle='-')
  plt.title('Rata-rata Tingkat PM2.5 per Tahun')
  plt.xlabel('Tahun')
  plt.ylabel('Rata-rata Tingkat PM2.5 (µg/m³)')
  plt.xticks(rotation=0)
  plt.grid(axis='y')
  st.pyplot()
