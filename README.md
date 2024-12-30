
Berikut adalah isi file README.md untuk proyek Streamlit Anda. File ini menjelaskan tentang proyek, cara menginstalasi, menjalankan aplikasi, serta informasi lainnya untuk membantu pengguna memahami dan menggunakan aplikasi.

Proyek Analisis Data Rental Sepeda
Aplikasi ini adalah sebuah dashboard interaktif berbasis Streamlit yang digunakan untuk menganalisis data rental sepeda. Aplikasi ini memungkinkan pengguna untuk memfilter data berdasarkan beberapa parameter seperti musim (season), hari (weekday), dan jam (hour) serta menampilkan visualisasi data seperti grafik bar dan garis.

Fitur Utama
Filter Data Interaktif:
Filter data berdasarkan musim, hari, jam, dan status hari kerja.
Tabel Data:
Menampilkan data hasil filtering dalam bentuk tabel.
Statistik Ringkas:
Menampilkan statistik deskriptif dari data yang telah difilter.
Visualisasi Data:
Grafik Bar: Menampilkan total rental sepeda berdasarkan jam.
Grafik Garis: Menampilkan total rental sepeda berdasarkan hari.
Struktur Folder
bash
Copy code
proyek_analisis_data/
├── data/
│   └── merged_day_hour.csv      # Dataset yang digunakan
├── dashboard.py                 # File utama aplikasi Streamlit
├── requirements.txt             # Dependensi yang diperlukan
└── README.md                    # Dokumentasi proyek
Persyaratan
Pastikan Anda memiliki:

Python versi 3.8 atau lebih baru.
Package Python yang tercantum di file requirements.txt.
Instalasi
Ikuti langkah-langkah berikut untuk menjalankan aplikasi:

1. Clone Repository
Jika proyek ini berada di GitHub, clone repository ke komputer Anda:

bash
Copy code
git clone <URL-repo>
cd proyek_analisis_data
2. Setup Lingkungan Python
Gunakan conda atau venv untuk membuat environment Python.

a) Menggunakan Conda
bash
Copy code
conda create --name bike-ds python=3.9 -y
conda activate bike-ds
pip install -r requirements.txt
b) Menggunakan venv
bash
Copy code
python -m venv venv
source venv/bin/activate    # Untuk Linux/Mac
venv\Scripts\activate       # Untuk Windows
pip install -r requirements.txt
3. Tambahkan Dataset
Pastikan file dataset merged_day_hour.csv berada di folder data/.

Menjalankan Aplikasi
Untuk menjalankan aplikasi Streamlit, gunakan perintah berikut:

bash
Copy code
streamlit run dashboard.py
Akses aplikasi melalui browser di URL berikut:

arduino
Copy code
http://localhost:8501
Penggunaan
Filter Data: Gunakan sidebar untuk memilih filter seperti musim, hari, jam, atau status hari kerja.
Tabel Data: Lihat data hasil filtering pada tabel di halaman utama.
Visualisasi: Analisis data menggunakan grafik bar dan garis untuk memahami pola rental sepeda.
Dependensi
Daftar library yang digunakan dalam proyek ini:

pandas: Untuk manipulasi data.
matplotlib: Untuk membuat visualisasi grafik.
streamlit: Untuk membangun dashboard interaktif.
Instal semua dependensi dengan perintah:

bash
Copy code
pip install -r requirements.txt
Lisensi
Proyek ini menggunakan lisensi MIT. Anda bebas untuk menggunakan, memodifikasi, dan mendistribusikan proyek ini selama mencantumkan kredit kepada pengembang asli.
