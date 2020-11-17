## FORM PEMBELANJAAN
""" Form yang mengatur mengenai segala yang berkaitan dengan
pembelanjaan
"""
from libs.library import *

# Matriks daftar barang
matDaftarBarang = lihatBarang()

# Gunakan fungsi berikut untuk memudahkan:
# editBarang(Kode_Barang, Nama_Barang = None, Stock = None, Harga = None)
#   untuk edit data barang

def formPembelanjaan():
    """Fungsi ini akan menampilkan form Pembelanjaan
    
    Form pembelanjaan adalah form yang digunakan saat penjaga 
    kasir menginputkan barang yang akan dijual kepada pembeli.
    
    Pada form ini juga akan ada opsi untuk mencetak barang"""
    hapusLayar()
    pass