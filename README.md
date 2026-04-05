# 🖐️ Gesture Hand Isyarat (Hand Gesture Recognition)

Proyek ini adalah sistem deteksi dan pengenalan gestur tangan (isyarat) secara *real-time* menggunakan teknik *Computer Vision*. Aplikasi ini dirancang untuk menerjemahkan gerakan atau posisi tangan tertentu menjadi perintah digital atau teks, yang dapat dikembangkan lebih lanjut untuk alat bantu komunikasi bagi penyandang disabilitas atau kontrol antarmuka tanpa sentuh.

-----

## 🧐 Fitur Utama

  * **Real-Time Tracking:** Mendeteksi titik koordinat tangan secara instan melalui input kamera.
  * **Hand Landmark Detection:** Mengidentifikasi struktur tulang tangan (21 titik kunci) untuk akurasi posisi jari.
  * **Klasifikasi Isyarat:** Mengenali berbagai pola isyarat tangan (seperti angka, huruf, atau perintah kustom).
  * **Visualisasi Feedback:** Menampilkan *bounding box* dan label hasil deteksi langsung pada layar.

-----

## 🛠️ Stack Teknologi

  * **Bahasa Pemrograman:** Python / Java (Pilih yang sesuai dengan proyek Anda).
  * **Library Utama:**
      * **OpenCV:** Untuk pengolahan citra dan akses kamera.
      * **MediaPipe:** Kerangka kerja lintas platform untuk deteksi *hand landmarks*.
      * **NumPy:** Untuk manipulasi matriks dan data koordinat.
      * **TensorFlow/Keras:** (Jika menggunakan model deep learning kustom).

-----

## 📐 Cara Kerja Sistem

1.  **Input Frame:** Menangkap gambar dari webcam secara terus-menerus.
2.  **Preprocessing:** Mengonversi warna (BGR ke RGB) dan melakukan normalisasi ukuran gambar.
3.  **Landmark Extraction:** Menentukan 21 titik koordinat $(x, y, z)$ pada tangan menggunakan MediaPipe.
4.  **Gesture Mapping:** Menghitung jarak antar jari atau sudut sendi untuk menentukan jenis isyarat yang dilakukan.
5.  **Output:** Menampilkan teks hasil terjemahan isyarat pada layar.

-----

## 🚀 Instalasi & Penggunaan

### Prasyarat

Pastikan Anda sudah menginstal Python dan PIP.

1.  **Clone Repositori**

    ```bash
    git clone https://github.com/asboyy/Gesture-Hand-Isyarat.git
    cd Gesture-Hand-Isyarat
    ```

2.  **Instal Dependencies**

    ```bash
    pip install opencv-python mediapipe numpy
    ```

3.  **Jalankan Program**

    ```bash
    python main.py
    ```

-----

## 📂 Struktur Repositori

```text
Gesture-Hand-Isyarat/
├── models/             # File model (jika ada, misal: .h5 atau .tflite)
├── scripts/            # Skrip pemrosesan utama
├── data/               # Dataset atau gambar referensi isyarat
├── main.py             # Entry point aplikasi
└── README.md
```

-----

## 🚧 Pengembangan Mendatang

  - [ ] Penambahan dataset Bahasa Isyarat Indonesia (BISINDO).
  - [ ] Integrasi ke aplikasi mobile (Android/iOS).
  - [ ] Optimasi performa untuk perangkat dengan spesifikasi rendah.

-----

## ✍️ Kontribusi

Jika Anda ingin berkontribusi dalam meningkatkan akurasi model atau menambahkan fitur baru, silakan lakukan **Fork** dan kirimkan **Pull Request**.

**Developer:** [@asboyy](https://www.google.com/search?q=https://github.com/asboyy)
