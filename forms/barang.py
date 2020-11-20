## FORM BARANG
""" Form yang mengatur mengenai barang yang ada di toko
"""

from libs.library import *

# Gunakan fungsi berikut untuk memudahkan:
# editBarang(Kode_Barang, Nama_Barang = None, Stock = None, Harga = None)
#   untuk edit data barang. Klo mau edit nama barangnya saja, kayak gini 
#   contohnya: editBarang("123456", Nama_Barang = "Kucing"). Klo mau
#   edit Nama barang menjadi "A" dan stock menjadi 20, bisa gini: 
#   editBarang("123", Nama_barang="A", stock = 20)
#
# hapusBarang(Kode_Barang)
#   untuk happus barang
#
# tambahBarang(Kode_Barang, Nama_Barang, Jumlah_Stock, Harga)
#   untuk nambah barang
# HAPUS KOMEN DIATAS KLO UDAH WKWKWK

def cetakTabel(matDaftarBarang):
    """Fungsi ini untuk mencetak matriks matDaftarBarang menjadi
    tabel."""

    print("=" * (int(log10(len(matDaftarBarang)+1)) + 109))
    print("| No.\t".expandtabs(int(log10(len(matDaftarBarang)+1)) + 6) , 
          " | Kode Barang\t".expandtabs(20)," | Nama Barang\t".expandtabs(50),
          " | Stock\t |".expandtabs(10), " Harga\t |".expandtabs(15))
    print("=" * (int(log10(len(matDaftarBarang)+1)) + 109))
    if len(matDaftarBarang) == 0: # Kalau data belum ada cetak BELUM ADA DATA DISINI
        print("|\tBELUM ADA DATA DISINI".expandtabs((83-21+25)//2), "\t|".expandtabs((83-22+25)//2))
    for i in range(len(matDaftarBarang)):
        print(  f"| {i+1}\t".expandtabs(int(log10(len(matDaftarBarang)+1)) + 7), 
                f"| {matDaftarBarang[i][0]}\t".expandtabs(20), 
                f"| {matDaftarBarang[i][1]}\t".expandtabs(50),
                f"| {str(matDaftarBarang[i][2])}\t".expandtabs(9),
                f"| Rp{matDaftarBarang[i][3]:,}\t |".expandtabs(17))
    print("-" * (int(log10(len(matDaftarBarang)+1)) + 109))

def formBarang():
    """Fungsi ini akan menampilkan form barang.
    
    Fungsi ini akan menampilkan daftar barang yang  ada di toko beserta
    stoknya dan opsi untuk menambah, mengedit, dan menghapus data yang
    ada pada toko.
    """
    menu_utama = False
    hapusLayar()

    while(menu_utama == False):

        # Matriks daftar barang
        # Urutan setiap elemen baris : 
        # [Kode_Barang, Nama_Barang, Stok, Harga]
        matDaftarBarang = lihatBarang()
        try:
            print()
            # Cetak output di tengah
            printRataTengah(2, [warnai("FORM BARANG", Warna.cyan)], True)
            print()

            cetakTabel(matDaftarBarang)

            print("")
            print("Pilih Aksi :")
            print("1. Tambah barang")
            print("2. Hapus barang")
            print("3. Edit barang")
            print("4. Cari barang")
            print("5. Kembali ke Menu Utama")
            print(warnai("Petunjuk : Jika anda ingin membatalkan aksi yang anda lakukan, tekan CTRL+C.",Warna.biru))
            aksi = input("\nPilihan Aksi : ")

            if(aksi == "1"):
                hapusLayar()
                boolValid = False

                while not boolValid:
                    print(warnai("Petunjuk : Masukan data barang yang ingin anda input.",Warna.biru))
                    print(warnai("           Jika anda ingin membatalkan aksi yang anda lakukan, tekan CTRL+C.",Warna.biru))
                    Kode_Barang = input("\nKode Barang: ")
                    Nama_Barang = input("Nama Barang: ")
                    Jumlah_Stock= input("Stok Barang: ")
                    Harga = input("Harga Barang: ")

                    if(Kode_Barang != "" and Nama_Barang != "" and
                        Jumlah_Stock != "" and Harga != "" and Jumlah_Stock.isnumeric()
                        and Harga.isnumeric()):
                        boolValid = True

                        # Cek apakah barang dengan Kode_Barang sudah ada?
                        for i in matDaftarBarang:
                            if(Kode_Barang == i[0]):
                                hapusLayar()
                                print(warnai("Barang sudah terdaftar. Gunakan Kode barang lain.", Warna.merah))
                                boolValid = False
                        
                    else:
                        hapusLayar()
                        print(warnai("Input tidak valid. Silahkan coba lagi.", Warna.merah))

                tambahBarang(Kode_Barang, Nama_Barang, Jumlah_Stock, Harga)
                hapusLayar()

            elif(aksi == "2"):
                boolBarangAda = False
                if len(matDaftarBarang) > 0:
                    while not boolBarangAda:
                        print(warnai("Petunjuk : Jika anda ingin membatalkan aksi yang anda lakukan, tekan CTRL+C.",Warna.biru))
                        Kode_Barang = input("Kode Barang: ")
                        for i in matDaftarBarang:
                            if(i[0] == Kode_Barang):
                                boolBarangAda = True
                                listDataBarang = i
                                break
                            
                        if not boolBarangAda:
                            print(warnai("Error! Barang tidak ditemukan.", Warna.merah))

                    hapusBarang(Kode_Barang)
                    hapusLayar()
                else:
                     print(warnai("Data barang belum ada. Silahkan tambah terlebih dahulu", Warna.kuning))

            elif(aksi == "3"):
                hapusLayar()
                printRataTengah(2, [warnai("EDIT BARANG", Warna.cyan)], True)
                print()
                cetakTabel(matDaftarBarang)

                edit = False
                boolBarangAda = False
                listDataBarang = None
                if(len(matDaftarBarang) > 0):
                    while not boolBarangAda:
                        print()
                        print(warnai("Petunjuk : Jika anda ingin membatalkan aksi yang anda lakukan, tekan CTRL+C.",Warna.biru))
                        print("Masukan kode barang dari data yang ingin anda hapus")
                        Kode_Barang = input("\nKode Barang: ")
                        for i in matDaftarBarang:
                            if(i[0] == Kode_Barang):
                                boolBarangAda = True
                                listDataBarang = i
                                break
                        if not boolBarangAda:
                            hapusLayar()
                            printRataTengah(2, [warnai("EDIT BARANG", Warna.cyan)], True)
                            print()
                            cetakTabel(matDaftarBarang)
                            print(warnai("\nError! Kode barang tidak ditemukan",Warna.merah))

                    Kode_Barang = listDataBarang[0]
                    Nama_Barang = listDataBarang[1]
                    Stock = listDataBarang[2]
                    Harga = listDataBarang[3]
                    while(edit == False):
                        if(boolBarangAda):
                            hapusLayar()
                            printRataTengah(2, [warnai("EDIT BARANG", Warna.cyan)], True)
                            print()

                            print("Data Barang yang akan diedit: ")
                            print(f"Kode Barang : {Kode_Barang}\nNama Barang : {Nama_Barang}")
                            print(f"Stock : {Stock}\nHarga : {Harga}")
                            print()

                            print("Pilih Aksi :")
                            print("1. Edit Nama Barang")
                            print("2. Edit Stok Barang")
                            print("3. Edit Harga Barang")
                            print("4. Simpan")
                            print("5. Batalkan dan kembali")
                            print(warnai("\nCatatan : Jika anda ingin membatalkan aksi yang anda lakukan, tekan CTRL+C.",Warna.biru))
                            aksi_edit = input("Pilihan Aksi : ")

                            try:
                                if(aksi_edit == "1"):
                                    Nama_Barang = input("Nama Barang Baru: ")

                                elif(aksi_edit == "3"):
                                    Harga = input("Harga Baru: ")

                                elif(aksi_edit == "2"):
                                    Stock = input("Stok Baru: ")

                                elif(aksi_edit == "4"):
                                    editBarang(Kode_Barang, Nama_Barang, Stock, Harga)
                                    edit = True #editing selesai dan keluar loop
                                elif(aksi_edit == "5"):
                                    edit = True
                                else:
                                    hapusLayar()
                                    print(warnai("Error! Masukan angka antara 1 s.d 4 saja.", Warna.merah))
                            except KeyboardInterrupt:
                                print(warnai("Pemberitahuan : Aksi dibatalkan..", Warna.hijau))

                    hapusLayar()
                else:
                    print(warnai("Data barang belum ada. Silahkan tambah terlebih dahulu", Warna.kuning))

            elif(aksi == "5"):
                menu_utama = True
            elif(aksi == "4"):
                try:
                    boolSelesai = False
                    hapusLayar()
                    while not boolSelesai:
                        printRataTengah(2, [warnai("PENCARI BARANG", Warna.cyan)], True)
                        print()
                        print("Apa yang anda ingin lakukan?")
                        print("1. Mencari detail barang dengan Kode Barang")
                        print("2. Mencari detail barang dengan Nama Barang")
                        print("3. Kembali ke Form Barang")
                        print(warnai("Petunjuk : Tekan CTRL+C jika ingin membatalkan aksi.\n",Warna.biru))

                        strCmd = input("Pilihan aksi : ")
                        if strCmd == "1":
                            print()
                            print("Masukkan kode barang atau subset kode barang yang ingin dicari.")
                            strKode = input("Kode barang : ")

                            matHasil = cariRegex(strKode, matDaftarBarang, 0)
                            hapusLayar()

                            printRataTengah(2, [warnai("HASIL PENCARIAN", Warna.cyan)], True)
                            print()
                            print(f"Berikut ini adalah hasil pencarian. Didapatkan {len(matHasil)} data.")
                            cetakTabel(matHasil)

                            input("\nTekan Enter untuk kembali.")
                            hapusLayar()
                        elif strCmd == "2":
                            print()
                            print("Masukkan nama barang atau subset nama barang yang ingin dicari.")
                            strKode = input("Nama Barang : ")

                            matHasil = cariRegex(strKode, matDaftarBarang, 1)
                            hapusLayar()

                            printRataTengah(2, [warnai("HASIL PENCARIAN", Warna.cyan)], True)
                            print()
                            print(f"Berikut ini adalah hasil pencarian. Didapatkan {len(matHasil)} data.")
                            cetakTabel(matHasil)
                            
                            input("\nTekan Enter untuk kembali.")
                            hapusLayar()
                        elif strCmd == "3":
                            boolSelesai = True
                        else:
                            hapusLayar()
                            print(warnai("Error! Masukan angka antara 1 s.d 5 saja.", Warna.merah))
                except KeyboardInterrupt:
                    print(warnai("Pemberitahuan : Aksi dibatalkan..", Warna.hijau))
                finally:
                    hapusLayar()
            else:
                print(warnai("Error! Masukan angka antara 1 s.d 5 saja.", Warna.merah))
        except KeyboardInterrupt as kbd:
            hapusLayar()
            print(warnai("Pemberitahuan : Aksi dibatalkan..", Warna.hijau))
        