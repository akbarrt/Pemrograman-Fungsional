"""
Assignment 2 - Pemrograman Fungsional (Modul 1)
Pencatatan Eksperimen Kecepatan Mengetik Berdasarkan Jenis Teks

Nama : (isi namamu)
NIM  : (isi NIM-mu)

Cara menjalankan di Visual Studio Code:
  1. Buka file ini di VS Code (pastikan ekstensi Python terpasang).
  2. Klik tombol Run (segitiga di kanan atas), atau
  3. Buka Terminal lalu ketik:  python assignment2_typing_test.py
"""

# ============================================================
# 1. DATA MOCK DAN STRUKTUR DATA
# ============================================================

# Tuple: menu bersifat tetap.
# Index 0-2 untuk tamu, index 3-7 untuk pengguna yang sudah login.
MENU = ("Register", "Login", "Keluar",
        "Catat Sesi", "Lihat Riwayat", "Koreksi Sesi", "Hapus Sesi", "Logout")

# Dictionary: ID sebagai key, password sebagai value
accounts = {
    "rani01": "pass123",
    "dika02": "abc456",
    "amel03": "qwerty",
}

# Nested dictionary: ID sebagai key, rincian profil (dictionary) sebagai value
profiles = {
    "rani01": {"nama": "Rani", "telepon": "0812345678", "peran": "Pemula", "keyboard": "Laptop"},
    "dika02": {"nama": "Dika", "telepon": "0813456789", "peran": "Menengah", "keyboard": "Mekanikal"},
    "amel03": {"nama": "Amel", "telepon": "0814567890", "peran": "Mahir", "keyboard": "Mekanikal"},
}

# List of dictionaries: catatan typing test (tipe data beragam: str, float, int, bool)
sessions = [
    {"owner": "rani01", "wpm": 48.5, "akurasi": 94.2, "typo": 7,
     "jenis_teks": "Kata Umum", "pakai_punctuation": False, "tanggal": "2026-10-01"},
    {"owner": "dika02", "wpm": 72.0, "akurasi": 97.8, "typo": 3,
     "jenis_teks": "Kode Python", "pakai_punctuation": True, "tanggal": "2026-10-01"},
    {"owner": "amel03", "wpm": 85.3, "akurasi": 98.5, "typo": 2,
     "jenis_teks": "Kutipan", "pakai_punctuation": True, "tanggal": "2026-10-02"},
]

# Pilihan tetap (tuple)
PERAN = ("Pemula", "Menengah", "Mahir")
KEYBOARD = ("Laptop", "Mekanikal", "Membran")
JENIS_TEKS = ("Kata Umum", "Kutipan", "Kode Python", "Angka & Simbol")

print("Data mock siap.")

# ============================================================
# 2. FUNGSI VALIDASI INPUT (while True + try-except)
# ============================================================

def minta_int(pesan, minimum, maksimum):
    """Meminta bilangan bulat dalam rentang minimum-maksimum."""
    while True:
        try:
            angka = int(input(pesan))
            if angka < minimum or angka > maksimum:
                print("Angka harus antara", minimum, "dan", maksimum)
            else:
                return angka
        except ValueError:
            print("Input harus berupa angka bulat. Coba lagi.")


def minta_float(pesan, minimum, maksimum):
    """Meminta angka desimal dalam rentang minimum-maksimum."""
    while True:
        try:
            angka = float(input(pesan))
            if angka < minimum or angka > maksimum:
                print("Angka harus antara", minimum, "dan", maksimum)
            else:
                return angka
        except ValueError:
            print("Input harus berupa angka. Coba lagi.")


def minta_teks(pesan):
    """Meminta teks yang tidak kosong."""
    while True:
        try:
            teks = input(pesan).strip()
            if teks == "":
                raise ValueError
            return teks
        except ValueError:
            print("Input tidak boleh kosong. Coba lagi.")


def minta_telepon(pesan):
    """Nomor telepon harus berupa angka."""
    while True:
        try:
            nomor = input(pesan).strip()
            int(nomor)
            return nomor
        except ValueError:
            print("Nomor telepon hanya boleh berisi angka. Coba lagi.")


def minta_ya_tidak(pesan):
    """Mengembalikan True jika jawab y, False jika jawab n."""
    while True:
        try:
            jawab = input(pesan).strip().lower()
            if jawab == "y":
                return True
            elif jawab == "n":
                return False
            else:
                raise ValueError
        except ValueError:
            print("Jawab dengan y atau n. Coba lagi.")


def minta_pilihan(pesan, pilihan):
    """Menampilkan pilihan bernomor, mengembalikan pilihan yang dipilih."""
    for i in range(len(pilihan)):
        print(i + 1, ".", pilihan[i])
    nomor = minta_int(pesan, 1, len(pilihan))
    return pilihan[nomor - 1]

# ============================================================
# 3. MENU DENGAN SLICING
# ============================================================

def tampilkan_menu(sudah_login):
    if sudah_login:
        menu_aktif = MENU[3:]      # slicing: menu setelah login
        print("=== MENU PENGGUNA ===")
    else:
        menu_aktif = MENU[:3]      # slicing: menu tamu
        print("=== MENU TAMU ===")

    for i in range(len(menu_aktif)):
        print(i + 1, ".", menu_aktif[i])
    return menu_aktif

# Contoh tampilan
tampilkan_menu(False)
tampilkan_menu(True)

# ============================================================
# 4. REGISTRASI DAN LOGIN
# ============================================================

