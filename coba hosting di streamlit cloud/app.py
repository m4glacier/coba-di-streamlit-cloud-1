import streamlit as st
import os

# Konfigurasi halaman
st.set_page_config(page_title="Simulasi Panel X-Ray", layout="wide")

st.title("Panel Kontrol Simulasi Pesawat Roentgen")

# Parameter awal
kv = st.number_input("Tegangan (kV)", 40, 120, 60)
ma = st.number_input("Arus (mA)", 10, 300, 50)
sec = st.number_input("Waktu (detik)", 1, 10, 1)
status = st.radio("Status", ["OFF", "PRE", "ON"])

# Menampilkan iframe ke index.html
status_kode = "x" if status == "OFF" else "p" if status == "PRE" else "e"

url = f"web/index.html?kode={status_kode}&kv={kv}&mA={ma}&Sec={sec}"

st.markdown("---")
st.subheader("Simulasi Pesawat Roentgen")
st.components.v1.iframe(src=url, height=800, scrolling=True)
