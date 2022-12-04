import streamlit as st
import mysql.connector 
import db_connection 

def edit():
    conn = db_connection.koneksi()

    st.info ('EDIT DATA BARANG')
    kode = st.text_input    ('KODE BARANG')
    nama = st.text_input    ('NAMA BARANG')
    satuan = st.selectbox   ('SATUAN', ['PCS','DUS','KG','RENCENG'])
    stok = st.number_input  ('STOK BARANG',0)

    cek=st.button ('UPDATE DATA')
    if (cek):
        if (kode == ''):
            st.error ('KODE BARANG BELUM DI INPUT')
        else:
            sql = "select * from barang where kode_barang = '%s'" % kode
            mycursor = conn.cursor()
            mycursor.execute(sql)
            dataku = mycursor.fetchall()

            ada = (len(dataku))
            if (ada == 0):
                st.error ('BARANG TIDAK ADA!')

            else:
                dt = (nama,stok,satuan,kode)
                sql = "update barang set \
                    nama_barang = %s \
                    ,stok = %s \
                    ,satuan = %s \
                    WHERE kode_barang = %s " 

                mycursor = conn.cursor()
                mycursor.execute(sql, dt)
                conn.commit()
                conn.close()

                st.header ('Data telah di update')
                st.snow()