def daftar_akun():
    print("--- Registrasi Akun Baru ---")

    # Ulangi sampai ID unik
    while True:
        id_baru = minta_teks("ID: ")
        if id_baru in accounts:
            print("ID sudah dipakai, pilih ID lain.")
        else:
            break

    password = minta_teks("Password: ")
    nama = minta_teks("Nama: ")
    telepon = minta_telepon("Nomor telepon: ")
    peran = minta_pilihan("Pilih peran (nomor): ", PERAN)
    keyboard = minta_pilihan("Pilih keyboard (nomor): ", KEYBOARD)

    # Simpan ke dua dictionary sekaligus
    accounts[id_baru] = password
    profiles[id_baru] = {"nama": nama, "telepon": telepon,
                         "peran": peran, "keyboard": keyboard}
    print("Registrasi berhasil. Silakan login.")


def masuk_akun():
    """Mengembalikan ID jika login berhasil, None jika gagal."""
    print("--- Login ---")
    for percobaan in range(3):
        id_input = minta_teks("ID: ")
        pass_input = minta_teks("Password: ")
        if id_input in accounts and accounts[id_input] == pass_input:
            print("Login berhasil. Selamat datang,", profiles[id_input]["nama"])
            return id_input
        print("ID atau password salah.")
    print("Login gagal 3 kali. Kembali ke menu tamu.")
    return None

# ============================================================
# 5. MANIPULASI DATA SESI DAN SESSION LOCK
# ============================================================

def sesi_milik(user_aktif):
    """Session lock: ambil hanya sesi milik user yang sedang login."""
    hasil = []
    for sesi in sessions:
        if sesi["owner"] == user_aktif:
            hasil.append(sesi)
    return hasil


def tampilkan_sesi(daftar):
    for i in range(len(daftar)):
        s = daftar[i]
        print(i + 1, "|", s["tanggal"], "| WPM:", s["wpm"], "| Akurasi:", s["akurasi"],
              "% | Typo:", s["typo"], "|", s["jenis_teks"], "| Punctuation:", s["pakai_punctuation"])


def catat_sesi(user_aktif):
    print("--- Catat Sesi Typing Test ---")
    wpm = minta_float("WPM (0-300): ", 0, 300)
    akurasi = minta_float("Akurasi % (0-100): ", 0, 100)
    typo = minta_int("Jumlah typo: ", 0, 1000)
    jenis = minta_pilihan("Pilih jenis teks (nomor): ", JENIS_TEKS)
    punct = minta_ya_tidak("Pakai tanda baca? (y/n): ")
    tanggal = minta_teks("Tanggal (contoh 2026-10-08): ")

    sesi_baru = {"owner": user_aktif,      # otomatis dari user yang login
                 "wpm": wpm, "akurasi": akurasi, "typo": typo,
                 "jenis_teks": jenis, "pakai_punctuation": punct,
                 "tanggal": tanggal}
    sessions.append(sesi_baru)
    print("Sesi berhasil dicatat.")


def lihat_riwayat(user_aktif):
    print("--- Riwayat Sesi Saya ---")
    milik = sesi_milik(user_aktif)
    if len(milik) == 0:
        print("Belum ada sesi tercatat.")
    else:
        tampilkan_sesi(milik)


def koreksi_sesi(user_aktif):
    print("--- Koreksi Sesi ---")
    milik = sesi_milik(user_aktif)
    if len(milik) == 0:
        print("Belum ada sesi untuk dikoreksi.")
        return
    tampilkan_sesi(milik)
    nomor = minta_int("Nomor sesi yang dikoreksi: ", 1, len(milik))
    sesi = milik[nomor - 1]

    field = minta_pilihan("Pilih bagian yang diubah (nomor): ", ("wpm", "akurasi", "typo"))
    if field == "wpm":
        sesi["wpm"] = minta_float("WPM baru (0-300): ", 0, 300)
    elif field == "akurasi":
        sesi["akurasi"] = minta_float("Akurasi baru (0-100): ", 0, 100)
    else:
        sesi["typo"] = minta_int("Typo baru: ", 0, 1000)
    print("Sesi berhasil dikoreksi.")


def hapus_sesi(user_aktif):
    print("--- Hapus Sesi ---")
    milik = sesi_milik(user_aktif)
    if len(milik) == 0:
        print("Belum ada sesi untuk dihapus.")
        return
    tampilkan_sesi(milik)
    nomor = minta_int("Nomor sesi yang dihapus: ", 1, len(milik))
    sesi = milik[nomor - 1]

    if minta_ya_tidak("Yakin hapus? (y/n): "):
        sessions.remove(sesi)
        print("Sesi berhasil dihapus.")
    else:
        print("Dibatalkan.")

# ============================================================
# 6. PROGRAM UTAMA
# ============================================================

def jalankan_program():
    user_aktif = None            # None artinya belum login (tamu)

    while True:
        menu_aktif = tampilkan_menu(user_aktif != None)
        nomor = minta_int("Pilih menu (nomor): ", 1, len(menu_aktif))
        pilihan = menu_aktif[nomor - 1]

        if pilihan == "Register":
            daftar_akun()
        elif pilihan == "Login":
            user_aktif = masuk_akun()
        elif pilihan == "Keluar":
            print("Terima kasih!")
            break
        elif pilihan == "Catat Sesi":
            catat_sesi(user_aktif)
        elif pilihan == "Lihat Riwayat":
            lihat_riwayat(user_aktif)
        elif pilihan == "Koreksi Sesi":
            koreksi_sesi(user_aktif)
        elif pilihan == "Hapus Sesi":
            hapus_sesi(user_aktif)
        elif pilihan == "Logout":
            print("Sampai jumpa,", profiles[user_aktif]["nama"])
            user_aktif = None
        print()


# ============================================================
# 7. MENJALANKAN PROGRAM
# ============================================================

if __name__ == "__main__":
    jalankan_program()