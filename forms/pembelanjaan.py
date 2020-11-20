## FORM PEMBELANJAAN
""" Form yang mengatur mengenai segala yang berkaitan dengan
pembelanjaan
"""
from libs.library import *
from forms.barang import cetakTabel as cetakTabelBarang

# Gunakan fungsi berikut untuk memudahkan:
# editBarang(Kode_Barang, Nama_Barang = None, Stock = None, Harga = None)
#   untuk edit data barang
#
# YG SUDAH DIDEBUG:
# 1. PEMBAYARAN
#       - Hitung Belanjaan
# 2. TAMBAH BARANG
#       - CETAK STRUK
# 3. CETAK TABEL
# 4. HAPUS BARANG


def hitungBelanjaan(Keranjang_Belanja):
    """Menghitung total belanjaan.
    
    Masukan:
    Keranjang_Belanja = Matriks keranjang belanja."""
    floatSum = 0.0
    for i in Keranjang_Belanja:
        floatSum += i[2]*i[3]*(1-i[4])
    
    return floatSum

def cetakStruk(Keranjang_Belanja, Uang_Dibayarkan):
    """Cetak Struk menjadi file.
    
    Masukan:
    Keranjang_Belanja = Matriks keranjang belanja.
    Uang_Dibayarkan = Besar uang yang dibayarkan."""
    try:
        now = datetime.datetime.now()
        file = open("struk\\"+ now.strftime("Struk_%d-%m-%Y_%H-%M-%S") +".txt","w")
        print("=================", file=file)
        print("STRUK PEMBAYARAN", file=file)
        print("=================", file=file)
        print(f"Tanggal\t: {now.day}-{now.month}-{now.year}", file=file)
        print(f"Waktu\t: {now.hour}:{now.minute}:{now.second}", file=file)
        print("",file=file)
        for i in Keranjang_Belanja:
            print(f"{i[0]}\t".expandtabs(14), f"{i[1]}\t".expandtabs(30), end="", file=file)
            print(f"Rp{i[2]}\t".expandtabs(17), f"x {i[3]}", f"= {i[2]*i[3]*(1-i[4])}", end="", file=file)
            if i[4] != 0:
                print(f" (Disc {i[4]*100:.0f}%)", end="", file=file)
            print(file=file)
        
        floatTotal = hitungBelanjaan(Keranjang_Belanja)
        print("\nTotal     : Rp", f"{floatTotal:,.2f}", sep="", file=file)
        print("Bayar     : Rp", f"{Uang_Dibayarkan:,.2f}", sep="", file=file)
        print("Kembalian : Rp", f"{Uang_Dibayarkan-floatTotal:,.2f}", sep="", file=file)
        print(file=file)
        print("Terima Kasih :D", file=file)
        return True

    except IOError as err:
        # Bila terjadi kegagalan dalam pencetakan struk
        print(warnai("Gagal membuat stuk pembayaran.", Warna.merah))
        return False

