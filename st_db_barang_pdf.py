import streamlit as st
import st_db_barang_koneksi
from fpdf import FPDF

def print_pdf():

    st.info('PRINT DATA BARANG KE PDF')
    cek = st.button ('Print PDF')
    if(cek):

        pdf = FPDF ('P','cm','A4')
        pdf.set_auto_page_break(auto=True, margin=1)
        pdf.add_page()

        pdf.set_font('helvetica','B',20)
        pdf.set_text_color(90,50,250)
        pdf.cell(0,1,'LAPORAN DATA BARANG',align='C')
        pdf.ln()
        pdf.set_text_color(0,0,0)
        pdf.set_font('helvetica','',10)
        pdf.cell(0,2,'No    KODE    NAMA BARANG     SATUAN      STOK')
        pdf.ln()

        conn = st_db_barang_koneksi.koneksi()
        mycursor =  conn.cursor()
        mycursor.execute('select * from barang order by kode_barang')
        dataku = mycursor.fetchall()

        nomer = 0
        tstok = 0

        for dt in dataku:
            nomer = nomer + 1
            xkd = dt[0]
            xnm = dt[1]
            xsatuan = dt[2]
            xstok = dt[3]

            tstok = tstok + xstok

            pdf.cell (0,0.7, f'({nomer}). {xkd}, {xnm}, {xsatuan}, {xstok}')
            pdf.ln()

        pdf.set_text_color(220,50,50)
        pdf.cell(0,0.7, f'Total Stok = {xstok}')

        conn.close()
        st.balloons()

        pdf.output('laporan_data_barang.pdf')
        st.warning('OK, sudah print PDF, silahkan buka explorer')