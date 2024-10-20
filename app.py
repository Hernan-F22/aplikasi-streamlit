import streamlit as st
import pandas as pd

# Judul dan Deskripsi
st.title('Aplikasi Edukasi sederhana')
st.write('Ini adalah aplikasi edukasi interaktif dengan streamlit!')

# Input Data dari User
nama = st.text_input('Masukan Nama:')
umur = st.number_input('Masukan Umur:', min_value=1, max_value=100)

# Tampilkan Data Input
if st.button('Submit'):
    st.write(f'Selamat Datang, {nama}! Usia kamu {umur} tahun.')

# Grafik Sederhana
st.subheader('Grafik Contoh')
data = {'Kategori': ['A','B','C'], 'Nilai': [10, 20, 30]}
st.bar_chart(data)

pilihan = st.selectbox("Pilih matakuliah:", ["Mobile Programming", "Komputerisasi", "Manajemen Proyek"])

data = pd.DataFrame({"Nama": ["A", "B"], "Nilai": [85, 90]})
st.dataframe(data)
