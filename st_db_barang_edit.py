import streamlit as st
import mysql.connector  #fungsi koneksi mysql
import st_db_barang_koneksi #file koneksi db

def edit():
    #buka koneksi server
    conn = st_db_barang_koneksi.koneksi()

    st.info ('EDIT DATA BARANG')
    kode = st.text_input    ('KODE BARANG')
    nama = st.text_input    ('NAMA BARANG')
    satuan = st.selectbox   ('SATUAN', ['PCS','DUS','KG','RENCENG'])
    stok = st.number_input  ('STOK BARANG',0)

    #Tombol
    cek=st.button ('UPDATE DATA')
    if (cek):
        #Cek kode belum di input
        if (kode == ''):
            st.error ('KODE BARANG BELUM DI INPUT')
        else:
            #Cek apakah kode double, jika double beri PESAN
            sql = "select * from barang where kode_barang = '%s'" % kode
            mycursor = conn.cursor()    #SIAPKAN SQL
            mycursor.execute(sql)       #jalankan sql
            dataku = mycursor.fetchall() #ambil datanya

            #cek data, jika NOL = kode salah
            ada = (len(dataku))
            if (ada == 0):
                st.error ('KODE SUDAH ADA, SAVE DI BATALKAN')

            else:
                #SQL UPDATE, pake PARAMETER = %s (harus huruf %s)
                dt = (nama,stok,satuan,kode)
                sql = "update barang set \
                    nama_barang = %s \
                    ,stok = %s \
                    ,satuan = %s \
                    WHERE kode_barang = %s " 

                mycursor = conn.cursor()    #siapkan aql
                mycursor.execute(sql, dt)   #run sql
                conn.commit()               #data save
                conn.close()                #tutup koneksi

                st.header ('Data telah di update')
                st.snow()