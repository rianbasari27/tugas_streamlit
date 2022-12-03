import streamlit as st
import db_connection
import pandas as pd	

def lihat():
	conn = db_connection.koneksi()

	mycursor = conn.cursor()
	mycursor.execute ('SELECT NO_VOUCHER, TGL, nama_barang, CAST(JUMLAH AS UNSIGNED) FROM barang_masuk \
                    INNER JOIN barang ON barang_masuk.KODE_BARANG = barang.kode_barang \
                    ORDER BY NO_VOUCHER;')

	data = mycursor.fetchall()

	st.header ('LAPORAN DATA BARANG MASUK')
	df = pd.DataFrame(data,
	columns=('No. Voucher', 'Tanggal Masuk', 'Nama Barang', 'Jumlah'))

	st.table(df)

	totalMasuk = 0
	for dt in data:
		jumlah = dt[3]
		totalMasuk = totalMasuk + jumlah
		
	st.success (f'Total Barang Masuk = {totalMasuk}')
	st.balloons()
	
	conn.close() 