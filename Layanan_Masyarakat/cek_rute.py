import streamlit as st

def cek_rute():
    st.title("Cek Rute")
    st.write("Simulasi rute perjalanan berdasarkan checkpoint.")

    jumlah_checkpoint = st.number_input("Masukkan jumlah checkpoint:", min_value=1, step=1)
    daftar_checkpoint = []

    for titik in range(1, jumlah_checkpoint + 1):
        daftar_checkpoint.append(f"Checkpoint {titik} berhasil dilewati.")

    if st.button("Mulai Cek Rute"):
        st.write("Rute perjalanan:")
        for checkpoint in daftar_checkpoint:
            st.write(checkpoint)
