# Pencatatan Eksperimen Kecepatan Mengetik Berdasarkan Jenis Teks

**Assignment 2 - Praktikum Pemrograman Fungsional, Modul 1 (Pemrograman Fungsional Menggunakan Python)**
Laboratorium Informatika, Universitas Muhammadiyah Malang

| | |
|---|---|
| **Nama** | _(isi namamu)_ |
| **NIM** | _(isi NIM-mu)_ |
| **Tema** | Pencatatan Data Eksperimental: Typing Test |
| **File utama** | `assignment2_typing_test.py` (versi notebook: `Assignment2_Typing_Test_Sederhana.ipynb`) |

---

## 1. Deskripsi Singkat

Program berbasis menu di terminal untuk mencatat hasil tes kecepatan mengetik (typing test). Pengguna dapat mendaftar, login, lalu mencatat hasil tes (WPM, akurasi, jumlah typo, jenis teks, pemakaian tanda baca). Setiap pengguna **hanya dapat melihat dan mengubah data miliknya sendiri** (*strict session lock*).

Temanya masuk kategori **Pencatatan Data Eksperimental**, bukan sistem manajemen/transaksional, sehingga sesuai aturan penugasan. Variabel eksperimennya adalah `jenis_teks` dan `pakai_punctuation`, yaitu kondisi yang dibandingkan dari sesi ke sesi.

---

## 2. Cara Menjalankan

**Di Visual Studio Code**
1. Pastikan Python dan ekstensi *Python* (Microsoft) terpasang.
2. Buka `assignment2_typing_test.py`.
3. Klik tombol **Run** di kanan atas, atau jalankan di terminal:
   ```
   python assignment2_typing_test.py
   ```
   (di Mac/Linux biasanya `python3 assignment2_typing_test.py`)

**Di Google Colab / Jupyter**
Buka `Assignment2_Typing_Test_Sederhana.ipynb`, lalu jalankan sel dari atas ke bawah. Sel terakhir (Program Utama) akan meminta input.

Tidak ada library tambahan. Program hanya memakai fitur bawaan Python.

---

## 3. Akun Contoh (Data Mock)

| ID | Password | Nama | Peran |
|---|---|---|---|
| `rani01` | `pass123` | Rani | Pemula |
| `dika02` | `abc456` | Dika | Menengah |
| `amel03` | `qwerty` | Amel | Mahir |

Atau buat akun baru lewat menu **Register**.

---

## 4. Struktur Data

```
MENU      (tuple)                 -> pilihan navigasi, tetap
accounts  (dict)                  -> ID : password
profiles  (nested dict)           -> ID : {nama, telepon, peran, keyboard}
sessions  (list of dictionaries)  -> catatan tes, tiap catatan punya "owner"
user_aktif (str / None)           -> ID yang sedang login (None = tamu)
```

Satu **ID** yang sama menghubungkan ketiganya:

```python
accounts["rani01"]   = "pass123"
profiles["rani01"]   = {"nama": "Rani", ...}
sessions[i]["owner"] = "rani01"
```

### Isi satu catatan sesi

| Field | Tipe | Keterangan |
|---|---|---|
| `owner` | `str` | ID pemilik data (dasar session lock) |
| `wpm` | `float` | Kecepatan mengetik (words per minute) |
| `akurasi` | `float` | Persentase ketepatan (0-100) |
| `typo` | `int` | Jumlah salah ketik |
| `jenis_teks` | `str` | Kata Umum / Kutipan / Kode Python / Angka & Simbol |
| `pakai_punctuation` | `bool` | Apakah teks memakai tanda baca |
| `tanggal` | `str` | Tanggal pencatatan |

### Kenapa memilih list of dictionaries untuk data tambahan

- Setiap sesi punya banyak field bernama dengan **tipe data berbeda** (str, float, int, bool), sehingga cocok memakai dictionary.
- Jumlah sesi **terus bertambah dan bisa dihapus**, sehingga cocok memakai list (`append`, `remove`).
- Mudah disaring per `owner`, dan mudah diolah lagi di modul berikutnya.

---

## 5. Pemetaan ke Instruksi Assignment 2

### Tipe Data (halaman 33 modul)

