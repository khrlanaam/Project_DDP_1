import streamlit as st
import transportasi
import makanan
import antar_jemput
import cleaning_service
import bengkel

def main():
    st.title("Aplikasi Layanan Masyarakat")
    st.sidebar.title("Pilih Layanan")
    
    menu = ["Transportasi Online", "Beli Makanan Online", "Jasa Antar Jemput Barang", "Jasa Cleaning Service", "Jasa Bengkel"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Transportasi Online":
        transportasi.main()
    elif choice == "Beli Makanan Online":
        makanan.main()
    elif choice == "Jasa Antar Jemput Barang":
        antar_jemput.main()
    elif choice == "Jasa Cleaning Service":
        cleaning_service.main()
    elif choice == "Jasa Bengkel":
        bengkel.main()
    else:
        st.write("Pilih layanan dari menu di sebelah kiri!")

if __name__ == "__main__":
    main()
