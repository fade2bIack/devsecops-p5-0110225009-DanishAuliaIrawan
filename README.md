# Aplikasi Manajemen Data Sederhana

1. **Nama & Fungsi:** Aplikasi Manajemen Data Sederhana. Berfungsi untuk memvalidasi dan mencatat penambahan data secara simulasi ke dalam log sistem.
2. **Bahasa:** Python 3.
3. **Cara Menjalankan:** Buka terminal, masuk ke folder proyek, lalu ketik `python main.py`.
4. **Overview CI/CD:** Pipeline diatur menggunakan GitHub Actions. Workflow akan terpicu secara otomatis setiap kali ada `push` atau `pull_request` ke branch `main`. Pipeline terdiri dari dua tahap (jobs): job `build` untuk memeriksa ketersediaan lingkungan Python, dan job `sast-scan` (menggunakan alat Bandit) yang berjalan setelah build selesai untuk memindai celah keamanan pada source code Python.