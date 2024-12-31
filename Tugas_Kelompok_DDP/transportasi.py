import streamlit as st

def hitung_transportasi(jenis, jarak):
    tarif = 5000 if jenis == "motor" else 8000
    return tarif * jarak

def main():
    st.subheader("Transportasi Online")
    jenis = st.radio("Pilih jenis transportasi:", ["motor", "mobil"])
    jarak = st.number_input("Masukkan jarak (KM):", min_value=0.0, step=0.1)
    
    if st.button("Hitung Biaya"):
        total = hitung_transportasi(jenis, jarak)
        st.success(f"Total biaya transportasi: Rp.{total:,}")
    else:
        st.info("Silakan pilih jenis transportasi dan masukkan jarak untuk menghitung biaya.")

if __name__ == "__main__":
    main()
