import streamlit as st
import db_connection
import pandas as pd

def lihat():
	conn = db_connection.koneksi()

	st.header('Lihat Stok Barang')
	pilih = st.radio('Pilih :', ('Semua barang', 'By kode barang', 'By stok minimum'))
	if (pilih == 'Semua barang'):
		query = 'select kode_barang, nama_barang, satuan, CAST(stok AS UNSIGNED) from barang order by kode_barang'
	elif (pilih == 'By kode barang'):
		kode = st.text_input('Input kode barang')
		query = f"select kode_barang, nama_barang, satuan, CAST(stok AS UNSIGNED) from barang where kode_barang = '{kode}'"
	elif (pilih == 'By stok minimum'):
		stok = st.number_input('Input stok minimum', 0)
		query = f"select kode_barang, nama_barang, satuan, CAST(stok AS UNSIGNED) from barang where stok >= '{stok}'"

	preview = st.button('Preview')

	mycursor = conn.cursor()

	if (preview):
		mycursor.execute(query)

		data = mycursor.fetchall()
		
		st.warning ('LAPORAN DATA BARANG')
		df = pd.DataFrame(data,
		columns=('Kode', 'Nama Barang', 'Satuan', 'Stok'))

		st.table(df)

		totalStok = 0
		for dt in data:
			stok = dt[3]
			totalStok = totalStok + stok		
			
		st.success (f'Total Stok = {totalStok}')
		st.balloons()
		
		conn.close()
