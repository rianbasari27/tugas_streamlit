import streamlit as st
import db_connection	

def lihat():
	conn = db_connection.koneksi()

	st.header('Lihat Stok Barang')
	pilih = st.radio('Pilih :', ('Semua barang', 'By kode barang', 'By stok minimum'))
	if (pilih == 'Semua barang'):
		query = 'select * from barang order by kode_barang'
	elif (pilih == 'By kode barang'):
		kode = st.text_input('Input kode barang')
		query = f"select * from barang where kode_barang = '{kode}'"
	elif (pilih == 'By stok minimum'):
		stok = st.number_input('Input stok minimum', 0)
		query = f"select * from barang where stok >= '{stok}'"

	preview = st.button('Preview')

	mycursor = conn.cursor()

	if (preview):
		mycursor.execute(query)

		data = mycursor.fetchall()
		num = 0
		totalStok = 0

		st.warning ('LAPORAN DATA BARANG')
		st.write ('No - Kode - Nama Barang - Satuan - Stok')
		st.write ('=======================================')
		for dt in data:
			num = num + 1
			kode = dt[0]
			namaBarang = dt[1]
			satuan = dt[2]
			stok = dt[3]
			
			totalStok = totalStok + stok		
			st.write (f'({num}). {kode}, {namaBarang}, {satuan},{stok}')
			
		st.success (f'Total Stok = {totalStok}')
		st.balloons()
		
		conn.close()
