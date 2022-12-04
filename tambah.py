import mysql.connector
import streamlit as st

import db_connection


def tambah():
    st.info(' ISI DATA BARANG')
    kode = st.text_input('KODE BARANG')
    nama = st.text_input('NAMA BARANG')
    satuan = st.text_input('SATUAN')
    stok = st.number_input('STOK',0)

    cek = st.button('SAVE')
    if (cek):
        if (kode == ''):
            st.error('KODE BARANG BELUM DI INPUT')

        else:
            conn = db_connection.koneksi()

            sql = "select * from barang where kode_barang = '%s'" % kode
            mycursor = conn.cursor()
            mycursor.execute(sql)
            dataku = mycursor.fetchall()

            ada = (len(dataku))
            if (ada > 0):
                st.error('KODE SUDAH ADA,SAVE DIBATALKAN')

            else:
                sql = "insert into barang (kode_barang, nama_barang, satuan, stok) value (%s, %s, %s, %s)"

            dt = (kode, nama, satuan, stok)

            mycursor = conn.cursor()
            mycursor.execute(sql, dt)
            conn.commit()
            conn.close()

            st.header('data telah di simpan')
            st.balloons()
