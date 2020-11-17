## FORM BARANG
""" Form yang mengatur mengenai barang yang ada di toko
"""

from libs.library import *

# Matriks datar barang
# Urutan setiap elemen baris : 
# [Kode_Barang, Nama_Barang, Stok, Harga]
matDaftarBarang = lihatBarang()

# Gunakan fungsi berikut untuk memudahkan:
# editBarang(Kode_Barang, Nama_Barang = None, Stock = None, Harga = None)
#   untuk edit data barang. Klo mau edit nama barangnya saja, kayak gini 
#   contohnya: editBarang("123456", Nama_Barang = "Kucing"). Klo mau
#   edit Nama barang menjadi "A" dan stock menjadi 20, bisa gini: 
#   editBarang("123", Nama_barang="A", stock = 20)
#
#
# hapusBarang(Kode_Barang)
#   untuk happus barang
#
# tambahBarang(Kode_Barang, Nama_Barang, Jumlah_Stock, Harga)
#   untuk nambah barang
# HAPUS KOMEN DIATAS KLO UDAH WKWKWK

def formBarang():
    """Fungsi ini akan menampilkan form barang.
    
    Fungsi ini akan menampilkan daftar barang yang  ada di toko beserta
    stoknya dan opsi untuk menambah, mengedit, dan menghapus data yang
    ada pada toko.
    """
    hapusLayar()
    pass