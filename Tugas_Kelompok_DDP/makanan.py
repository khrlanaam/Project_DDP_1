import streamlit as st

def hitung_makanan(jenis_makanan):
    # Daftar harga makanan
    harga_makanan = {
        "Burger": 15000,
        "Nasi Goreng": 13000,
        "Mie Ayam": 12000,
    }
    return harga_makanan[jenis_makanan]

def main():
    st.subheader("Aplikasi Pemesanan Makanan Online")
    # Tampilkan daftar harga makanan
    st.write("**Daftar Harga Makanan:**")
    st.write("""
    - Burger: Rp 15,000
    - Nasi Goreng: Rp 13,000
    - Mie Ayam: Rp 12,000
    """)

    # Input pemilihan makanan
    jenis_makanan = st.selectbox("Pilih makanan:", ["Burger", "Nasi Goreng", "Mie Ayam"])
    
    # Hitung biaya total
    if st.button("Hitung Biaya"):
        total = hitung_makanan(jenis_makanan)
        st.success(f"Total biaya makanan: Rp {total:,}")
    else:
        st.info("Silakan pilih makanan dan tekan tombol untuk menghitung biaya.")

if __name__ == "__main__":
    main()
