import streamlit as st
import db_connection	

def lihat():
	conn = db_connection.koneksi()

	mycursor = conn.cursor()
	mycursor.execute ('SELECT NO_VOUCHER, TGL, nama_barang, JUMLAH FROM barang_masuk \
                    INNER JOIN barang ON barang_masuk.KODE_BARANG = barang.kode_barang \
                    ORDER BY NO_VOUCHER;')

	data = mycursor.fetchall()
	num = 0
	totalMasuk = 0	

	st.warning ('LAPORAN DATA BARANG MASUK')
	st.write ('No - No. Voucher - Tanggal - Nama Barang - Jumlah')
	st.write ('=======================================')
	for dt in data:
		num = num + 1
		noVoucher = dt[0]
		tanggal = dt[1]
		namaBarang = dt[2]
		jumlah = dt[3]
		
		totalMasuk = totalMasuk + jumlah		
		st.write (f'({num}). {noVoucher}, {tanggal}, {namaBarang},{jumlah}')
		
	st.success (f'Total Barang Masuk = {totalMasuk}')
	st.balloons()
	
	conn.close() 