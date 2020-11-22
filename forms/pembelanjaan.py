## FORM PEMBELANJAAN
""" Form yang mengatur mengenai segala yang berkaitan dengan
pembelanjaan
"""
# Impor Pustaka
from libs.library import *
from forms.barang import cetakTabel as cetakTabelBarang

def hitungBelanjaan(Keranjang_Belanja):
    """Menghitung total belanjaan.
    
    Masukan:
    Keranjang_Belanja = Matriks keranjang belanja.
    Urutan matriks keranjang belanja adalah 
    [Kode_Barang, Nama_Barang, Harga, Qyt, Diskon]
    
    Output : Jumlah biaya yang harus dibayar (float)"""

    floatSum = 0.0
    # Menghitung jumlah belanjaan tiap baris
    for i in Keranjang_Belanja:
        # Menghitung harga * Qyt * (1-diskon)
        floatSum += i[2]*i[3]*(1-i[4])
    
    return floatSum

def cetakStruk(Keranjang_Belanja, Uang_Dibayarkan):
    """Cetak Struk menjadi file.
    
    Masukan:
    Keranjang_Belanja = Matriks keranjang belanja.
    Uang_Dibayarkan = Besar uang yang dibayarkan (float).
    
    Output : Sebuah file pada folder struk dengan nama
    berforma Struk_Hari-bulan-tahun_jam-menit-detik.txt
    dan fungsi ini akan mengembalikan True bila berhasil
    mencetak file"""
    
    # Handler Error
    try:
        # Dapatkan tanggal dan waktu sekarang
        now = datetime.datetime.now()
        
        # Buat dan buka file baru pada mode menulis
        file = open("struk\\"+ now.strftime("Struk_%d-%m-%Y_%H-%M-%S") +".txt","w")

        # Cetak Kepala file
        print("=================", file=file)
        print("STRUK PEMBAYARAN", file=file)
        print("=================", file=file)
        print(f"Tanggal\t: {now.day}-{now.month}-{now.year}", file=file)
        print(f"Waktu\t: {now.hour}:{now.minute}:{now.second}", file=file)
        print("",file=file)

        # Cetak keranjang belanja
        for i in Keranjang_Belanja:
            print(f"{i[0]}\t".expandtabs(14), f"{i[1]}\t".expandtabs(30), end="", file=file)
            print(f"Rp{i[2]}\t".expandtabs(17), f"x {i[3]}", f"= {i[2]*i[3]*(1-i[4])}", end="", file=file)
            if i[4] != 0:
                print(f" (Disc {i[4]*100:.0f}%)", end="", file=file)
            print(file=file)
        
        # Mencetak keterangan transaksi
        # Seperti jumlah belanjaan, bayar, dan kembalian
        floatTotal = hitungBelanjaan(Keranjang_Belanja)
        print("\nTotal     : Rp", f"{floatTotal:,.2f}", sep="", file=file)
        print("Bayar     : Rp", f"{Uang_Dibayarkan:,.2f}", sep="", file=file)
        print("Kembalian : Rp", f"{Uang_Dibayarkan-floatTotal:,.2f}", sep="", file=file)
        print(file=file)

        # Cetak penutup file
        print("Terima Kasih :D", file=file)
        return True

    except IOError as err:
        # Bila terjadi kegagalan dalam pencetakan struk
        # Cetak error di layar
        print(warnai("Gagal membuat stuk pembayaran.", Warna.merah))
        return False

