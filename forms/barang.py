## FORM BARANG
""" Form yang mengatur mengenai barang yang ada di toko
"""

from libs.library import *

# Fungsi yang digunakan pada file ini
#
# editBarang(Kode_Barang, Nama_Barang = None, Stock = None, Harga = None)
#   Untuk mengedit data barang
# hapusBarang(Kode_Barang)
#   untuk menghapus barang
# tambahBarang(Kode_Barang, Nama_Barang, Jumlah_Stock, Harga)
#   untuk menambahkan barang
# hapusLayar()
#   untuk membersihkan layar
# log10(float)
#   menghasilkan nilai dari logaritma basis 10
# str.expandtabs(int)
#   memperlebar besar tab (\t)
# lihatBarang()
#   mendapatkan list barang
# warnai(str, warna_text)
#   memberi fomat warna pada string

def cetakTabel(matDaftarBarang):
    """Fungsi ini untuk mencetak matriks matDaftarBarang menjadi
    tabel.

    Input : 
    matDaftarBarang (Matrix) : Daftar barang yang akan dicetak.
    Format per item dari matriks ini adalah [Kode_Barang, Nama_Barang, Stok, Harga]

    Output : 
    Mencetak tabel dari matriks daftar barang"""

    # Cetak kepala tabel
    print("=" * (int(log10(len(matDaftarBarang)+1)) + 109))
    print("| No.\t".expandtabs(int(log10(len(matDaftarBarang)+1)) + 6) , 
          " | Kode Barang\t".expandtabs(20)," | Nama Barang\t".expandtabs(50),
          " | Stock\t |".expandtabs(10), " Harga\t |".expandtabs(15))
    print("=" * (int(log10(len(matDaftarBarang)+1)) + 109))

    # Cetak badan tabel
    # Kalau data belum ada cetak BELUM ADA DATA DISINI
    if len(matDaftarBarang) == 0: 
        print("|\tBELUM ADA DATA DISINI".expandtabs((83-21+25)//2), "\t|".expandtabs((83-22+25)//2))
    
    # Cetak semua data di matDaftarBarang
    for i in range(len(matDaftarBarang)):
        print(  f"| {i+1}\t".expandtabs(int(log10(len(matDaftarBarang)+1)) + 7), 
                f"| {matDaftarBarang[i][0]}\t".expandtabs(20), 
                f"| {matDaftarBarang[i][1]}\t".expandtabs(50),
                f"| {str(matDaftarBarang[i][2])}\t".expandtabs(9),
                f"| Rp{matDaftarBarang[i][3]:,}\t |".expandtabs(17))
    
    # Cetak penutup tabel
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
        # Mengambil data yang ada pada database
        matDaftarBarang = lihatBarang()

        # Mencegah KeyboardIntterupt (CTRL+C)
        try:
            # Cetak judul
            print()
            printRataTengah(2, [warnai("FORM BARANG", Warna.cyan)], True)
            print()

            # Cetak tabel dari data barang yang ada di database
            cetakTabel(matDaftarBarang)

            # Cetak pilihan aksi
            print("")
            print("Pilih Aksi :")
            print("1. Tambah barang")
            print("2. Hapus barang")
            print("3. Edit barang")
            print("4. Cari barang")
            print("5. Kembali ke Menu Utama")
            print(warnai("Petunjuk : Jika anda ingin membatalkan aksi yang anda lakukan, tekan CTRL+C.",Warna.biru))

            # Ambil aksi yang diinginkan user
            aksi = input("\nPilihan Aksi : ")

            if(aksi == "1"):
                # User memilih tambah barang
                hapusLayar()
                boolValid = False

                # Selama data yang diinput belum valid, ulangi terus ambil data
                while not boolValid:
                    # Mencetak petunjuk
                    print(warnai("Petunjuk : Masukan data barang yang ingin anda input.",Warna.biru))
                    print(warnai("           Jika anda ingin membatalkan aksi yang anda lakukan, tekan CTRL+C.",Warna.biru))

                    # Mengambil data yang akan ditambahkan dari pengguna
                    Kode_Barang = input("\nKode Barang: ")
                    Nama_Barang = input("Nama Barang: ")
                    Jumlah_Stock= input("Stok Barang: ")
                    Harga = input("Harga Barang: ")

                    # Cek apakah kode barang, nama barang, stock, dan harga tidak kosong?
                    # Cek juga apakah Jumlah stock dan harga yang dimasukan adalah angka
                    if(Kode_Barang != "" and Nama_Barang != "" and
                        Jumlah_Stock != "" and Harga != "" and Jumlah_Stock.isnumeric()
                        and Harga.isnumeric()):
                        # set data yang diinput Valid untuk sementara
                        boolValid = True

                        # Cek apakah barang dengan Kode_Barang sudah ada? bila belum
                        # maka data sudah valid.
                        for i in matDaftarBarang:
                            if(Kode_Barang == i[0]):
                                # Barang dengan kode yang sama ditemukan.
                                # Data tidak valid. Ulangi kembali proses pengambilan data
                                hapusLayar()
                                print(warnai("Barang sudah terdaftar. Gunakan Kode barang lain.", Warna.merah))
                                boolValid = False
                    else:
                        # Cetak error tidak valid
                        hapusLayar()
                        print(warnai("Input tidak valid. Silahkan coba lagi.", Warna.merah))

                # Tambah barang pada database
                tambahBarang(Kode_Barang, Nama_Barang, Jumlah_Stock, Harga)
                # Bersihkan layar dan kembali ke form barang
                hapusLayar()

            elif(aksi == "2"):
                # User memilih Hapus barang
                boolBarangAda = False
                # Cek apakah matriks daftar barang tidak kosong
                if len(matDaftarBarang) > 0:
                    # Lakukan pengambilan data selama kode barang tidak ditemukan
                    while not boolBarangAda:
                        # Cetak petunjuk
                        print(warnai("Petunjuk : Jika anda ingin membatalkan aksi yang anda lakukan, tekan CTRL+C.",Warna.biru))

                        # Mengambil input pengguna
                        Kode_Barang = input("Kode Barang: ")

                        # Cek apakah barang ada
                        for i in matDaftarBarang:
                            if(i[0] == Kode_Barang):
                                boolBarangAda = True
                                listDataBarang = i
                                break
                            
                        if not boolBarangAda:
                            # Cetak error bila barang belum ada
                            print(warnai("Error! Barang tidak ditemukan.", Warna.merah))
                    
                    # Hapus barang di database
                    hapusBarang(Kode_Barang)
                    hapusLayar()
                else:
                    # Cetak peringatan bila matriks barang kosong
                     print(warnai("Data barang belum ada. Silahkan tambah terlebih dahulu", Warna.kuning))

            elif(aksi == "3"):
                # User memilih Edit barang
                hapusLayar()

                # Cetak judul
                printRataTengah(2, [warnai("EDIT BARANG", Warna.cyan)], True)
                print()
                cetakTabel(matDaftarBarang)

                edit = False
                boolBarangAda = False
                listDataBarang = None

                # Cek apakah barang pada matriks barang ada
                if(len(matDaftarBarang) > 0):
                    # Ambil data kode barang selama kode barang belum ditemukan
                    while not boolBarangAda:
                        # Mencetak petunjuk
                        print()
                        print(warnai("Petunjuk : Jika anda ingin membatalkan aksi yang anda lakukan, tekan CTRL+C.",Warna.biru))
                        print("Masukan kode barang dari data yang ingin anda hapus")

                        # Mengambil input pengguna
                        Kode_Barang = input("\nKode Barang: ")

                        # Memeriksa apakah barang ada
                        for i in matDaftarBarang:
                            if(i[0] == Kode_Barang):
                                boolBarangAda = True
                                listDataBarang = i
                                break
                        
                        if not boolBarangAda:
                            # Cetak error karena barang tidak ada
                            hapusLayar()
                            printRataTengah(2, [warnai("EDIT BARANG", Warna.cyan)], True)
                            print()
                            cetakTabel(matDaftarBarang)
                            print(warnai("\nError! Kode barang tidak ditemukan",Warna.merah))

                    Kode_Barang = listDataBarang[0]
                    Nama_Barang = listDataBarang[1]
                    Stock = listDataBarang[2]
                    Harga = listDataBarang[3]

                    # Lakukan selama edit belum selesai
                    while(edit == False):
                        if(boolBarangAda):
                            # Bila barang ada pada database
                            # Cetak judul
                            hapusLayar()
                            printRataTengah(2, [warnai("EDIT BARANG", Warna.cyan)], True)
                            print()
                            
                            # Tampilkan data barang yang akan diedit
                            print("Data Barang yang akan diedit: ")
                            print(f"Kode Barang : {Kode_Barang}\nNama Barang : {Nama_Barang}")
                            print(f"Stock : {Stock}\nHarga : {Harga}")
                            print()

                            # Tampilkan pilihan aksi
                            print("Pilih Aksi :")
                            print("1. Edit Nama Barang")
                            print("2. Edit Stok Barang")
                            print("3. Edit Harga Barang")
                            print("4. Simpan")
                            print("5. Batalkan dan kembali")

                            # Tampilkan petunjuk
                            print(warnai("\nCatatan : Jika anda ingin membatalkan aksi yang anda lakukan, tekan CTRL+C.",Warna.biru))
                            aksi_edit = input("Pilihan Aksi : ")

                            try:
                                if(aksi_edit == "1"):
                                    # Ubah nama barang
                                    Nama_Barang = input("Nama Barang Baru: ")
                                elif(aksi_edit == "3"):
                                    # Ubah harga
                                    Harga = input("Harga Baru: ")
                                elif(aksi_edit == "2"):
                                    # Ubah stock barang
                                    Stock = input("Stok Baru: ")
                                elif(aksi_edit == "4"):
                                    # Simpan perubahan pada database
                                    editBarang(Kode_Barang, Nama_Barang, Stock, Harga)
                                    edit = True # Editing selesai dan keluar loop
                                elif(aksi_edit == "5"):
                                    # Editing selesai tanpa menerapkann perubahan pada
                                    # database
                                    edit = True
                                else:
                                    # Tampilkan error
                                    hapusLayar()
                                    print(warnai("Error! Masukan angka antara 1 s.d 4 saja.", Warna.merah))

                            except KeyboardInterrupt:
                                # User menekan CTRL+C. Aksi dibatalkan
                                print(warnai("Pemberitahuan : Aksi dibatalkan..", Warna.hijau))

                    hapusLayar()
                else:
                    # Tampilkan peringatan
                    print(warnai("Data barang belum ada. Silahkan tambah terlebih dahulu", Warna.kuning))

            elif(aksi == "5"):
                # User memilih kembali ke menu utama
                menu_utama = True
            elif(aksi == "4"):
                # User memilih untuk mencari barang
                try:
                    boolSelesai = False
                    hapusLayar()
                    
                    while not boolSelesai:
                        # Cetak judul
                        printRataTengah(2, [warnai("PENCARI BARANG", Warna.cyan)], True)

                        # Cetak pilihan aksi 
                        print()
                        print("Apa yang anda ingin lakukan?")
                        print("1. Mencari detail barang dengan Kode Barang")
                        print("2. Mencari detail barang dengan Nama Barang")
                        print("3. Kembali ke Form Barang")
                        print(warnai("Petunjuk : Tekan CTRL+C jika ingin membatalkan aksi.\n",Warna.biru))
                        
                        # Ambil input pilihan aksi
                        strCmd = input("Pilihan aksi : ")

                        if strCmd == "1":
                            # User memilih pencarian berdasarkan kode barang
                            # Mencetak perintah
                            print()
                            print("Masukkan kode barang atau subset kode barang yang ingin dicari.")

                            # Mengambil kode barang yang akan dicari
                            strKode = input("Kode barang : ")

                            # Cari data yang sesuai dengan pola regex dari kode barang yang diinput
                            matHasil = cariRegex(strKode, matDaftarBarang, 0)
                            
                            # Cetak hasil penelusuran
                            hapusLayar()
                            printRataTengah(2, [warnai("HASIL PENCARIAN", Warna.cyan)], True)
                            print()
                            print(f"Berikut ini adalah hasil pencarian. Didapatkan {len(matHasil)} data.")
                            cetakTabel(matHasil)
                            
                            # Menahan agar hasil penelusuran tidak langsung tertutup
                            input("\nTekan Enter untuk kembali.")
                            hapusLayar()
                        elif strCmd == "2":
                            # User memilih pencarian berdasarkan nama barang
                            # Mencetak perintah
                            print()
                            print("Masukkan nama barang atau subset nama barang yang ingin dicari.")

                            # Mengambil nama barang yang akan dicari
                            strKode = input("Nama Barang : ")

                            # Mencari nama barang yang sesuai pada Daftar barang
                            matHasil = cariRegex(strKode, matDaftarBarang, 1)
                            
                            # Menampilkan hasil penelusuran
                            hapusLayar()
                            printRataTengah(2, [warnai("HASIL PENCARIAN", Warna.cyan)], True)
                            print()
                            print(f"Berikut ini adalah hasil pencarian. Didapatkan {len(matHasil)} data.")
                            cetakTabel(matHasil)
                            
                            # Menahan agar hasil penelusuran tidak tertutup otomatis
                            input("\nTekan Enter untuk kembali.")
                            hapusLayar()
                        elif strCmd == "3":
                            # Pencarian barang selesai
                            boolSelesai = True
                        else:
                            # Tampilkann error
                            hapusLayar()
                            print(warnai("Error! Masukan angka antara 1 s.d 5 saja.", Warna.merah))
                except KeyboardInterrupt:
                    # User menekan CTRL+C. Aksi dibatalkan
                    print(warnai("Pemberitahuan : Aksi dibatalkan..", Warna.hijau))
                finally:
                    # Setelah selesai dari pencarian barang, hapus layar dan kembali ke form barang
                    hapusLayar()
            else:
                # Tampilkan error
                print(warnai("Error! Masukan angka antara 1 s.d 5 saja.", Warna.merah))
        except KeyboardInterrupt as kbd:
            # User menekan CTRL+C. Aksi dibatalkan
            hapusLayar()
            print(warnai("Pemberitahuan : Aksi dibatalkan..", Warna.hijau))
        