
# Pertemuan 10 - String dan Pengolahan Teks

Repositori ini berisi latihan dan tugas mata kuliah
Algoritma dan Pemrograman tentang pengolahan string
menggunakan Python.

## Identitas Mahasiswa

- **Nama:** Aulia Nurrizqi
- **NIM:** 2225250160
- **Program Studi:** S1 Pendidikan Matematika
- **Mata Kuliah:** Algoritma dan Pemrograman
- **Pertemuan:** 10
- **Tahun Ajaran:** 2026/2027 Ganjil

## Tujuan

Mempelajari dan menerapkan operasi string dalam Python,
meliputi indeks, slicing, method string, normalisasi teks,
split, join, pencarian kata, dan penggunaan fungsi.

## Struktur Proyek

```text
pertemuan-10-string-NIM/
├── README.md
├── .gitignore
├── latihan/
│   ├── 01_dasar_string.py
│   ├── 02_indeks_slicing.py
│   ├── 03_method_string.py
│   ├── 04_bersihkan_teks.py
│   ├── 05_split_join.py
│   └── 06_pencarian_kata.py
└── tugas/
    └── normalisasi_data_mahasiswa.py
```

## Daftar Latihan

1. **Dasar String**  
   Menggunakan string, `len()`, `upper()`, dan `lower()`.

2. **Indeks dan Slicing**  
   Mengakses karakter dan mengambil sebagian string.

3. **Method String**  
   Menggunakan `strip()`, `title()`, dan `upper()`.

4. **Membersihkan Teks**  
   Menghapus spasi berlebih dan merapikan teks.

5. **Split dan Join**  
   Memisahkan kalimat menjadi kata dan menggabungkannya kembali.

6. **Pencarian Kata**  
   Menggunakan operator `in`, `count()`, dan `find()`.

## Tugas 4: Normalisasi Data Mahasiswa

Program menerima nama mahasiswa dan kode kelas,
kemudian melakukan proses berikut:

1. Menghapus spasi berlebih pada nama.
2. Mengubah nama menjadi format title case.
3. Mengubah kode kelas menjadi huruf kapital.
4. Mengganti spasi pada kode kelas dengan tanda hubung.
5. Menghitung jumlah kata pada nama.
6. Membuat inisial dari setiap kata nama.
7. Menampilkan hasil normalisasi.

## Cara Menjalankan Program

Pastikan Python 3 sudah terpasang dan terminal
VS Code berada di folder utama proyek.

Jalankan latihan dengan perintah berikut:

```bash
python latihan/01_dasar_string.py
python latihan/02_indeks_slicing.py
python latihan/03_method_string.py
python latihan/04_bersihkan_teks.py
python latihan/05_split_join.py
python latihan/06_pencarian_kata.py
```

Jalankan tugas utama:

```bash
python tugas/normalisasi_data_mahasiswa.py
```

Masukkan nama mahasiswa dan kode kelas sesuai
petunjuk yang ditampilkan program.

## Pengujian

Pengujian dilakukan menggunakan empat contoh data
yang tercantum dalam bahan ajar Pertemuan 10.

| Nama Input | Kode Kelas | Hasil Inisial |
|---|---|---|
| aan hendrayana | pmat a 2026 | AH |
| fATHIYYAH mUTHMAINNAH | kelas b | FM |
| BUDI | pmtk 01 | B |
| siti nur aisyah | kelas c | SNA |

Hasil pengujian aktual diperiksa dengan menjalankan
program menggunakan setiap input tersebut.

## Refleksi

Melalui latihan ini, saya mempelajari cara mengolah
teks menggunakan string Python. Operasi seperti
`strip()`, `title()`, `split()`, dan `join()` membantu
menyeragamkan data teks yang tidak konsisten.

Penggunaan fungsi membuat kode lebih terstruktur,
mudah dibaca, dan dapat digunakan kembali.

## Sumber dan Bantuan

- Bahan Ajar Pertemuan 10: String dan Pengolahan Teks dalam Python.
- Dokumentasi Python 3.
- Bantuan tambahan dicantumkan sesuai dengan sumber
  yang benar-benar digunakan.

---