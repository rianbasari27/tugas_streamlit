import streamlit as st
import laporan.view_barang as view_barang
import tambah
import edit
import delete
import laporan.print_pdf as print_pdf
import transaksi.input_stok as input_stok
import laporan.barang_masuk as barang_masuk

def menu_home():
    st.image('img/gudang.jpg')
    st.header('PROGRAM GUDANG STOK MASUK')
    st.subheader('Dengan Python Framework Streamlit')

def menu_input():
    tambah.tambah()  

def menu_edit():
    edit.edit()

def menu_delete():
    delete.delete()

def menu_stok_barang():
    view_barang.lihat()

def menu_input_stok():
    input_stok.tambah()

def menu_hapus_stok():
    input_stok.hapus()

def menu_stok_masuk():
    barang_masuk.lihat()

def menu_print_pdf():
    print_pdf.print_pdf()


# -----------HALAMAN PROGRAMMER------------------#
def menu_programmer():
    st.info('INFO PROGRAMMER')
    st.image('img/kelompok4.jpg')
    st.write('Di buat oleh Kelompok 5 (Tipe A)')
    st.write('1. Dafit Syahrul Dharmawan (NIM : 200441180037)')
    st.write('2. M. Rian Basari (NIM : 200441180007)')
    st.write('3. Syuja Fadhlurrahman (NIM : 200441180044)')


# ----------MENU SIDEBAR---------------#
def menu():
    with st.sidebar:
        pilih = st.selectbox('Menu barang',
                             ['Home', 'Programmer', 'Input data','Edit data',
                              'Delete data','-------Transaksi-------','Input stok masuk',
                              'Hapus stok masuk','-------Laporan-------','Lihat Stok Barang',
                              'Print Stok Barang PDF','Lihat stok masuk'])
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
    elif (pilih == '-------Transaksi-------' or pilih == 'Input stok masuk'):
        menu_input_stok()
    elif (pilih == 'Hapus stok masuk'):
        menu_hapus_stok()
    elif (pilih == '-------Laporan-------' or pilih == 'Lihat Stok Barang'):
        menu_stok_barang()
    elif (pilih == 'Print Stok Barang PDF'):
        menu_print_pdf()
    elif (pilih == 'Lihat stok masuk'):
        menu_stok_masuk()
    else:
        menu_print_pdf()


def main():
    menu()


if __name__ == '__main__':
    main()