| Instruksi modul | Implementasi | Lokasi |
|---|---|---|
| Menu: gunakan **Tuple** untuk pilihan navigasi tetap | `MENU` berupa tuple | baris 20 |
| Autentikasi: **Dictionary** (username -> password) | `accounts` | baris 24 |
| Data profil: **Nested Dictionary** | `profiles` (ID -> dict profil) | baris 31 |
| Main data: **List of Dictionaries** | `sessions` | baris 38 |

### Persyaratan Fungsi Program (halaman 34 modul)

| No | Persyaratan modul | Implementasi | Lokasi |
|---|---|---|---|
| 1 | **Menu (Tuple & Slicing)**: tampilkan menu dinamis, beda untuk tamu dan user login | `tampilkan_menu()` memakai `MENU[:3]` (tamu) dan `MENU[3:]` (login) | baris 133 |
| 2 | **Registrasi**: tambah ke Account Dictionary dan Profile Nested Dictionary, ID harus unik | `daftar_akun()`: cek `id_baru in accounts`, lalu isi `accounts` dan `profiles` bersamaan | baris 153 |
| 3 | **Login**: validasi ID dan password cocok dengan Account Dictionary | `masuk_akun()`: cek `accounts[id] == password`, maksimal 3 percobaan | baris 177 |
| 4 | **Manipulasi Data**: fungsi terpisah, nama kontekstual (bukan CRUD), list of dictionaries bertipe beragam | `catat_sesi()`, `lihat_riwayat()`, `koreksi_sesi()`, `hapus_sesi()` | baris 210-256 |
| 4 | **Strict Session Lock**: user hanya mengakses data milik ID yang sedang login | `sesi_milik(user_aktif)` memfilter berdasarkan `owner`; `owner` pada sesi baru diisi otomatis, bukan dari input | baris 194, 210 |
| 5 | **Input Validation**: `while` loop + `try-except` pada semua input | `minta_int`, `minta_float`, `minta_teks`, `minta_telepon`, `minta_ya_tidak`, `minta_pilihan` | baris 58-122 |
| 6 | **Data Mock**: 3 data untuk setiap dataset | 3 akun, 3 profil, 3 sesi | baris 24-46 |

### Larangan dan aturan tema

| Aturan | Status |
|---|---|
| Bukan sistem manajemen/transaksional (toko, kasir, perpustakaan) | Terpenuhi (pencatatan eksperimen) |
| Tidak sama dengan contoh (Football Club Players) | Terpenuhi |
| Tidak identik dengan tema teman sekelas | Perlu dicek ulang di spreadsheet sebelum submit |
| Tema dikumpulkan paling lambat H-1 demo Modul 1 | Dikerjakan di luar program |

---

## 6. Konsep Modul 1 yang Dipakai

| Konsep (bab modul) | Di mana digunakan |
|---|---|
| Variabel dan tipe data (3.1) | `str`, `int`, `float`, `bool`, `dict`, `list`, `tuple` pada data sesi dan profil |
| Tuple dan slicing (3.1.2.3) | `MENU[:3]` dan `MENU[3:]` |
| Dictionary dan nested dictionary (3.1.2.4) | `accounts`, `profiles`, serta setiap catatan sesi |
| Type casting (3.1.3) | `int(...)` dan `float(...)` pada fungsi validasi input |
| Indentasi (3.2) | Seluruh blok fungsi, `if`, `for`, `while` |
| Function dengan parameter dan `return` (3.3) | Semua fungsi; mis. `sesi_milik()` menerima `user_aktif` dan mengembalikan list |
| Percabangan `if/elif/else` (3.4) | Pemilihan menu di `jalankan_program()`, pengecekan login |
| Perulangan `for` dan `while` (3.5) | `for` untuk menelusuri sesi, `while True` untuk validasi input dan loop menu |
| `break` (3.5.1) | Keluar dari loop saat ID unik terpenuhi dan saat memilih Keluar |
| Exception handling `try-except` (3.7) | Menangkap `ValueError` pada setiap input |

---

## 7. Alur Program

