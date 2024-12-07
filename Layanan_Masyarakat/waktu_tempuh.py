import streamlit as st

def hitung_waktu():
    st.title("Estimasi Waktu Tempuh")
    st.write("Hitung waktu perjalanan berdasarkan jarak dan kecepatan.")

    jarak = st.number_input("Masukkan jarak tempuh (km):", min_value=0.0)
    kecepatan = st.number_input("Masukkan kecepatan rata-rata (km/jam):", min_value=0.1)

    if st.button("Hitung Waktu"):
        waktu_tempuh = jarak / kecepatan
        for jam in range(1, int(waktu_tempuh) + 1):
            st.write(f"Jam ke-{jam}: Perjalanan masih berlangsung...")
        st.write(f"Waktu total perjalanan: {waktu_tempuh:.2f} jam")