def tambahKeranjang(Keranjang_Belanja, Daftar_Barang):
    """Fungsi ini akan mengubah Keranjang Belanja.
    
    Input : 
    Keranjang_Belanja = Matriks keranjang belanja. (Reference Mode)
    Daftar_Barang     = Matriks daftar barang belanjaan. (Reference Mode)

    Keluaran:
    True bila berhasil, False bila gagal. Keranjang ditambhakan barang
    baru."""
    
    # Cari barang di Daftar Barang hingga ketemu
    intIndex = -1
    hapusLayar()
    while(intIndex == -1):
        # Cetak Judul
        cetakFrame()
        printRataTengah(3, [warnai("TAMBAH KERANJANG", Warna.cyan)])
        pindahkanKursor(5,4)

        # Cetak Petunjuk
        print(warnai("Petunjuk : Tekan CTRL+C untuk membatalkan aksi ini.", Warna.biru))
        pindahkanKursor(6,4)
        print(warnai("           Tulis CARI pada input kode barang bila anda ingin mencari data barang.\n", Warna.biru))

        # Mengambil input kode barang
        pindahkanKursor(8,4)
        strKode = input("Masukkan kode barang : ")

        if strKode.upper() == "CARI":
            # Bila keyword yang ditulis adalah CARI, maka
                try:
                    boolSelesai = False
                    hapusLayar()
                    while not boolSelesai:
                        # Cetak judul
                        printRataTengah(2, [warnai("PENCARI BARANG", Warna.cyan)], True)
                        print()

                        # Cetak aksi yang mungkin
                        print("Apa yang anda ingin lakukan?")
                        print("1. Mencari detail barang dengan Kode Barang")
                        print("2. Mencari detail barang dengan Nama Barang")
                        print("3. Kembali ke Form Tambah Keranjang")
                        
                        # Cetak petunjuk berwarna biru
                        print(warnai("Petunjuk : Tekan CTRL+C jika ingin membatalkan aksi.\n",Warna.biru))

                        # Mengambil input aksi
                        strCmd = input("Pilihan aksi : ")
                        if strCmd == "1":
                            # User memilih berdasarkan kode barang
                            print()
                            print("Masukkan kode barang atau subset kode barang yang ingin dicari.")
                            
                            # Mengambil input format kode barang
                            strKode = input("Kode barang : ")

                            # Mencari barang dengan Regex berdasarkan format kode barang
                            matHasil = cariRegex(strKode, Daftar_Barang, 0)

                            # Mencetak hasil pencarian
                            # Cetak kepala
                            hapusLayar()
                            printRataTengah(2, [warnai("HASIL PENCARIAN", Warna.cyan)], True)
                            print()

                            # Tampilkan hasil penelusuran
                            print(f"Berikut ini adalah hasil pencarian. Didapatkan {len(matHasil)} data.")
                            cetakTabelBarang(matHasil)

                            # Tahan program agar tidak langsung menutup
                            input("\nTekan Enter untuk kembali.")
                            hapusLayar()
                        elif strCmd == "2":
                            # User memilih berdasarkan nama barang
                            # Cetak perintah
                            print()
                            print("Masukkan nama barang atau subset nama barang yang ingin dicari.")
                            
                            # Input nama kode barang yang mau dicari
                            strKode = input("Nama Barang : ")

                            # Cari barang berdasarkan nama barang
                            matHasil = cariRegex(strKode, Daftar_Barang, 1)
                            hapusLayar()

                            # Tampilkan hasil pencarian
                            printRataTengah(2, [warnai("HASIL PENCARIAN", Warna.cyan)], True)
                            print()
                            print(f"Berikut ini adalah hasil pencarian. Didapatkan {len(matHasil)} data.")
                            cetakTabelBarang(matHasil)
                            
                            # Tahan program agar tidak langsung kembali
                            input("\nTekan Enter untuk kembali.")
                            hapusLayar()
                        elif strCmd == "3":
                            # Kembali ke tambah barang
                            boolSelesai = True
                        else:
                            # Bila input tidak valid, cetak error
                            hapusLayar()
                            print(warnai("Error! Masukan angka antara 1 s.d 3 saja.", Warna.merah))
                except KeyboardInterrupt:
                    # User menekann CTRL+C. Aksi dibatalkan
                    print(warnai("Pemberitahuan : Aksi dibatalkan..", Warna.hijau))
                finally:
                    hapusLayar()
        else:
            # Cari barang dengan Kode barang yang dicari
            for i in range(len(Daftar_Barang)):
                if(Daftar_Barang[i][0] == strKode):
                    intIndex = i
                    break
            
            if(intIndex == -1):
                # Barang tidak ditemukan, maka tampilkan error
                hapusLayar()
                pindahkanKursor(9,4)
                print(warnai("Kesalahan: Kode barang tidak ditemukan.", Warna.merah))
                pindahkanKursor(1,1)

    # Bersihkan baris ke 9 dari error
    pindahkanKursor(9,4)
    print(" " * 40)
    intQyt = 0

    # Menginput data jumlah barang yg mau dibeli
    while intQyt <= 0:
        pindahkanKursor(9,4)
        try:
            intQyt = int(input("Masukkan banyak yang mau dibeli : "))
            if(intQyt <= 0):
                raise ValueError
        except ValueError:
            # Bila input tidak valid, tampilkan error
            pindahkanKursor(10,4)
            print(warnai("Error! Massukan harus berupa integer lebih dari 0.", Warna.merah))
            continue
        
        # Hapus baris ke-10
        pindahkanKursor(10,4)
        print(" " * 50)    

        if(Daftar_Barang[i][2] < intQyt):
            # Barang tidak mencukupi stok
            intQyt = -1
            pindahkanKursor(10,4)
            print(warnai("Peringatan: Stock tidak mencukupi.", Warna.kuning))
    
    # Hapus baris 10 pada layar
    pindahkanKursor(10,4)
    print(" "*50)

    # Ambil input diskon
    intDiskon = -1
    while intDiskon == -1:
        pindahkanKursor(10,4)
        try:
            intDiskon = int(input("Masukkan jumlah diskon (dalam %) : "))
        except ValueError:
            # Bila input diskon bukan integer, tampilkan error dan
            # ambil data lagi
            pindahkanKursor(11,4)
            print(" "*60)
            pindahkanKursor(11,4)
            print(warnai("Error! Massukan input berupa integer.", Warna.merah))
            continue
        
        # Hapus baris ke-11
        pindahkanKursor(11,4)
        print(" " * 37)    

        # Cek apakah input diskon berada di antara 0 s.d. 100 (inklusif)
        if(not(0 <= intDiskon <= 100)):
            # Bila tidak, tampilkan error
            intDiskon = -1
            pindahkanKursor(11,4)
            print(" "*60)
            pindahkanKursor(11,4)
            print(warnai("Kesalahan: Diskon harus diantara 0 s.d. 100.", Warna.merah))
        else:
            # Mengurangi jumlah stock di daftar barang
            Daftar_Barang[i][2] -= intQyt
            # Tambah data ke keranjang
            Keranjang_Belanja.append([Daftar_Barang[intIndex][0], Daftar_Barang[intIndex][1], 
                              Daftar_Barang[intIndex][3], intQyt, intDiskon / 100])