def tambahKeranjang(Keranjang_Belanja, Daftar_Barang):
    """Fungsi ini akan mengubah Keranjang Belanja.
    
    Input : 
    Keranjang_Belanja = Matriks keranjang belanja. (Reference Mode)
    Daftar_Barang     = Matriks daftar barang belanjaan. (Reference Mode)

    Keluaran:
    True bila berhasil, False bila gagal."""
    
    # Cari barang
    intIndex = -1
    hapusLayar()
    while(intIndex == -1):
        cetakFrame()
        printRataTengah(3, [warnai("TAMBAH KERANJANG", Warna.cyan)])
        pindahkanKursor(5,4)
        print(warnai("Petunjuk : Tekan CTRL+C untuk membatalkan aksi ini.", Warna.biru))
        pindahkanKursor(6,4)
        print(warnai("           Tulis CARI pada input kode barang bila anda ingin mencari data barang.\n", Warna.biru))

        pindahkanKursor(8,4)
        strKode = input("Masukkan kode barang : ")
        if strKode.upper() == "CARI":
                try:
                    boolSelesai = False
                    hapusLayar()
                    while not boolSelesai:
                        printRataTengah(2, [warnai("PENCARI BARANG", Warna.cyan)], True)
                        print()
                        print("Apa yang anda ingin lakukan?")
                        print("1. Mencari detail barang dengan Kode Barang")
                        print("2. Mencari detail barang dengan Nama Barang")
                        print("3. Kembali ke Form Tambah Keranjang")
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
                            cetakTabelBarang(matHasil)
                            
                            input("\nTekan Enter untuk kembali.")
                            hapusLayar()
                        elif strCmd == "3":
                            boolSelesai = True
                        else:
                            hapusLayar()
                            print(warnai("Error! Masukan angka antara 1 s.d 3 saja.", Warna.merah))
                except KeyboardInterrupt:
                    print(warnai("Pemberitahuan : Aksi dibatalkan..", Warna.hijau))
                finally:
                    hapusLayar()
        
        for i in range(len(Daftar_Barang)):
            if(Daftar_Barang[i][0] == strKode):
                intIndex = i
                break
        
        
        if(intIndex == -1):
            hapusLayar()
            pindahkanKursor(9,4)
            print(warnai("Kesalahan: Kode barang tidak ditemukan.", Warna.merah))
            pindahkanKursor(1,1)

    pindahkanKursor(9,4)
    print(" " * 40)
    intQyt = 0

    while intQyt <= 0:
        pindahkanKursor(9,4)
        try:
            intQyt = int(input("Masukkan banyak yang mau dibeli : "))
            if(intQyt <= 0):
                raise ValueError
        except ValueError:
            pindahkanKursor(10,4)
            print(warnai("Error! Massukan harus berupa integer lebih dari 0.", Warna.merah))
            continue

        pindahkanKursor(10,4)
        print(" " * 50)    

        if(Daftar_Barang[i][2] < intQyt):
            intQyt = -1
            pindahkanKursor(10,4)
            print(warnai("Peringatan: Stock tidak mencukupi.", Warna.kuning))
    
    pindahkanKursor(10,4)
    print(" "*50)

    intDiskon = -1
    while intDiskon == -1:
        pindahkanKursor(10,4)
        try:
            intDiskon = int(input("Masukkan jumlah diskon (dalam %) : "))
        except ValueError:
            pindahkanKursor(11,4)
            print(" "*60)
            pindahkanKursor(11,4)
            print(warnai("Error! Massukan input berupa integer.", Warna.merah))
            continue

        pindahkanKursor(11,4)
        print(" " * 37)    

        if(not(0 <= intDiskon <= 100)):
            intDiskon = -1
            pindahkanKursor(11,4)
            print(" "*60)
            pindahkanKursor(11,4)
            print(warnai("Kesalahan: Diskon harus diantara 0 s.d. 100.", Warna.merah))
        else:
            Daftar_Barang[i][2] -= intQyt # Mengurangi jumlah stock di daftar barang
            Keranjang_Belanja.append([Daftar_Barang[intIndex][0], Daftar_Barang[intIndex][1], 
                              Daftar_Barang[intIndex][3], intQyt, intDiskon / 100])

def kurangKeranjang(Keranjang_Belanja, Daftar_Barang):
    """Mengurangi barang pada keranjang
    
    Input : 
    Keranjang_Belanja = Matriks keranjang belanja. (Reference Mode)
    Daftar_Barang     = Matriks daftar barang belanjaan. (Reference Mode)

    Keluaran:
    True bila berhasil, False bila gagal."""

    if len(Keranjang_Belanja) == 0:
        return False

    boolValid = False
    hapusLayar()
    while not boolValid:
        cetakFrame()
        printRataTengah(3, [warnai("KURANGI KERANJANG", Warna.cyan)])
        pindahkanKursor(4,4)
        print(warnai("Petunjuk : Tekan CTRL+C untuk membatalkan aksi ini.", Warna.biru))
        pindahkanKursor(5,4)
        print(warnai("           Tulis LIHAT pada input Nomor Baris bila anda ingin melihat keranjang.\n", Warna.biru))

        pindahkanKursor(7,4)
        strKeranjang = input("Masukkan Nomor Baris : ")
        if(strKeranjang.upper() == "LIHAT"):
            hapusLayar()
            cetakTabel(Keranjang_Belanja)
            input("Tekan Enter bila anda sudah selesai. ")
            hapusLayar()
            continue
        
        try:
            Index_Keranjang = int(strKeranjang) - 1
            if(not(0 <= Index_Keranjang < len(Keranjang_Belanja))):
                raise ValueError
            
            boolValid = True
        except ValueError:
            hapusLayar()
            pindahkanKursor(8,4)
            print(warnai("Kesalahan: Nomor baris keranjang tidak valid.", Warna.merah))
            pindahkanKursor(9,4)
            print(warnai("Pastikan input adalah integer yang lebih dari 1 dan <= jumlah baris pada keranjang", Warna.merah))
            pindahkanKursor(1,1)
            continue
    
    # Cari barang
    intIndex = -1
    for i in range(len(Daftar_Barang)):
        if(Daftar_Barang[i][0] == Keranjang_Belanja[Index_Keranjang][0]):
            intIndex = i
            break
    
    Daftar_Barang[i][2] += Keranjang_Belanja[Index_Keranjang][3] # Tambah stock di Daftar Barang
    del Keranjang_Belanja[Index_Keranjang]
    return True

