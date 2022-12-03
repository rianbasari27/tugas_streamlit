import streamlit as st
import db_connection
import pandas as pd
from fpdf import FPDF

def print_pdf():

    st.header('PRINT STOK BARANG PDF')
    pilih = st.radio('Pilih :', ('Semua barang', 'By stok minimum'))
    if (pilih == 'Semua barang'):
        query = f"SELECT kode_barang, nama_barang, satuan, CAST(stok AS UNSIGNED) FROM `barang`"
    elif (pilih == 'By stok minimum'):
        minimum = st.text_input('Input stok minimum')
        query = f"SELECT kode_barang, nama_barang, satuan, CAST(stok AS UNSIGNED) FROM `barang` where stok >= '{minimum}'"

    cek = st.button ('Print PDF')
    if(cek):
        pdf = FPDF ('P','cm','A4')
        pdf.set_auto_page_break(auto=True, margin=1)
        pdf.add_page()

        m = 2 # Margin
        pw = 21 - 2 * m # Page width
        ch = 0.7 # Cell height

        pdf.set_font('helvetica','B',28)
        pdf.set_text_color(90,50,250)
        pdf.cell(0,1,'LAPORAN STOK BARANG',align='C')
        pdf.ln()
        pdf.set_text_color(0,0,0)
        pdf.set_font('helvetica','B',12)
        pdf.cell(w=(pw/5), h=ch, txt="No.", border=1, ln=0)
        pdf.cell(w=(pw/5), h=ch, txt="Kode Barang", border=1, ln=0)
        pdf.cell(w=(pw/5), h=ch, txt="Nama Barang", border=1, ln=0)
        pdf.cell(w=(pw/5), h=ch, txt="Satuan", border=1, ln=0)
        pdf.cell(w=(pw/5), h=ch, txt="Stok", border=1, ln=0)
        pdf.ln()

        conn = db_connection.koneksi()
        mycursor = conn.cursor()
        mycursor.execute(query)
        data = mycursor.fetchall()

        st.warning ('LAPORAN STOK BARANG')

        num = 0
        totalStok = 0

        for dt in data:
            num = num + 1
            # kode = dt[0]
            # nama = dt[1]
            # satuan = dt[2]
            stok = dt[3]

            pdf.set_font('helvetica','',12)
            pdf.cell(w=(pw/5), h=ch, txt=f"{num}", border=1, ln=0)
            pdf.cell(w=(pw/5), h=ch, txt=f"{dt[0]}", border=1, ln=0)
            pdf.cell(w=(pw/5), h=ch, txt=f"{dt[1]}", border=1, ln=0)
            pdf.cell(w=(pw/5), h=ch, txt=f"{dt[2]}", border=1, ln=0)
            pdf.cell(w=(pw/5), h=ch, txt=f"{dt[3]}", border=1, ln=0)
            pdf.ln()
            
            totalStok = totalStok + stok

        df = pd.DataFrame(data,
        columns=('Kode', 'Nama Barang', 'Satuan', 'Stok'))
        st.table(df)

        pdf.set_text_color(220,50,50)
        pdf.cell(w=(pw), h=ch, txt=f"Total stok = {totalStok}", border=1, ln=0)
        # pdf.cell(0,0.7, f'Total Stok = {totalStok}')

        conn.close()
        st.balloons()

        pdf.output('laporan_stok_barang.pdf')
        st.warning('Data sudah diprint!')