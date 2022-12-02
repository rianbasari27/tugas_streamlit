import streamlit as st
import mysql.connector
import db_connection


def delete():
    # buka koneksi server
    conn = db_connection.koneksi()

    st.info('HAPUS DATA')
    kode = st.text_input('INPUT KODE BARANG YANG AKAN DI HAPUS')

    # tombol
    cek = st.button('DELETE DATA')
    if (cek):

        # cek kode sudah diinput
        if (kode == ''):
            st.error('KODE BARANG BELUM DI INPUT')

        else:
            # cek apakah kode ada
            sql = "select * from barang where kode_barang = '%s'" % kode
            mycursor = conn.cursor()  # siapkan sql
            mycursor.execute(sql)  # jalankan sql
            dataku = mycursor.fetchall()  # ambil datanya

        # cek data jika nol = kode salah
        ada = (len(dataku))
        if (ada == 0):
            st.header('KODE SALAH')

        else:
            # sql hapus data
            # pake parameter - %s (harus huruf %s)
            sql = "DELETE FROM barang WHERE kode_barang = '%s'" % kode
            mycursor = conn.cursor()  # siapkan sql
            mycursor.execute(sql, kode)  # jalankan sql
            conn.commit()  # save transaksi
            conn.close()  # tutup koneksi db

            st.header('Data telah di hapus')
            st.snow()
