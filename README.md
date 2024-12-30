# Proyek Analisis Data Rental Sepeda
Aplikasi ini adalah sebuah dashboard interaktif berbasis Streamlit yang digunakan untuk menganalisis data rental sepeda. Aplikasi ini memungkinkan pengguna untuk memfilter data berdasarkan beberapa parameter seperti musim (season), hari (weekday), dan jam (hour) serta menampilkan visualisasi data seperti grafik bar dan garis.

## Fitur Utama
1. Filter Data Interaktif:
    Filter data berdasarkan musim, hari, jam, dan status hari kerja.
2. Tabel Data:
    Menampilkan data hasil filtering dalam bentuk tabel.
3. Statistik Ringkas:
    Menampilkan statistik deskriptif dari data yang telah difilter.
4. Visualisasi Data:
    Grafik Bar: Menampilkan total rental sepeda berdasarkan jam.
    Grafik Garis: Menampilkan total rental sepeda berdasarkan hari.

## Instalasi
### Clone Repository
Jika proyek ini berada di GitHub, clone repository ke komputer
```
git clone <URL-repo>
cd SubmissionProyekAnalisisDataDicoding
```
### Gunakan Conda untuk membuat environtment
Conda
```
conda create --name bike-ds python=3.9 -y
conda activate bike-ds
pip install -r requirements.txt
```
### Tambahkan Dataset
Pastikan file dataset alldata.csv berada di folder

## Menajalankan Aplikasi
```
streamlit run dashboard.py
```

## Penggunaan
Filter Data: Gunakan sidebar untuk memilih filter seperti musim, hari, jam, atau status hari kerja.
Tabel Data: Lihat data hasil filtering pada tabel di halaman utama.
Visualisasi: Analisis data menggunakan grafik bar dan garis untuk memahami pola rental sepeda.

## Depedensi
Daftar library yang digunakan dalam proyek ini:
  - pandas: Untuk manipulasi data.
  - matplotlib: Untuk membuat visualisasi grafik.
  - streamlit: Untuk membangun dashboard interaktif.
Instal semua dependensi dengan perintah:
```
pip install -r requirements.txt
```
## Lisensi
Proyek ini menggunakan lisensi MIT. Anda bebas untuk menggunakan, memodifikasi, dan mendistribusikan proyek ini selama mencantumkan kredit kepada pengembang asli.

## Kontak
Jika ada pertanyaan atau masalah terkait proyek ini, silakan hubungi:
Nama: Azzam Muhammad Alghozy
Email: azzam.alghozy04@gmail.com
GitHub: Azzamzy