def pembayaran(Keranjang_Belanja, Daftar_Barang):
    """Fungsi ini akan melakukan proses pembayaran hingga pencetakan
    Struk.
    
    Masukan: 
    Keranjang_Belanja = Matriks keranjang belanja. (Reference Mode)

    Keluaran:
    Mengembalikan True bila berhasil, False bila gagal."""
    if len(Keranjang_Belanja) == 0:
        print(warnai("Peringatan! Keranjang belanja masih kosong", Warna.kuning))
        return False

    try:
        floatUangBayar = -1
        floatTotal = hitungBelanjaan(Keranjang_Belanja)
        hapusLayar()
        while floatUangBayar < floatTotal:
            cetakFrame()
            printRataTengah(3, [warnai("PEMBAYARAN", Warna.cyan)], True)
            pindahkanKursor(5,4)
            print(warnai("Petunjuk : Tekan CTRL+C untuk membatalkan pembayaran.", Warna.biru))
            pindahkanKursor(6,4)
            print("Berikut ini ringkasan biaya yang harus dibayarkan : ")
            pindahkanKursor(7,4)
            print(f"Total Harga : Rp{floatTotal:,.2f}")
            pindahkanKursor(8,4)
            try:
                floatUangBayar = float(input(f"Bayar : Rp"))
            except ValueError:
                hapusLayar()
                pindahkanKursor(9,4)
                print(warnai(f"Kesalahan : Masukkan jumlah uang yang dibayar adalah float!",
                        Warna.merah))
                pindahkanKursor(1,1)
                continue

            if(floatUangBayar < floatTotal):
                hapusLayar()
                pindahkanKursor(9,4)
                print(warnai(f"Kesalahan : Masukkan jumlah uang pembayaran lebih dari total belanjaan!",
                        Warna.merah))
                pindahkanKursor(1,1)
                continue
            
            pindahkanKursor(9,4)
            print(" " * 70)

            pindahkanKursor(10,4)
            print(warnai("Memproses pembayaran...", Warna.hijau))
            for i in Daftar_Barang:
                editBarang(i[0], Stock=i[2])
            
            cetakStruk(Keranjang_Belanja, floatUangBayar)

            for i in range(len(Keranjang_Belanja)):
                del Keranjang_Belanja[i]

            pindahkanKursor(11,4)
            input(warnai("Pembayaran Selesai. Tekan enter untuk kembali.", Warna.hijau))
            hapusLayar()
            
            return True
    except KeyboardInterrupt:
        hapusLayar()
        print(warnai("Pembayaran dibatalkan.", Warna.hijau))
        return False

def cetakTabel(Keranjang_Belanja):
    """Mencetak Keranjang Belanja"""
    # Matriks Keranjang Belanja
    # Urutan setiap elemen baris:
    # [Kode_Barang, Nama_Barang, Harga, Qyt, Diskon]

    # KONSTANTA
    LEBAR_NO = int(log10(len(Keranjang_Belanja) + 1)) + 2
    LEBAR_KODE = 20
    LEBAR_NAMA = 40
    LEBAR_HARGA = 15
    LEBAR_QYT = 8
    LEBAR_DISKON = 10
    LEBAR_TOTAL = 25
    C = 4*6 # Penambah supaya pas

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
    
    if len(Keranjang_Belanja) == 0:
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

    print("-" * (LEBAR_NO + LEBAR_KODE + LEBAR_NAMA + LEBAR_HARGA + 
        LEBAR_QYT + LEBAR_TOTAL+ C - 2))
    print(f"Total Belanjaan : Rp{hitungBelanjaan(Keranjang_Belanja):,.2f}")