def kurangKeranjang(Keranjang_Belanja, Daftar_Barang):
    """Mengurangi barang pada keranjang
    
    Input : 
    Keranjang_Belanja = Matriks keranjang belanja. (Reference Mode)
    Daftar_Barang     = Matriks daftar barang belanjaan. (Reference Mode)

    Keluaran:
    True bila berhasil, False bila gagal. Keranjang_belanja dan 
    daftar_barang akan berubah seiring fungsi ini berhasil dijalankan."""

    # Memeriksa apakah keranjang belanja kosong atau tidak
    if len(Keranjang_Belanja) == 0:
        # Jika kosong, jangan lakukan apa-apa
        return False

    # Ambil nomor baris yang valid
    boolValid = False
    hapusLayar()
    while not boolValid:
        # Cetak Judul
        cetakFrame()
        printRataTengah(3, [warnai("KURANGI KERANJANG", Warna.cyan)])
        pindahkanKursor(4,4)

        # Cetak Petunjuk
        print(warnai("Petunjuk : Tekan CTRL+C untuk membatalkan aksi ini.", Warna.biru))
        pindahkanKursor(5,4)
        print(warnai("           Tulis LIHAT pada input Nomor Baris bila anda ingin melihat keranjang.\n", Warna.biru))

        # Ambil nomor baris dari user
        pindahkanKursor(7,4)
        strKeranjang = input("Masukkan Nomor Baris : ")
        if(strKeranjang.upper() == "LIHAT"):
            # Apabila user menulis LIHAT, tampilkan
            # keranjang belanja saat ini
            hapusLayar()
            cetakTabel(Keranjang_Belanja)

            # Tahan program agar tidak langsung tertutup
            input("Tekan Enter bila anda sudah selesai. ")

            # Kembali ke kurangi keranjang
            hapusLayar()
            continue
        
        try:
            # Cek apakah inut valid atau tidak
            Index_Keranjang = int(strKeranjang) - 1
            if(not(0 <= Index_Keranjang < len(Keranjang_Belanja))):
                raise ValueError
            
            boolValid = True
        except ValueError:
            # Input tidak valid, cetak error.
            hapusLayar()
            pindahkanKursor(8,4)
            print(warnai("Kesalahan: Nomor baris keranjang tidak valid.", Warna.merah))
            pindahkanKursor(9,4)
            print(warnai("Pastikan input adalah integer yang lebih dari 1 dan <= jumlah baris pada keranjang", Warna.merah))
            pindahkanKursor(1,1)
            continue
    
    # Cari index barang pada daftar barang
    intIndex = -1
    for i in range(len(Daftar_Barang)):
        if(Daftar_Barang[i][0] == Keranjang_Belanja[Index_Keranjang][0]):
            intIndex = i
            break
    
    # Edit stock barang di daftar barang
    Daftar_Barang[i][2] += Keranjang_Belanja[Index_Keranjang][3] # Tambah stock di Daftar Barang
    
    # Hapus keranjang belanja
    del Keranjang_Belanja[Index_Keranjang]
    return True

