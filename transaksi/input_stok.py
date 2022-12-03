import mysql.connector
import streamlit as st
import db_connection


def tambah():
    conn = db_connection.koneksi()

    query = "select * from barang"
    mycursor = conn.cursor()  
    mycursor.execute(query)  
    data = mycursor.fetchall()

    st.info('INPUT STOK BARANG')
    noVoucher = st.text_input('No. Voucher')
    tanggal = st.date_input('Tanggal Masuk')
    optionBarang = [row[1] for row in data]
    namaBarang = st.selectbox('Nama Barang', optionBarang)
    jumlah = st.number_input('Jumlah',0)


    save = st.button('SAVE')
    if (save):
        if (noVoucher == ''):
            st.error('NOMOR VOUCHER BELUM DI INPUT')

        else:
            conn = db_connection.koneksi()

            sql = "select * from barang_masuk where NO_VOUCHER = '%s'" % noVoucher
            mycursor = conn.cursor()  
            mycursor.execute(sql)  
            dataku = mycursor.fetchall()  

            # cek jumlah data
            ada = (len(dataku))
            if (ada > 0):
                st.error('KODE SUDAH ADA,SAVE DIBATALKAN')

            else:
                # tmabah data
                sql = "insert into barang_masuk (NO_VOUCHER, TGL, KODE_BARANG, JUMLAH) value (%s, %s, %s, %s)"

            dt = (noVoucher, tanggal, namaBarang, jumlah)

            mycursor = conn.cursor()  # siapkan sql
            mycursor.execute(sql, dt)  # run sql
            conn.commit()  # data save
            conn.close()  # tutup koneksi

            st.header('data telah di simpan')
            st.balloons()

def hapus():
    conn = db_connection.koneksi()

    st.info('HAPUS STOK DATA')
    kode = st.text_input('MASUKAN NOMOR VOUCHER YANG AKAN DIHAPUS')

    cek = st.button('DELETE DATA')
    if (cek):

        if (kode == ''):
            st.error('NOMOR VOUCHER BELUM DI INPUT')

        else:
            query = "select * from barang_masuk where NO_VOUCHER = '%s'" % kode
            mycursor = conn.cursor() 
            mycursor.execute(query) 
            data = mycursor.fetchall()

        ada = (len(data))
        if (ada == 0):
            st.header('KODE TIDAK VALID')

        else:
            query = "DELETE FROM barang_masuk WHERE NO_VOUCHER = '%s'" % kode
            mycursor = conn.cursor() 
            mycursor.execute(query, kode)
            conn.commit()
            conn.close()

            st.header('Data telah di hapus')
            st.snow()
