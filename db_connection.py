import streamlit as st
import mysql.connector

def koneksi():
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='',
        db='dbgudang',
        port= 3306
    )
    return conn

if __name__ == '__main__':
    koneksi()
