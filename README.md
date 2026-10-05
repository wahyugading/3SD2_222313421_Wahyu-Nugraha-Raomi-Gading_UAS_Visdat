---
{
  "id": "file_schd91ic",
  "filetype": "document",
  "filename": "README",
  "created_at": "2026-10-05T02:50:36.329Z",
  "updated_at": "2026-10-05T02:53:23.032Z",
  "meta":
    {
      "location": "/",
      "tags": [],
      "categories": [],
      "description": "",
      "source": "markdown",
    },
}
---

# Rokok-vs-Gizi-Susenas

### _Ironi Konsumsi Masyarakat: Visualisasi Spasial dan Analisis Teks Pengeluaran Zat Adiktif terhadap Kebutuhan Gizi Menggunakan Mikrodata Susenas_

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://uas-visdat-wahyu-nugraha-3sd2.streamlit.app/)[![Python 3.12](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)](https://www.python.org/)[![Plotly](https://img.shields.io/badge/Visualization-Plotly%20%7C%20D3.js-3F4F75?logo=plotly)](https://plotly.com/)[![NetworkX](https://img.shields.io/badge/Network%20Analysis-NetworkX-blue)](https://networkx.org/)[![Tests](https://img.shields.io/badge/QA%20Testing-9%2F9%20Passed-brightgreen)](https://pytest.org/)[![License: CC BY-SA 4.0](https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-sa/4.0/)

---

## 📌 Identitas Karya Ilmiah & Pengembang

Proyek ini disusun guna memenuhi evaluasi **Ujian Akhir Semester (UAS) Mata Kuliah Visualisasi Data dan Informasi** — Tahun Akademik 2025/2026.

- **Mahasiswa:** Wahyu Nugraha Raomi Gading
- **NIM / Kelas:** 222313421 / 3SD2
- **Program Studi:** D-IV Komputasi Statistik
- **Dosen Pengampu:** Farid Ridho, M.T. & Siti Mariyah, Ph.D.
- **Institusi:** Politeknik Statistika STIS, Jakarta, Indonesia
- **🌐 Tautan Aplikasi Web (Streamlit Cloud):** <https://uas-visdat-wahyu-nugraha-3sd2.streamlit.app/>
- **📂 Tautan Repositori Kode Sumber (GitHub):** <https://github.com/wahyugading/3SD2_222313421_Wahyu-Nugraha-Raomi-Gading_UAS_Visdat.git>

---

## 📖 Ringkasan Proyek

Pemenuhan gizi yang optimal, terutama protein hewani bermutu tinggi (daging dan ikan), merupakan pilar mendasar dalam mitigasi _stunting_ dan peningkatan kualitas modal manusia Indonesia. Namun, data empiris Survei Sosial Ekonomi Nasional (Susenas) Badan Pusat Statistik (BPS) periode 2018–2024 memperlihatkan realitas yang paradoksal: **alokasi belanja rumah tangga untuk zat adiktif (rokok dan tembakau) tetap bertengger tinggi dan persisten, bahkan melampaui gabungan belanja protein hewani di hampir separuh wilayah Indonesia.**

Aplikasi **Rokok-vs-Gizi-Susenas** mengadopsi pendekatan jurnalisme komputasional bergaya editorial (_The Editorial Ledger / Charcoal Atlas_) untuk membangun _data storytelling_ terpadu. Sistem ini membedah data mikro agregat 511 kabupaten/kota ke dalam **5 taksonomi visualisasi data sekaligus** (hierarkis, multivariat, geospasial, teks, dan jejaring) serta memvalidasinya melalui penambangan teks 104 dokumen resmi Berita Resmi Statistik (BRS) BPS.

---

## 🚀 Fitur dan Taksonomi Visualisasi Utama

Aplikasi ini mencakup lima modul analitik mendalam:

### 1. Bagian 1: Anatomi Keranjang Belanja (_Data Berhierarki_)

- **Representasi Ganda:** Diagram Partisi **Sunburst** dan **Treemap 3 tingkat** (`Semua Pengeluaran` → `Komoditas Utama` → `Subkomoditas`).
- **Fitur Interaktif:** Pemilihan tahun pengamatan (2018–2024), pemilihan wilayah dinamis (Nasional vs 511 kabupaten/kota), serta _drill-down zoom_ dengan _breadcrumb navigation_.
- **Integritas Data:** Rekonstruksi hierarki _bottom-up_ murni guna meniadakan risiko bias penghitungan ganda (_double-counting_).

### 2. Bagian 2: Ekonometrika & Korelasi (_Analisis Multivariat_)