```
Mulai (user_aktif = None)
   |
   v
Menu Tamu  (MENU[:3])
   |-- Register -> ID unik? -> isi accounts + profiles
   |-- Login    -> ID & password cocok? -> user_aktif = ID
   |-- Keluar   -> program selesai
   |
   v (setelah login)
Menu Pengguna  (MENU[3:])
   |-- Catat Sesi     -> validasi input -> tambah ke sessions (owner = user_aktif)
   |-- Lihat Riwayat  -> tampilkan sesi milik user_aktif saja
   |-- Koreksi Sesi   -> pilih sesi milik sendiri -> ubah wpm / akurasi / typo
   |-- Hapus Sesi     -> pilih sesi milik sendiri -> konfirmasi -> hapus
   |-- Logout         -> user_aktif = None -> kembali ke Menu Tamu
```

---

## 8. Daftar Fungsi

| Fungsi | Kegunaan |
|---|---|
| `minta_int`, `minta_float` | Meminta angka dalam rentang tertentu sampai valid |
| `minta_teks` | Meminta teks tidak kosong |
| `minta_telepon` | Meminta nomor telepon yang hanya berisi angka |
| `minta_ya_tidak` | Meminta jawaban y/n, mengembalikan `True`/`False` |
| `minta_pilihan` | Menampilkan opsi bernomor dan mengembalikan pilihan |
| `tampilkan_menu` | Menampilkan menu dengan slicing sesuai status login |
| `daftar_akun` | Registrasi akun dan profil baru |
| `masuk_akun` | Login, mengembalikan ID atau `None` |
| `sesi_milik` | **Session lock**: mengambil sesi milik user aktif |
| `tampilkan_sesi` | Mencetak daftar sesi bernomor |
| `catat_sesi` | Menambah catatan typing test baru |
| `lihat_riwayat` | Menampilkan riwayat milik sendiri |
| `koreksi_sesi` | Mengubah data sesi milik sendiri |
| `hapus_sesi` | Menghapus sesi milik sendiri (dengan konfirmasi) |
| `jalankan_program` | Loop utama yang mengatur alur menu |

---

## 9. Skenario Uji

| Skenario | Input | Hasil yang diharapkan |
|---|---|---|
| Menu tamu | Buka program | Hanya 3 menu: Register, Login, Keluar |
| Menu pengguna | Login berhasil | 5 menu: Catat Sesi sampai Logout |
| ID kembar | Register dengan `rani01` | Ditolak, diminta ID lain |
| Login salah | Password keliru | Ditolak; 3 kali salah kembali ke menu tamu |
| Tipe data salah | WPM diisi `abc` | Pesan error, diminta ulang |
| Di luar rentang | WPM `500` atau akurasi `150` | Pesan error, diminta ulang |
| Jawaban y/n salah | Isi `x` | Diminta ulang |
| Session lock | Login `rani01` lalu lihat riwayat | Hanya sesi milik `rani01` yang tampil |
| Tambah, ubah, hapus | Catat, koreksi, hapus sesi | Data berubah sesuai; data user lain tidak terpengaruh |

Seluruh skenario di atas sudah diuji dengan input langsung ke program dan berjalan tanpa error.

---

## 10. Catatan Pengembangan Lanjutan

Beberapa ide untuk modul berikutnya (pemrograman fungsional):
- Menghitung rata-rata WPM per jenis teks dengan `map`, `filter`, dan `reduce`.
- Menyaring sesi dengan akurasi di atas 95% memakai `lambda`.
- Mengubah fungsi menjadi *pure function* (tanpa mengubah variabel global).
- Visualisasi progres WPM dengan Matplotlib atau Plotly.
- Menyimpan data ke file (JSON/CSV) agar tidak hilang saat program ditutup.

---

## 11. Struktur File

```
.
├── assignment2_typing_test.py                  # Program utama (jalankan di VS Code)
├── Assignment2_Typing_Test_Sederhana.ipynb     # Versi notebook (Colab/Jupyter)
└── README.md                                   # Dokumen ini
```

> Catatan: `Assignment2_Typing_Test.ipynb` (tanpa kata "Sederhana") adalah versi awal yang memakai sintaks di luar materi Modul 1 (list comprehension, lambda, dll.). Gunakan versi **Sederhana** untuk dikumpulkan dan didemokan.
