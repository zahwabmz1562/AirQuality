# Air Quality Dashboard

## Deskripsi Proyek
Proyek ini merupakan aplikasi dashboard kualitas udara yang menampilkan visualisasi data udara dari berbagai stasiun selama periode 2013-2017. Visualisasi termasuk heatmap korelasi parameter udara, boxplot, dan line chart untuk melihat tren PM10.

## Setup
1. Pastikan Python telah diinstal.
2. Instal dependencies menggunakan `pip install -r requirements.txt`.
3. Jalankan aplikasi dengan perintah `streamlit run AirQuality.py`.

## Struktur Direktori
- `AirQuality.py`: Kode utama aplikasi Streamlit.
- `merged_data.csv`: Data udara yang telah digabungkan dari berbagai stasiun.
- `requirements.txt`: Daftar dependencies.

## Dependencies
- `streamlit`: Framework untuk membuat aplikasi web dengan Python.
- `pandas`: Library untuk manipulasi dan analisis data.
- `seaborn`, `matplotlib`: Library untuk visualisasi data.

## Cara Menggunakan
1. Jalankan aplikasi menggunakan perintah `streamlit run AirQuality.py`.
2. Gunakan sidebar untuk memilih stasiun, kategori, tanggal, dan parameter lainnya.
3. Gunakan tombol untuk beralih antara visualisasi seperti heatmap, boxplot, dan line chart.

## Kontribusi
Kontribusi selalu dipersilakan. Silakan buat *issue* atau *pull request* untuk memberikan masukan atau peningkatan.

## Lisensi
Proyek ini dilisensikan di bawah [MIT License](LICENSE).