- **Diagram Pencar (Scatter Plot) Multidimensi:** Memetakan hubungan pengeluaran rokok mingguan (sumbu X) terhadap berbagai indikator kesejahteraan (sumbu Y: _Prevalensi Ketidakcukupan Pangan / PoU, Garis Kemiskinan, P0, P1, P2_).
- **Encoding Grafis:** Diameter lingkaran proporsional terhadap populasi penduduk, warna mewakili 7 kelompok kepulauan besar.
- **Evaluasi Statistik:** Estimasi koefisien korelasi Pearson ($r$) dan pengujian signifikansi asosiasi secara _real-time_.

### 3. Bagian 3: Atlas Geospasial Spasial (_Data Geospasial_)

- **Dua Jenis Peta Komparatif:**
  1. **Peta Kloroplet (Choropleth Map):** Menampilkan rasio defisit belanja rokok terhadap komoditas pangan terpilih pada poligon batas wilayah 511 daerah otonom.
  2. **Peta Simbol Proporsional (Bubble Map):** Menggabungkan dua variabel serentak—diameter lingkaran mengkodekan volume nominal rupiah belanja rokok mingguan, dan warna gradasi divergen mengkodekan rasio defisit.
- **Filter Komoditas Pembanding Dinamis:** Memungkinkan pengguna membandingkan belanja rokok terhadap beragam komoditas (Telur & Susu, Daging, Ikan, Sayur-sayuran, Padi-padian, Buah-buahan, dll.).
- **Skala Divergen Bebas Distorsi:** Palet Okabe-Ito divergen berpusat netral pada angka ambang kritis $1{,}0\times$ (_Biru = Prioritas Gizi, Jingga = Defisit Nutrisi_).

### 4. Bagian 4: Bukti Tekstual Resmi BPS (_Data Teks & Jejaring_)

- **Korpus Dokumen:** 104 dokumen teks resmi Publikasi dan Berita Resmi Statistik (BRS) BPS periode 2018–2024 bertema kemiskinan dan kesejahteraan rakyat.
- **Tiga Visualisasi Teks:**
  1. _Horizontal Bar Chart:_ 15 kata paling dominan (_Term Frequency_).
  2. _Line Chart Deret Waktu:_ Tren kemunculan kata kunci per tahun (Rokok vs Beras 2018–2024).
  3. _Graf Jejaring Semantik (Bigram Network):_ Struktur keterkaitan ko-okurensi kata berdampingan menggunakan algoritma pegas deterministik (_Spring Layout NetworkX_).
- **Filter Periode:** Penapisan dokumen interaktif per tahun pengamatan atau korpus agregat multi-tahun.

### 5. Bagian 5: Dokumentasi Data, Metodologi, & Aksesibilitas

- **Rujukan Resmi BPS:** Tabel publikasi dan modul survei Susenas BPS lengkap dengan cakupan wilayah dan tanggal aksesibilitas data.
- **Kamus Metadata Variabel:** Definisi operasional, tipe data, klasifikasi, dan peran analitik seluruh variabel.
- **Matriks Justifikasi Visual Encoding:** Penjelasan teoritis pemilihan posisi ortogonal, warna divergen, ukuran simbol, dan partisi area mengacu pada prinsip persepsi _Cleveland & McGill_ dan _Tamara Munzner_.
- **Unduh Dataset Publik:** Fasilitas pengunduhan dataset panel olahan 511 daerah dan master data agregat format `.CSV`.

---

## 🎨 Aksesibilitas & Desain Visual

- **Palet Warna Ramah Buta Warna (_Barrier-Free Color_):** Seluruh elemen visual menggunakan palet warna ilmiah standar **Okabe-Ito Color Universal Design (CUD)** yang terbukti ramah dan aman bagi pembaca dengan defisiensi penglihatan warna (_deuteranopia, protanopia, tritanopia_).
- **Pengalih Tema Tampilan Cerdas (Tri-State Theme Switcher):**
  - 💻 **Mode Sistem (Auto):** Mendeteksi konfigurasi OS pengguna secara otomatis.
  - ☀️ **Mode Terang (Light Mode):** Kanvas putih bersih dengan teks kontras tinggi (`#000000` / `#0F172A`) dan aksen tegas.
  - 🌙 **Mode Gelap (Dark Mode):** Kanvas arang monolitik (`#0E1117`) dengan tipografi cerah berlatar gelap permanen.
- **Tipografi Editorial Ledger:** Perpaduan harmonis antara _Playfair Display_ (keanggunan judul editorial), _Nunito Sans_ (keterbacaan teks analitik), dan _JetBrains Mono_ (presisi angka statistik).

---

## 📁 Struktur Repositori

