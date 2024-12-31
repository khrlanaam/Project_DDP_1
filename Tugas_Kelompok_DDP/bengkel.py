import streamlit as st

def hitung_bengkel(layanan, jarak):
    harga_layanan = {
        "tambal ban": 25000,
        "mekanik mesin": 200000,
        "derek mobil": 50000
    }
    return harga_layanan[layanan] + (5000 * jarak)

def main():
    st.write("""
    - Tambal Ban: Rp 25,000
    - Mekanik Mesin: Rp 200,000
    - Derek Mobil: Rp 50,000
    """)
    st.subheader("Jasa Bengkel/Montir Online")
    layanan = st.selectbox("Pilih layanan:", ["tambal ban", "mekanik mesin", "derek mobil"])
    jarak = st.number_input("Masukkan jarak (KM):", min_value=0.0, step=0.1)
    
    if st.button("Hitung Biaya"):
        total = hitung_bengkel(layanan, jarak)
        st.success(f"Total biaya bengkel: Rp.{total:,}")
    else:
        st.info("Silakan pilih layanan dan masukkan jarak untuk menghitung biaya.")

if __name__ == "__main__":
    main()
