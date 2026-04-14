# RGB to Grayscale Converter

Aplikasi berbasis web menggunakan **Streamlit** untuk melakukan konversi citra warna (RGB) menjadi citra berskala abu-abu (*grayscale*). Program ini dibuat untuk mendemonstrasikan implementasi algoritma pengolahan citra digital di tingkat piksel tanpa menggunakan fungsi otomatis dari library pengolah citra.

## Link Web


## Fitur Utama
* **Upload Citra**: Mendukung format `.jpg`, `.jpeg`, dan `.png`.
* **Algoritma Murni**: Proses konversi dilakukan secara manual menggunakan perulangan (*looping*) pada setiap piksel.
* **Metode Luminosity**: Menggunakan standar bobot persepsi manusia (ITU-R BT.601) untuk hasil yang lebih akurat secara visual.
* **Side-by-Side Comparison**: Menampilkan perbandingan gambar asli dan hasil secara langsung.

## Algoritma yang Digunakan
Program ini mengimplementasikan rumus **Luminosity** untuk menghitung nilai intensitas abu-abu:

`Gray = 0.299·R + 0.587·G + 0.114·B`

Secara manual untuk memahami struktur data citra sebagai matriks tiga dimensi (lebar, tinggi, kanal warna) dan bagaimana operasi aritmatika diterapkan pada tiap elemennya.
