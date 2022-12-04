import streamlit as st
import mysql.connector
import db_connection


def delete():
    conn = db_connection.koneksi()

    st.info('HAPUS DATA')
    kode = st.text_input('INPUT KODE BARANG YANG AKAN DI HAPUS')

    cek = st.button('DELETE DATA')
    if (cek):

        if (kode == ''):
            st.error('KODE BARANG BELUM DI INPUT')

        else:
            sql = "select * from barang where kode_barang = '%s'" % kode
            mycursor = conn.cursor() 
            mycursor.execute(sql) 
            dataku = mycursor.fetchall()  

        ada = (len(dataku))
        if (ada == 0):
            st.header('KODE SALAH')

        else:
            sql = "DELETE FROM barang WHERE kode_barang = '%s'" % kode
            mycursor = conn.cursor()
            mycursor.execute(sql, kode)
            conn.commit()
            conn.close()  

            st.header('Data telah di hapus')
            st.snow()