def editKeranjang(Keranjang_Belanja, Daftar_Barang):
    """Prosedur ini akan mengedit keranjang belanja.
    
    Input : 
    Keranjang_Belanja = Matriks keranjang belanja. (Reference Mode)
    Daftar_Barang     = Matriks daftar barang belanjaan. (Reference Mode)"""

    if len(Keranjang_Belanja) == 0:
        print(warnai("Peringatan! Keranjang belanja masih kosong", Warna.kuning))
        return False

    Index_Keranjang = -1
    boolValid = False
    hapusLayar()
    while not boolValid:
        cetakFrame()
        printRataTengah(3, [warnai("EDIT KERANJANG",Warna.cyan)])
        pindahkanKursor(5,4)
        print(warnai("Petunjuk : Tekan CTRL+C untuk membatalkan aksi ini dan kembali ke Form Kasir.", Warna.biru))
        pindahkanKursor(6,4)
        print(warnai("           Tulis LIHAT pada input Nomor Baris bila anda ingin melihat keranjang.\n", Warna.biru))

        pindahkanKursor(8,4)
        strKeranjang = input("Masukkan Nomor Baris : ")
        if(strKeranjang.upper() == "LIHAT"):
            hapusLayar()
            cetakTabel(Keranjang_Belanja)
            input("Tekan Enter bila anda sudah selesai. ")
            hapusLayar()
            continue
        
        try:
            Index_Keranjang = int(strKeranjang) - 1
            if(not(0 <= Index_Keranjang < len(Keranjang_Belanja))):
                raise ValueError
            
            boolValid = True
        except ValueError:
            hapusLayar()
            pindahkanKursor(9,4)
            print(warnai("Kesalahan: Nomor baris keranjang tidak valid.", Warna.merah))
            pindahkanKursor(1,1)
            continue

    boolSelesai = False
    while not boolSelesai:
        try:
            hapusLayar()
            cetakFrame()
            printRataTengah(3, [warnai("EDIT KERANJANG", Warna.cyan)])
            pindahkanKursor(5,4)
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
                floatTotal = (Keranjang_Belanja[Index_Keranjang][2] * Keranjang_Belanja[Index_Keranjang][3]\
                     * (1-Keranjang_Belanja[Index_Keranjang][4]))
                print("Total       :", 
                    warnai(f"Rp {floatTotal:,.2f} (Setelah Diskon)", Warna.kuning))
            else:
                print("Total       :", f"Rp {floatTotal:,.2f}")

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
            print(warnai("Peringatan! Segala perubahan yang dilakukan, tidak bisa dikembalikan.", Warna.magenta))

            pindahkanKursor(21,4)
            strPilihan = input("Pilihan : ")
            
            pindahkanKursor(22,4)
            print(" " * 36)
            pindahkanKursor(22,4)

            if strPilihan == "1":
                intIndex = -1
                while(intIndex == -1):
                    hapusLayar()
                    cetakFrame()
                    printRataTengah(3, [warnai("EDIT KODE BARANG", Warna.cyan)])
                    pindahkanKursor(5,4)
                    print(warnai("Petunjuk : Tekan CTRL+C untuk membatalkan aksi ini.", Warna.biru))
                    pindahkanKursor(6,4)
                    print(warnai("           Tulis CARI pada input kode barang bila anda ingin mencari data barang.\n", Warna.biru))
            
                    pindahkanKursor(8,4)
                    strKode = input("Masukkan kode barang baru : ")
                    if strKode.upper() == "CARI":
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
                    
                    for i in range(len(Daftar_Barang)):
                        if(Daftar_Barang[i][0] == strKode):
                            intIndex = i
                            break
                        
                    if(intIndex == -1):
                        pindahkanKursor(9,4)
                        print(warnai("Kesalahan: Kode barang tidak ditemukan.", Warna.merah))
                
                intIndexSebelum = -1
                for i in range(len(Daftar_Barang)):
                        if(Daftar_Barang[i][0] == Keranjang_Belanja[Index_Keranjang][0]):
                            intIndexSebelum = i
                            break
                
                Keranjang_Belanja[Index_Keranjang][0] = strKode
                Keranjang_Belanja[Index_Keranjang][1] = Daftar_Barang[intIndex][1]
                Keranjang_Belanja[Index_Keranjang][2] = Daftar_Barang[intIndex][3]
                Daftar_Barang[intIndex][2] -= Keranjang_Belanja[Index_Keranjang][3]
                Daftar_Barang[intIndexSebelum][2] += Keranjang_Belanja[Index_Keranjang][3]
                # pindahkanKursor(9,4)
            elif strPilihan == "2":
                boolOK = False
                while not boolOK:
                    pindahkanKursor(22,4)
                    try:
                        intJumlahBaru = int(input("Masukan jumlah barang yang baru : "))

                        intIndexSebelum = -1
                        for i in range(len(Daftar_Barang)):
                            if(Daftar_Barang[i][0] == Keranjang_Belanja[Index_Keranjang][0]):
                                intIndexSebelum = i
                                break
                        pindahkanKursor(23,4)
                        print(" " * 50)
                        pindahkanKursor(23,4)

                        if intJumlahBaru > (Daftar_Barang[intIndexSebelum][2] + Keranjang_Belanja[Index_Keranjang][3]):
                            print(warnai("Keterangan: Stock Barang tidak mencukupi.", Warna.kuning))
                        else:
                            Daftar_Barang[intIndexSebelum][2] += Keranjang_Belanja[Index_Keranjang][3]
                            Keranjang_Belanja[Index_Keranjang][3] = intJumlahBaru
                            Daftar_Barang[intIndexSebelum][2] -= Keranjang_Belanja[Index_Keranjang][3]
                            boolOK = True

                    except ValueError:
                        pindahkanKursor(23,4)
                        print(" " * 50)
                        pindahkanKursor(23,4)
                        print(warnai("Error: Masukkan input berupa bilangan bulat.", Warna.merah))
            elif strPilihan == "3":
                boolOK = False
                while not boolOK:
                    pindahkanKursor(22,4)
                    try:
                        intDiskon = int(input("Masukkan Diskon (dalam %) : "))
                        if(0 <= intDiskon <= 100):
                            boolOK = True
                            Keranjang_Belanja[Index_Keranjang][4] = intDiskon / 100
                        else:
                            raise ValueError
                    except ValueError:
                        pindahkanKursor(22,4)
                        print(" " * 70)
                        pindahkanKursor(22,4)
                        print(warnai("Error: Masukkan input berupa bilangan bulat antara 0 s.d. 100.", Warna.merah))
            elif strPilihan == "4":
                hapusLayar()
                boolSelesai = True
            else:
                print(warnai("Masukan angka mulai dari 1 s.d. 5.", Warna.merah))

        except KeyboardInterrupt:
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
            printRataTengah(2, [warnai("FORM KASIR", Warna.cyan)], True)
            print()

            # Cetak Tanggal sekarang
            dateNow = datetime.datetime.now()
            print(f"Tanggal : {(dateNow.day)}-{dateNow.month}-{dateNow.year}")
            print()
            cetakTabel(matKeranjangBelanja)
            print()
            print("Pilihan Aksi : ")
            print("1. Tambah barang ke keranjang.")
            print("2. Hapus barang di keranjang.")
            print("3. Edit barang di keranjang")
            print("4. Bayar")
            print("5. Kembali ke menu utama.")
            print(warnai("\nCatatan : Jika anda ingin membatalkan aksi yang anda lakukan, tekan CTRL+C.",Warna.biru))
            strPilihan = input("Pilihan Aksi : ")

            if strPilihan == "1":
                tambahKeranjang(matKeranjangBelanja, matDaftarBarang)
                hapusLayar()
            elif strPilihan == "2":
                if not kurangKeranjang(matKeranjangBelanja, matDaftarBarang):
                    hapusLayar()
                    print(warnai("Peringatan! Keranjang belanja masih kosong", Warna.kuning))
                else:
                    hapusLayar()
            elif strPilihan == "3":
                hapusLayar()
                editKeranjang(matKeranjangBelanja, matDaftarBarang)
            elif strPilihan == "4":
                hapusLayar()
                pembayaran(matKeranjangBelanja, matDaftarBarang)
            elif strPilihan == "5":
                hapusLayar()
                boolMenuUtama = True
            else:
                hapusLayar()
                print(warnai("Kesalahan : Masukkan angka hanya antara 1 s.d. 5 saja.", Warna.merah))

        except KeyboardInterrupt:
            hapusLayar()
            print(warnai("Pemberitahuan : Aksi dibatalkan..", Warna.hijau))