import streamlit as st
from jarak_tempuh import hitung_jarak
from estimasi_tarif import hitung_tarif
from waktu_tempuh import hitung_waktu
from cek_rute import cek_rute
from kendaraan import detail_kendaraan

def main():
    st.sidebar.title("Aplikasi Transportasi Sederhana")
    menu = st.sidebar.radio("Pilih Menu:", ["Jarak Tempuh", "Estimasi Tarif", "Estimasi Waktu", "Cek Rute", "Detail Kendaraan"])

    if menu == "Jarak Tempuh":
        hitung_jarak()
    elif menu == "Estimasi Tarif":
        hitung_tarif()
    elif menu == "Estimasi Waktu":
        hitung_waktu()
    elif menu == "Cek Rute":
        cek_rute()
    elif menu == "Detail Kendaraan":
        detail_kendaraan()

if __name__ == "__main__":
    main()
