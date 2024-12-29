import streamlit as st

def hitung_cleaning_service(layanan, jarak):
    harga_layanan = {
        "kamar mandi": 30000,
        "kamar": 25000,
        "kebun": 75000,
        "full service": 110000
    }
    return harga_layanan[layanan] + (5000 * jarak)

def main():
    st.subheader("Jasa Cleaning Service Online")
    layanan = st.selectbox("Pilih layanan:", ["kamar mandi", "kamar", "kebun", "full service"])
    jarak = st.number_input("Masukkan jarak (KM):", min_value=0.0, step=0.1)
    
    if st.button("Hitung Biaya"):
        total = hitung_cleaning_service(layanan, jarak)
        st.success(f"Total biaya cleaning service: Rp.{total:,}")