def pembayaran(Keranjang_Belanja, Daftar_Barang):
    """Fungsi ini akan melakukan proses pembayaran hingga pencetakan
    Struk.
    
    Masukan: 
    Keranjang_Belanja = Matriks keranjang belanja. (Reference Mode)
    Uang yanh dibayarkan (secara input)

    Keluaran:
    Mengembalikan True bila berhasil, False bila gagal. Bila fungsi ini
    berhasil dijalankan, hapus keranjang belanja dan cetak struk."""
    # Cek apakah keranjang belanja kosong apa tidak
    if len(Keranjang_Belanja) == 0:
        print(warnai("Peringatan! Keranjang belanja masih kosong", Warna.kuning))
        return False

    try:
        floatUangBayar = -1
        floatTotal = hitungBelanjaan(Keranjang_Belanja)
        hapusLayar()
        
        # Ambil data uang yang dibayarkan oleh pelanggan
        while floatUangBayar < floatTotal:
            # Cetak judul
            cetakFrame()
            printRataTengah(3, [warnai("PEMBAYARAN", Warna.cyan)], True)
            pindahkanKursor(5,4)

            # Cetak petunjuk
            print(warnai("Petunjuk : Tekan CTRL+C untuk membatalkan pembayaran.", Warna.biru))
            pindahkanKursor(6,4)

            # Cetak ringkasan biaya yang harus dibayarkan
            print("Berikut ini ringkasan biaya yang harus dibayarkan : ")
            pindahkanKursor(7,4)
            print(f"Total Harga : Rp{floatTotal:,.2f}")
            pindahkanKursor(8,4)

            # Bersihkan baris 9
            pindahkanKursor(9,4)
            print(" " * 70)

            # Terima input uang yang dibayarkan
            try:
                floatUangBayar = float(input(f"Bayar : Rp"))
            except ValueError:
                # Jika input tidak sah, cetak error.
                hapusLayar()
                pindahkanKursor(9,4)
                print(warnai(f"Kesalahan : Masukkan jumlah uang yang dibayar adalah float!",
                        Warna.merah))
                pindahkanKursor(1,1)
                continue
            
            if(floatUangBayar < floatTotal):
                # Uang tidak cukup, tampilkan error
                hapusLayar()
                pindahkanKursor(9,4)
                print(warnai(f"Kesalahan : Masukkan jumlah uang pembayaran lebih dari total belanjaan!",
                        Warna.merah))
                pindahkanKursor(1,1)
                continue
            
            # Bersihkan baris 9
            pindahkanKursor(9,4)
            print(" " * 70)

            # Tampilkan proses pembayaran
            pindahkanKursor(10,4)
            print(warnai("Memproses pembayaran...", Warna.hijau))

            # Edit setiap barang di database
            for i in Daftar_Barang:
                editBarang(i[0], Stock=i[2])
            
            # Cetak Struk
            cetakStruk(Keranjang_Belanja, floatUangBayar)

            # Hapus keranjang belanja
            for i in range(len(Keranjang_Belanja)):
                del Keranjang_Belanja[i]

            # Tahan agar form pembayaran tidak langsung tertutup
            pindahkanKursor(11,4)
            input(warnai("Pembayaran Selesai. Tekan enter untuk kembali.", Warna.hijau))
            hapusLayar()
            
            return True
    except KeyboardInterrupt:
        # User menekan CTRL+C, Pembayaran dibatalkan.
        hapusLayar()
        print(warnai("Pembayaran dibatalkan.", Warna.hijau))
        return False

