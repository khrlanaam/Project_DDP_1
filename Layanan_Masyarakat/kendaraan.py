import streamlit as st

class Kendaraan:
    def __init__(self, jenis_kendaraan, tarif_per_km):
        self.jenis_kendaraan = jenis_kendaraan
        self.tarif_per_km = tarif_per_km

    def hitung_tarif_total(self, jarak_tempuh):
        return self.tarif_per_km * jarak_tempuh

def detail_kendaraan():
    st.title("Detail Kendaraan")
    st.write("Lihat tarif kendaraan berdasarkan jenis.")

    jenis_kendaraan = st.selectbox("Pilih jenis kendaraan:", ["Motor", "Mobil"])
    jarak_tempuh = st.number_input("Masukkan jarak tempuh (km):", min_value=0.0)

    kendaraan = Kendaraan(jenis_kendaraan, 5000 if jenis_kendaraan == "Motor" else 10000)
    total_tarif = kendaraan.hitung_tarif_total(jarak_tempuh)

    st.write(f"Jenis kendaraan: {kendaraan.jenis_kendaraan}")
    st.write(f"Tarif per km: Rp {kendaraan.tarif_per_km}")
    st.write(f"Estimasi tarif total: Rp {total_tarif}")