```text
web story uas/
├── app.py                                              # Naskah utama aplikasi Streamlit data storytelling
├── test_app.py                                         # Suite pengujian mutu otomatis (Pytest)
├── requirements.txt                                    # Daftar dependensi pustaka Python
├── README.md                                           # Dokumentasi resmi proyek
├── 3SD2_222313421_Wahyu Nugraha Raomi Gading.docx     # Laporan makalah ilmiah format IEEE
├── master_data_pengeluaran_kemiskinan_2018_2024.csv    # Master data agregat pengeluaran & kemiskinan makro
├── master_subkomoditas_long.csv                        # Data panel hierarkis subkomoditas pangan & rokok
├── master_teks_kemiskinan.csv                          # Korpus teks bersih 104 dokumen BRS BPS
├── indonesia511.geojson                                # Batas poligon spasial digital 511 kabupaten/kota
└── ekstrak dan prepocessing data/
    └── scrape_teks_bps.py                              # Skrip penambangan teks BPS & pra-pemrosesan NLP
```

---

## 💻 Panduan Menjalankan Secara Lokal

### 1. Prasyarat Sistem

- Python versi 3.10, 3.11, atau 3.12
- Git

### 2. Kloning Repositori

```bash
git clone https://github.com/wahyugading/3SD2_222313421_Wahyu-Nugraha-Raomi-Gading_UAS_Visdat.git
cd 3SD2_222313421_Wahyu-Nugraha-Raomi-Gading_UAS_Visdat
```

### 3. Buat dan Aktifkan Virtual Environment

```bash
# Windows (PowerShell)
python -m venv venv
.\venv\Scripts\Activate.ps1

# Linux / macOS
python3 -m venv venv
source venv/bin/activate
```

### 4. Instalasi Dependensi

```bash
pip install -r requirements.txt
```

### 5. Jalankan Aplikasi Streamlit

```bash
streamlit run app.py
```

Aplikasi akan otomatis terbuka pada peramban web di alamat lokal `http://localhost:8501`.

---

## 🧪 Pengujian Kualitas Otomatis (QA Testing)

Proyek ini dilengkapi dengan suite pengujian otomatis berbasis `pytest` untuk menjamin integritas fungsional, keandalan formula, dan stabilitas rendering:

```bash
pytest test_app.py -v
```

### Cakupan Pengujian (9/9 Passed - 100%):

1. `test_rupiah`: Verifikasi pemformatan mata uang rupiah dengan pemisah ribuan titik.
2. `test_title_prov`: Normalisasi kapitalisasi nama provinsi dan akronim (DKI, DI).
3. `test_wilayah_key`: Pengujian normalisasi kunci penyambung tabel BPS ke batas spasial GeoJSON.
4. `test_wmean`: Verifikasi formula matematis rata-rata tertimbang berbasis populasi penduduk.
5. `test_zero_division_safety`: Penanganan nilai nol dan tak terdefinisi (_division-by-zero resilience_).
6. `test_shapely_fallback`: Mekanisme toleransi kesalahan penyederhanaan geometri spasial.
7. `test_load_data_loose_coupling`: Pengujian modularitas pembacaan dataset independen.
8. `test_app_renders_without_exception`: Pengujian eksekusi rendering antarmuka Streamlit tanpa eror.
9. `test_app_interactions`: Pengujian simulasi interaksi widget, pemilihan tahun, wilayah, dan kontrol layer.

---

## 📊 Rujukan Sumber Data BPS

Seluruh data bersumber dari rujukan resmi Badan Pusat Statistik (BPS) Republik Indonesia:

1. _Survei Sosial Ekonomi Nasional (Susenas) Modul Konsumsi dan Pengeluaran (2018–2024)_.
2. _Berita Resmi Statistik (BRS) Profil Kemiskinan di Indonesia (Rilis Semesteran Maret & September 2018–2024)_.
3. _Publikasi Statistik Kesejahteraan Rakyat Indonesia (Susenas Kor 2018–2024)_.
4. _Tabel Dinamis Garis Kemiskinan menurut Kabupaten/Kota (2018–2024)_.
5. _Prevalensi Ketidakcukupan Konsumsi Pangan / Prevalence of Undernourishment (BPS & Badan Pangan Nasional 2018–2024)_.
6. _Peta Geospasial Batas Administrasi Digital Indonesia (SIG BPS & Ina-Geoportal)_.

---

## 📜 Lisensi & Integritas Akademik

Karya visualisasi dan naskah ilmiah ini didistribusikan di bawah lisensi terbuka [Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/). Seluruh kode sumber terbuka untuk keperluan riset akademik, verifikasi mandiri, dan advokasi kebijakan publik.
