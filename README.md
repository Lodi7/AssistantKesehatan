# AI Health Assistant

AI Health Assistant adalah aplikasi chatbot kesehatan berbasis Artificial Intelligence yang membantu pengguna memperoleh informasi kesehatan, mencari dokter berdasarkan spesialisasi, menemukan rumah sakit sesuai lokasi, serta mengakses berita kesehatan terbaru melalui antarmuka percakapan yang sederhana dan interaktif.

Aplikasi ini dibangun menggunakan Streamlit sebagai frontend dan Google Gemini sebagai mesin AI untuk menghasilkan respons yang informatif dan mudah dipahami.

---

# Features

## Health Assistant

* Tanya jawab kesehatan berbasis AI
* Informasi gejala dan keluhan kesehatan
* Edukasi kesehatan umum
* Saran gaya hidup sehat
* Dukungan percakapan kesehatan mental ringan

## Doctor Recommendation

* Cari dokter berdasarkan spesialisasi
* Menampilkan profil dokter
* Menampilkan rumah sakit tempat praktik dokter

## Hospital Search

* Cari rumah sakit berdasarkan kota atau wilayah
* Menampilkan informasi rumah sakit yang relevan
* Pencarian berbasis data rumah sakit Indonesia

## Health News

* Menampilkan berita kesehatan terbaru
* Klasifikasi berita berdasarkan kategori kesehatan
* Integrasi data real-time dari NewsAPI

## User Experience

* Riwayat percakapan
* Reset percakapan
* Antarmuka chatbot interaktif
* Respons real-time

---

# Tech Stack

## Frontend

* Streamlit

## Artificial Intelligence

* Google Gemini 2.0 Flash

## Backend & Data Processing

* Python
* Requests
* Python Dotenv

## External APIs

* Gemini API
* NewsAPI

## Data Sources

* GitHub Raw JSON
* Dataset Dokter Indonesia
* Dataset Rumah Sakit Indonesia

---

# Installation

## Clone Repository

```bash
git clone https://github.com/Lodi7/AssistantKesehatan.git
```

## Masuk Folder Project

```bash
cd AssistantKesehatan
```

## Install Dependency

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Buat file `.env`

```env
GEMINI_API_KEY=your_gemini_api_key
NEWS_API_KEY=your_newsapi_key
```

---

# Running Project

Jalankan aplikasi Streamlit:

```bash
streamlit run app.py
```

Aplikasi akan berjalan pada:

```txt
http://localhost:8501
```

---

# Example Prompts

### Cari Dokter

```txt
Cari dokter jantung
```

```txt
Rekomendasi dokter anak di Surabaya
```

### Cari Rumah Sakit

```txt
Rumah sakit di Surabaya
```

```txt
Cari rumah sakit di Jawa Timur
```

### Berita Kesehatan

```txt
Berita kesehatan terbaru
```

```txt
Berita kesehatan mental
```

### Konsultasi Kesehatan

```txt
Saya sering sakit kepala saat bekerja
```

```txt
Bagaimana cara menjaga kesehatan jantung?
```

---

# Disclaimer

AI Health Assistant hanya digunakan untuk tujuan edukasi dan informasi kesehatan umum.

Informasi yang diberikan oleh sistem tidak menggantikan diagnosis, konsultasi, maupun tindakan medis profesional. Untuk kondisi medis tertentu, segera konsultasikan dengan dokter atau tenaga kesehatan yang berwenang.

---

# License

This project is for educational purposes.
