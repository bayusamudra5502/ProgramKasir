# Program Kasir
Program Kasir adalah program yang dibuat untuk mempermudah perhitungan pembelanjaan pada pasar swalayan atau warung-warung. Aplikasi ini dibangun atas program python. Latar belakang program ini dibuat adalah untuk mempermudah para penjaga toko menghitung belajaan para pelanggannya. 


## Fitur
Beberapa fitur yang ada pada program ini diantaranya sebagai berikut:

### Fitur Login
Fitur login adalah fitur untuk menjaga pengaksesan dari pihak yang tidak  memiliki akses. Hanya penjaga toko yang terdaftar sebagai pengguna yang dapat mengakses aplikasi ini.

### Fitur Kasir
Fitur kasir adalah tempat dimana para penjaga toko menginputkan barang-barang yang akan dibeli oleh pelanggannya. Barang yang diinputkan pasti harus ada stoknya. Setelah melalui penginputan barang, para penjaga toko akan dihadapkan dengan kalkulator perhitungan kembalian. Disini, para penjaga toko harus menginputkan jumlah uang yang dibayarkan oleh pelanggan. Jika uang kurang, maka transaksi tidak bisa dilanjutkan, dan akan terus diulang hingga uang cukup. Pada fitur ini juga akan disediakan opsi untuk mencetak struk. Setelah proses transaksi selesai, stok barang akan diupdate otomatis.

### Fitur Barang
Fitur ini akan memperlihatkan daftar barang yang ada pada toko. Pengguna dapat menambahkan, mengedit, menghapus barang yang ada pada program ini.

### Fitur Pengguna
Fitur ini akan memperlihatkan daftar pengguna yang ada pada toko. Pengguna dapat menambahkan pengguna lain, mengedit kata sandi semua pengguna, dan menghapus pengguna lain.

### Fitur Menu
Fitur ini untuk mempermudah pengguna mengakses fitur lain yang ada pada program ini.

## Prasyarat Menjalankan program
Prasyarat yang perlu dimiliki untuk menjalankan program ini adalah:
* Menggunakan Microsoft Windows 10
* Terinstall Windows Terminal untuk hasil yang baik. Unduh dengan [menekan ini.](https://www.microsoft.com/en-us/p/windows-terminal/9n0dx20hk701?activetab=pivot:overviewtab) (opsional)
* Terinstall Python minimal python versi 3.9.0. Unduh [disini](https://www.python.org/downloads/release/python-390/).
* Terinstall pip minimal versi 20.2.4. Anda dapat cek dengan menjalankan perintah `pip --version`
* Terinstall pustaka berikut:
    1. Colorama versi 0.4.4
    2. Termcolor versi 1.1.0

**Keterangan :** Untuk memasang pustaka diatas, ada dapat menjalankan perintah ini pada folder teratas program: `pip install -r requirements.txt`

## Cara Menjalankan Program
Untuk menjalankan program ini, anda hanya perlu menjalankan perintah ini:
`python main.py`

## Cara Berkontribusi
Disini terdapat beberapa folder penting, yaitu:
1. Folder `forms` berisi komponen fitur yang ada pada program. Folder inilah yang akan kita garap bersama untuk membuat program ini lebih baik. Pada folder ini terdiri dari
    * File `barang.py` yang berisi fitur barang pada program
    * File `loading.py` yang berfungsi menampilkan loading pada program saat dibuka
    * File `login.py` yang berisi dari fitur login pada program
    * File `menu.py` yang berisi fitur menu utama pada program
    * File `pembelanjaan.py` yang berisi fitur kasir yang akan digunakan dalam transaksi.
    * File `pengguna.py` yang berisi fitur pengguna pada program.
2. Folder `libs` berisi fungsi-fungsi utama yang ada pada program. Folder ini tidak perlu dipelajari, karena berisi hal-hal teknis seperti hubungan terhadap database dan OS.