def cetakTabel(Keranjang_Belanja):
    """Mencetak Keranjang Belanja"""
    # Input: Matriks keranjang belanja yang setiap itemnya
    # memiliki format berikut:
    # [Kode_Barang, Nama_Barang, Harga, Qyt, Diskon]

    # KONSTANTA JARAK
    LEBAR_NO = int(log10(len(Keranjang_Belanja) + 1)) + 2
    LEBAR_KODE = 20
    LEBAR_NAMA = 40
    LEBAR_HARGA = 15
    LEBAR_QYT = 8
    LEBAR_DISKON = 10
    LEBAR_TOTAL = 25
    C = 4*6 # Penambah supaya pas

    # Cetak kepala tabel
    print("-" * (LEBAR_NO + LEBAR_KODE + LEBAR_NAMA + LEBAR_HARGA + 
        LEBAR_QYT + LEBAR_TOTAL+ C - 2))
    print("| No.\t".expandtabs(LEBAR_NO),
          "| Kode Barang\t".expandtabs(LEBAR_KODE),
          "| Nama Barang\t".expandtabs(LEBAR_NAMA),
          "| Harga\t".expandtabs(LEBAR_HARGA),
          "| Qyt\t".expandtabs(LEBAR_QYT),
          "| Diskon  ",
          "| Total\t |".expandtabs(LEBAR_TOTAL))
    print("-" * (LEBAR_NO + LEBAR_KODE + LEBAR_NAMA + LEBAR_HARGA + 
        LEBAR_QYT + LEBAR_TOTAL+ C - 2))
    
    # Cetak badan tabel
    if len(Keranjang_Belanja) == 0:
        # Bila keranjang belanja kosong, tampilkan keranjang kosong
        print("| \tKERANJANG BELANJA KOSONG ".expandtabs((LEBAR_NO + LEBAR_KODE + LEBAR_NAMA + LEBAR_HARGA + 
        LEBAR_QYT + LEBAR_DISKON + LEBAR_TOTAL + C-13-24)//2), end="")
        print("\t|".expandtabs((LEBAR_NO + LEBAR_KODE + LEBAR_NAMA + LEBAR_HARGA + 
        LEBAR_QYT + LEBAR_DISKON + LEBAR_TOTAL + C-13-12)//2-6))
    else:
        j = 0
        for i in Keranjang_Belanja:
            print(f"| {j+1}\t".expandtabs(LEBAR_NO+4),
                  f"| {i[0]}\t ".expandtabs(LEBAR_KODE-1),
                  f"| {i[1]}\t ".expandtabs(LEBAR_NAMA-1),
                  f"| Rp{i[2]:,.0f}\t ".expandtabs(LEBAR_HARGA-1),
                  f"| {i[3]}\t ".expandtabs(LEBAR_QYT-1),
                  f"| {i[4]*100:.0f}%\t ".expandtabs(LEBAR_DISKON-1),
                  f"| Rp{i[2]*i[3]*(1-i[4]):,.0f}\t |".expandtabs(LEBAR_TOTAL))
            j += 1

    # Cetak penutup tabel
    print("-" * (LEBAR_NO + LEBAR_KODE + LEBAR_NAMA + LEBAR_HARGA + 
        LEBAR_QYT + LEBAR_TOTAL+ C - 2))

    # Cetak total belanjaan
    print(f"Total Belanjaan : Rp{hitungBelanjaan(Keranjang_Belanja):,.2f}")

def editKeranjang(Keranjang_Belanja, Daftar_Barang):
    """Prosedur ini akan mengedit keranjang belanja.
    
    Input : 
    Keranjang_Belanja = Matriks keranjang belanja. (Reference Mode)
    Daftar_Barang     = Matriks daftar barang belanjaan. (Reference Mode)
    
    Output :
    True dan perrubahan pada keranjang belanja dan daftar barang jika berhasil
    False jika gagal."""

    if len(Keranjang_Belanja) == 0:
        # Bila keranjang belanja kosong. Jangan lakukan apa-apa.
        print(warnai("Peringatan! Keranjang belanja masih kosong", Warna.kuning))
        return False

    Index_Keranjang = -1
    boolValid = False
    hapusLayar()
    while not boolValid:
        cetakFrame()

        # Cetak kepala for
        printRataTengah(3, [warnai("EDIT KERANJANG",Warna.cyan)])
        pindahkanKursor(5,4)

        # Cetak petunjuk
        print(warnai("Petunjuk : Tekan CTRL+C untuk membatalkan aksi ini dan kembali ke Form Kasir.", Warna.biru))
        pindahkanKursor(6,4)
        print(warnai("           Tulis LIHAT pada input Nomor Baris bila anda ingin melihat keranjang.\n", Warna.biru))

        # Mengambil nomor baris
        pindahkanKursor(8,4)
        strKeranjang = input("Masukkan Nomor Baris : ")
        if(strKeranjang.upper() == "LIHAT"):
            # User memilih untuk Lihat keranjang
            # Tampilkan keranjang
            hapusLayar()
            cetakTabel(Keranjang_Belanja)

            # Tahan agar tidak ketutup otomatis
            input("Tekan Enter bila anda sudah selesai. ")
            hapusLayar()
            continue
        
        # Ambil indeks keranjang yang valid
        try:
            Index_Keranjang = int(strKeranjang) - 1
            if(not(0 <= Index_Keranjang < len(Keranjang_Belanja))):
                raise ValueError
            
            boolValid = True
        except ValueError:
            # Input tidak valid, cetak error.
            hapusLayar()
            pindahkanKursor(9,4)
            print(warnai("Kesalahan: Nomor baris keranjang tidak valid.", Warna.merah))
            pindahkanKursor(1,1)
            continue

    boolSelesai = False
    while not boolSelesai:
        try:
            # Cetak judul
            hapusLayar()
            cetakFrame()
            printRataTengah(3, [warnai("EDIT KERANJANG", Warna.cyan)])
            pindahkanKursor(5,4)

            # Tampilkan data barang yg dihighlight saat ini
            print("Data keranjang yang diedit : ")
            pindahkanKursor(6,4)
            print("Nomor Baris :", Index_Keranjang + 1)
            pindahkanKursor(7,4)
            print(f"Kode Barang : {Keranjang_Belanja[Index_Keranjang][0]}")
            pindahkanKursor(8,4)
            print(f"Nama Barang : {Keranjang_Belanja[Index_Keranjang][1]}")
            pindahkanKursor(9,4)
            print(f"Qyt         : {Keranjang_Belanja[Index_Keranjang][3]}")
            pindahkanKursor(10,4)
            print(f"Harga       : {Keranjang_Belanja[Index_Keranjang][2]:,.2f}")
            pindahkanKursor(11,4)
            print("Diskon      :", Keranjang_Belanja[Index_Keranjang][4]*100, "%")
            pindahkanKursor(12,4)

            if Keranjang_Belanja[Index_Keranjang][4] > 0:
                # Bila ada diskon, warnai teks total
                floatTotal = (Keranjang_Belanja[Index_Keranjang][2] * Keranjang_Belanja[Index_Keranjang][3]\
                     * (1-Keranjang_Belanja[Index_Keranjang][4]))
                print("Total       :", 
                    warnai(f"Rp {floatTotal:,.2f} (Setelah Diskon)", Warna.kuning))
            else:
                print("Total       :", f"Rp {floatTotal:,.2f}")

            # Cetak opsi pengeditan yang tersedia
            pindahkanKursor(14,4)
            print("Opsi pengeditan yang tersedia: ")
            pindahkanKursor(15,4)
            print("1. Kode Barang")
            pindahkanKursor(16,4)
            print("2. Qyt")
            pindahkanKursor(17,4)
            print("3. Diskon")
            pindahkanKursor(18,4)
            print("4. Selesai dan kembali ke Form Kasir")
            pindahkanKursor(19,4)

            # Cetak petunjuk
            print(warnai("Peringatan! Segala perubahan yang dilakukan, tidak bisa dikembalikan.", Warna.magenta))

            # Ambil pilihan user
            pindahkanKursor(21,4)
            strPilihan = input("Pilihan : ")
            
            # Hapus baris 22
            pindahkanKursor(22,4)
            print(" " * 36)
            pindahkanKursor(22,4)


            if strPilihan == "1":
                # User memilih edit berdasarkan kode barang
                intIndex = -1
                while(intIndex == -1):
                    hapusLayar()

                    # Cetak judul
                    cetakFrame()
                    printRataTengah(3, [warnai("EDIT KODE BARANG", Warna.cyan)])
                    pindahkanKursor(5,4)

                    # Cetak petunjuk
                    print(warnai("Petunjuk : Tekan CTRL+C untuk membatalkan aksi ini.", Warna.biru))
                    pindahkanKursor(6,4)
                    print(warnai("           Tulis CARI pada input kode barang bila anda ingin mencari data barang.\n", Warna.biru))

                    # Ambil kode barang yang baru dari user
                    pindahkanKursor(8,4)
                    strKode = input("Masukkan kode barang baru : ")

                    if strKode.upper() == "CARI":
                            # User ingin mencari barang.
                            # Lakukan algoritma seperti pada pencarian di form barang
                            try:
                                boolSelesai = False
                                hapusLayar()
                                while not boolSelesai:
                                    printRataTengah(2, [warnai("PENCARI BARANG", Warna.cyan)], True)
                                    print()
                                    print("Apa yang anda ingin lakukan?")
                                    print("1. Mencari detail barang dengan Kode Barang")
                                    print("2. Mencari detail barang dengan Nama Barang")
                                    print("3. Kembali")
                                    print(warnai("Petunjuk : Tekan CTRL+C jika ingin membatalkan aksi.\n",Warna.biru))
            
                                    strCmd = input("Pilihan aksi : ")
                                    if strCmd == "1":
                                        print()
                                        print("Masukkan kode barang atau subset kode barang yang ingin dicari.")
                                        strKode = input("Kode barang : ")
            
                                        matHasil = cariRegex(strKode, Daftar_Barang, 0)
                                        hapusLayar()
            
                                        printRataTengah(2, [warnai("HASIL PENCARIAN", Warna.cyan)], True)
                                        print()
                                        print(f"Berikut ini adalah hasil pencarian. Didapatkan {len(matHasil)} data.")
                                        cetakTabelBarang(matHasil)
            
                                        input("\nTekan Enter untuk kembali.")
                                        hapusLayar()
                                    elif strCmd == "2":
                                        print()
                                        print("Masukkan nama barang atau subset nama barang yang ingin dicari.")
                                        strKode = input("Nama Barang : ")
            
                                        matHasil = cariRegex(strKode, Daftar_Barang, 1)
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
                                        print(warnai("Error! Masukan angka antara 1 s.d 4 saja.", Warna.merah))
                            except KeyboardInterrupt:
                                print(warnai("Pemberitahuan : Aksi dibatalkan..", Warna.hijau))
                            finally:
                                hapusLayar()
                    
                    # Cari barang apakah ada
                    for i in range(len(Daftar_Barang)):
                        if(Daftar_Barang[i][0] == strKode):
                            intIndex = i
                            break
                        
                    if(intIndex == -1):
                        # Jika tidak ada barangnya, cetak error
                        pindahkanKursor(9,4)
                        print(warnai("Kesalahan: Kode barang tidak ditemukan.", Warna.merah))
                
                # Cari data barang di daftar barang
                intIndexSebelum = -1
                for i in range(len(Daftar_Barang)):
                        if(Daftar_Barang[i][0] == Keranjang_Belanja[Index_Keranjang][0]):
                            intIndexSebelum = i
                            break
                
                # Edit data barang di keranjang belanja
                Keranjang_Belanja[Index_Keranjang][0] = strKode
                Keranjang_Belanja[Index_Keranjang][1] = Daftar_Barang[intIndex][1]
                Keranjang_Belanja[Index_Keranjang][2] = Daftar_Barang[intIndex][3]

                # Edit data barang di daftar barang
                Daftar_Barang[intIndex][2] -= Keranjang_Belanja[Index_Keranjang][3]
                Daftar_Barang[intIndexSebelum][2] += Keranjang_Belanja[Index_Keranjang][3]
                # pindahkanKursor(9,4)
            elif strPilihan == "2":
                # User memilih mengubah jumlah barang
                boolOK = False
                while not boolOK:
                    pindahkanKursor(22,4)
                    try:
                        intJumlahBaru = int(input("Masukan jumlah barang yang baru : "))

                        # Mencari indeks barang pada daftar barang
                        intIndexSebelum = -1
                        for i in range(len(Daftar_Barang)):
                            if(Daftar_Barang[i][0] == Keranjang_Belanja[Index_Keranjang][0]):
                                intIndexSebelum = i
                                break

                        # Bersihkan baris 23
                        pindahkanKursor(23,4)
                        print(" " * 50)
                        pindahkanKursor(23,4)

                        if intJumlahBaru > (Daftar_Barang[intIndexSebelum][2] + Keranjang_Belanja[Index_Keranjang][3]):
                            # Stock baru tidak mencukupi
                            print(warnai("Keterangan: Stock Barang tidak mencukupi.", Warna.kuning))
                        else:
                            # Ubah Qyt di keranjang belanja dan 
                            # stok barang di daftar barang
                            Daftar_Barang[intIndexSebelum][2] += Keranjang_Belanja[Index_Keranjang][3]
                            Keranjang_Belanja[Index_Keranjang][3] = intJumlahBaru
                            Daftar_Barang[intIndexSebelum][2] -= Keranjang_Belanja[Index_Keranjang][3]
                            boolOK = True # Selesai

                    except ValueError:
                        # Bila input error, tampilkan error
                        pindahkanKursor(23,4)
                        print(" " * 50)
                        pindahkanKursor(23,4)
                        print(warnai("Error: Masukkan input berupa bilangan bulat.", Warna.merah))
            elif strPilihan == "3":
                # User memilih mengubah diskon
                boolOK = False
                while not boolOK:
                    pindahkanKursor(22,4)

                    # Ambil input diskon yang valid
                    # yaitu bilangan bulat antara 0 s.d. 100 (inklusif)
                    try:
                        intDiskon = int(input("Masukkan Diskon (dalam %) : "))
                        if(0 <= intDiskon <= 100):
                            # Bila benar, ubah diskon di keranjang belanja
                            # Ubah keranjang belanja
                            Keranjang_Belanja[Index_Keranjang][4] = intDiskon / 100
                            
                            # Ubah diskon selessai
                            boolOK = True
                        else:
                            raise ValueError
                    except ValueError:
                        # Bila tidak sesuai tampilkan error
                        pindahkanKursor(22,4)
                        print(" " * 70)
                        pindahkanKursor(22,4)
                        print(warnai("Error: Masukkan input berupa bilangan bulat antara 0 s.d. 100.", Warna.merah))

            elif strPilihan == "4":
                # Kembali ke form pembelian
                hapusLayar()
                boolSelesai = True
            else:
                # Input tidak valid. Tampilkan error
                print(warnai("Masukan angka mulai dari 1 s.d. 5.", Warna.merah))

        except KeyboardInterrupt:
            # User menekann CTRL+C. Aksi dibatalkan
            hapusLayar()
            pindahkanKursor(2,2)
            print(warnai("Aksi dibatalkan.", Warna.hijau))

def formPembelanjaan():
    """Fungsi ini akan menampilkan form Pembelanjaan
    
    Form pembelanjaan adalah form yang digunakan saat penjaga 
    kasir menginputkan barang yang akan dijual kepada pembeli.
    
    Pada form ini juga akan ada opsi untuk mencetak barang"""
    
    # Variabel Global
    # Matriks daftar barang
    # Urutan setiap elemen baris : 
    # [Kode_Barang, Nama_Barang, Stok, Harga]
    matDaftarBarang = lihatBarang()

    # Matriks Keranjang Belanja
    # Urutan setiap elemen baris:
    # [Kode_Barang, Nama_Barang, Harga, Qyt, Diskon]
    matKeranjangBelanja = []

    hapusLayar()
    boolMenuUtama = False

    while(not boolMenuUtama):
        try:
            # Cetak judul form
            printRataTengah(2, [warnai("FORM KASIR", Warna.cyan)], True)
            print()

            # Cetak Tanggal sekarang
            dateNow = datetime.datetime.now()
            print(f"Tanggal : {(dateNow.day)}-{dateNow.month}-{dateNow.year}")
            print()

            cetakTabel(matKeranjangBelanja)

            # Cetak pilihan aksi
            print()
            print("Pilihan Aksi : ")
            print("1. Tambah barang ke keranjang.")
            print("2. Hapus barang di keranjang.")
            print("3. Edit barang di keranjang")
            print("4. Bayar")
            print("5. Kembali ke menu utama.")

            # Cetak petunjuk
            print(warnai("\nCatatan : Jika anda ingin membatalkan aksi yang anda lakukan, tekan CTRL+C.",Warna.biru))
            
            # Ambil pilihan input aksi
            strPilihan = input("Pilihan Aksi : ")

            if strPilihan == "1":
                # Tambah barang ke keranjang
                tambahKeranjang(matKeranjangBelanja, matDaftarBarang)
                hapusLayar()
            elif strPilihan == "2":
                # Kurangi barang ke keranjang belanja
                if not kurangKeranjang(matKeranjangBelanja, matDaftarBarang):
                    # Keranjang masih kosong
                    hapusLayar()
                    print(warnai("Peringatan! Keranjang belanja masih kosong", Warna.kuning))
                else:
                    hapusLayar()
            elif strPilihan == "3":
                # Edit barang pada keranjang
                hapusLayar()
                editKeranjang(matKeranjangBelanja, matDaftarBarang)
            elif strPilihan == "4":
                # Lakukan pembayaran
                hapusLayar()
                pembayaran(matKeranjangBelanja, matDaftarBarang)
            elif strPilihan == "5":
                # Kembali ke menu utama
                hapusLayar()
                boolMenuUtama = True # Keluar
            else:
                # Input tidak valid
                hapusLayar()
                print(warnai("Kesalahan : Masukkan angka hanya antara 1 s.d. 5 saja.", Warna.merah))

        except KeyboardInterrupt:
            # User menekan CTRL+C. Aksi dibatalkan.
            hapusLayar()
            print(warnai("Pemberitahuan : Aksi dibatalkan..", Warna.hijau))