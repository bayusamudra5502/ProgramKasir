## FORM MAIN
""" Form yang mengatur mengenai segala yang berkaitan dengan
menu utama dari program
"""

from libs.library import *
from forms.barang import *
from forms.loading import *
from forms.pembelanjaan import *
from forms.pengguna import *

# Gunakan fungsi ini untuk memudahkan anda:
# hapusLayar() : Untuk membersihkan layar
# formBarang() : Membuka form barang
# formPembelanjaan() : Membuka form pembelanjaan
# formPengguna() : Membuka form pengguna

def formMenu():
    """Fungsi ini akan form Menu.
    
    Form menu berperan untuk menjadi perantara antara berbagai
    form yang ada pada program, seperti form barang, form pengguna,
    dan form penjualan.
    """
    hapusLayar()
    pass