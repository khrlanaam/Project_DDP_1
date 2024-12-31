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
    st.write("""
    - Kamar Mandi: Rp 30,000
    - Kamar Tidur: Rp 25,000
    - Kebun: Rp 75,000
    - Full Service: Rp 110,000
    """)
    st.subheader("Jasa Cleaning Service Online")
    layanan = st.selectbox("Pilih layanan:", ["kamar mandi", "kamar", "kebun", "full service"])
    jarak = st.number_input("Masukkan jarak (KM):", min_value=0.0, step=0.1)
    
    if st.button("Hitung Biaya"):
        total = hitung_cleaning_service(layanan, jarak)
        st.success(f"Total biaya cleaning service: Rp.{total:,}")
    else:
        st.info("Silakan pilih layanan dan masukkan jarak untuk menghitung biaya.")

if __name__ == "__main__":
    main()
