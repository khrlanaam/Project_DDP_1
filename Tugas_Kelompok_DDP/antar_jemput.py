import streamlit as st

def hitung_antar_jemput(berat, jarak):
    return (3000 * berat) + (5000 * jarak)

def main():
    st.subheader("Jasa Antar Jemput Barang")
    berat = st.number_input("Masukkan berat barang (KG):", min_value=0.0, step=0.1)
    jarak = st.number_input("Masukkan jarak (KM):", min_value=0.0, step=0.1)
    
    if st.button("Hitung Biaya"):
        total = hitung_antar_jemput(berat, jarak)
        st.success(f"Total biaya antar jemput barang: Rp.{total:,}")
    else:
        st.info("Silakan masukkan data dan tekan tombol Hitung Biaya untuk mengetahui total biaya.")

if __name__ == "__main__":
    main()
