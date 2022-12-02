import mysql.connector
import streamlit as st

import db_connection


def tambah():
    st.info(' ISI DATA BARANG')
    kode = st.text_input('KODE BARANG')
    nama = st.text_input('NAMA BARANG')
    satuan = st.text_input('SATUAN')
    stok = st.number_input('STOK',0)

# tombol
    cek = st.button('SAVE')
    if (cek):
        # cek kode belum input
        if (kode == ''):
            st.error('KODE BARANG BELUM DI INPUT')

        else:
            # buka koneksi DB
            conn = db_connection.koneksi()

            # cek apakah kjode double,jika double diberi pesan
            sql = "select * from barang where kode_barang = '%s'" % kode
            mycursor = conn.cursor()  # siapkan sql
            mycursor.execute(sql)  # jalankan sql
            dataku = mycursor.fetchall()  # ambil datanya

            # cek jumlah data
            ada = (len(dataku))
            if (ada > 0):
                st.error('KODE SUDAH ADA,SAVE DIBATALKAN')

            else:
                # tmabah data
                sql = "insert into barang (kode_barang, nama_barang, satuan, stok) value (%s, %s, %s, %s)"

            dt = (kode, nama, satuan, stok)

            mycursor = conn.cursor()  # siapkan sql
            mycursor.execute(sql, dt)  # run sql
            conn.commit()  # data save
            conn.close()  # tutup koneksi

            st.header('data telah di simpan')
            st.balloons()
