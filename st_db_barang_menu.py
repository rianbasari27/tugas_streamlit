# menu utama

import streamlit as st
import st_db_barang_lihat
import st_db_barang_tambah
import st_db_barang_edit
import st_db_barang_delete
import st_db_barang_pdf
# from PIL import Image



# ambil koneksi


def menu_home():
    st.image('img/gudang.jpg')
    st.header('PROGRAM GUDANG STOK MASUK')
    st.subheader('Dengan Python Framework Streamlit')

# file crud #


def menu_input():
    st_db_barang_tambah.tambah()  # panggil file & function

def menu_edit():
    st_db_barang_edit.edit()


def menu_delete():
    st_db_barang_delete.delete()


def menu_lihat():
    st_db_barang_lihat.lihat()

def menu_print_pdf():
    st_db_barang_pdf.print_pdf()

# -----------HALAMAN PROGRAMMER------------------#


def menu_programmer():
    st.info('INFO PROGRAMMER')
    st.image('img/kelompok4.jpg')
    st.write('Di buat oleh Kelompok 5 (Tipe A)')
    st.write('1. Dafit Syahrul Dharmawan (NIM : 200441180037)')
    st.write('2. M. Rian Basari (NIM : 200441180007)')
    st.write('3. Syuja Fadhlurrahman (NIM : 200441180044)')
# ----------UTAMA,MENU SIDEBAR---------------#


def menu():
    with st.sidebar:
        pilih = st.selectbox('Menu barang',
                             ['Home', 'Programmer', 'Input data','Edit data',
                              'Delete data','-------Transaksi-------','input stok masuk',
                              'hapus stok masuk','-------Laporan-------','Lihat Stok Barang',
                              'Print Stok Barang PDF','lihat stok masuk'])
    if (pilih == 'Home'):
        menu_home()
    elif (pilih == 'Programmer'):
        menu_programmer()
    elif (pilih == 'Input data'):
        menu_input()
    elif(pilih == 'Edit data'):
        menu_edit()
    elif (pilih == 'Delete data'):
        menu_delete()
    elif (pilih == 'Lihat Stok Barang'):
        menu_lihat()
    else:
        menu_print_pdf()


def main():
    menu()


if __name__ == '__main__':
    main()
