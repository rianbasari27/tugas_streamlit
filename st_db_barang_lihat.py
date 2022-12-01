#File CRUD LIHAT DATA BARANG
import streamlit as st
import st_db_barang_koneksi		#koneksi ke db server

def lihat():
	#buka koneksi db
	conn = st_db_barang_koneksi.koneksi()

	#ambil data
	mycursor = conn.cursor()
	mycursor.execute ('select * from barang order by kode_barang')

    # ambil data nya
	dataku = mycursor.fetchall()
	nomer = 0	#buat nomer urut
	tstok = 0	#total stok akhir laporan

    # looping baca data
	st.warning ('LAPORAN DATA BARANG')
	st.write ('No - Kode - Nama Barang - Satuan - Stok')
	st.write ('=======================================')
	for dt in dataku:
		nomer = nomer + 1
		xkd = dt[0]
		xnm = dt[1]
		xsatuan = dt[2]
		xstok = dt[3]
		
        # hitung total stok
		tstok = tstok + xstok		
		st.write (f'({nomer}). {xkd}, {xnm}, {xsatuan},{xstok}')
		
	st.success (f'Total Stok = {tstok}')
	st.balloons()
	
	conn.close() #tutup koneksi