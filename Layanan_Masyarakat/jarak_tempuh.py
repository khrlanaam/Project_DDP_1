import streamlit as st

def hitung_jarak():
    st.title("Jarak Tempuh")
    st.write("Hitung jarak tempuh berdasarkan kecepatan dan waktu.")

    kecepatan = st.number_input("Masukkan kecepatan (km/jam):", min_value=0.0)
    waktu = st.number_input("Masukkan waktu perjalanan (jam):", min_value=0.0)

    if st.button("Hitung Jarak"):
        jarak = kecepatan * waktu
        st.write(f"Jarak yang ditempuh: {jarak} km")
