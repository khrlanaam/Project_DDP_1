import streamlit as st

def hitung_tarif():
    st.title("Estimasi Tarif")
    st.write("Hitung tarif perjalanan berdasarkan jarak dan jenis kendaraan.")

    jarak = st.number_input("Masukkan jarak tempuh (km):", min_value=0.0)
    kendaraan = st.selectbox("Pilih jenis kendaraan:", ["Motor", "Mobil"])

    if kendaraan == "Motor":
        biaya_per_km = 5000
    elif kendaraan == "Mobil":
        biaya_per_km = 10000

    total_biaya = jarak * biaya_per_km

    if st.button("Hitung Tarif"):
        st.write(f"Total tarif perjalanan: Rp {total_biaya}")
