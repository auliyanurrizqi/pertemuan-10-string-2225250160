
# KUIS FORMATIF PERTEMUAN 10
# Mata Kuliah: Algoritma dan Pemrograman
# Materi: String dan Pengolahan Teks Python

def tampilkan_jawaban():
    print("=" * 60)
    print("JAWABAN KUIS FORMATIF PERTEMUAN 10")
    print("String dan Pengolahan Teks dalam Python")
    print("=" * 60)

    jawaban = [
        (
            "1. Apa perbedaan string dan list pada Python?",
            "String adalah urutan karakter untuk menyimpan teks, "
            "sedangkan list adalah kumpulan elemen yang dapat "
            "memiliki berbagai tipe data."
        ),
        (
            "2. Mengapa string disebut immutable?",
            "Karena karakter dalam string tidak dapat diubah "
            "secara langsung setelah string dibuat. Untuk "
            "mengubah teks, kita harus membuat string baru."
        ),
        (
            "3. Apa hasil dari 'Python'[1:4]?",
            "yth, karena slicing mengambil karakter dari indeks "
            "1 sampai sebelum indeks 4."
        ),
        (
            "4. Apa fungsi strip()?",
            "strip() digunakan untuk menghapus spasi atau "
            "karakter whitespace di awal dan akhir string."
        ),
        (
            "5. Kapan lower() lebih tepat daripada title()?",
            "lower() lebih tepat ketika teks perlu diubah "
            "menjadi huruf kecil semua, misalnya sebelum "
            "melakukan pencarian atau perbandingan teks."
        ),
        (
            "6. Apa perbedaan split() dan join()?",
            "split() memecah string menjadi list berdasarkan "
            "pemisah, sedangkan join() menggabungkan kumpulan "
            "string menjadi satu string dengan pemisah tertentu."
        ),
        (
            "7. Bagaimana memeriksa apakah kata 'data' "
            "terdapat dalam suatu string?",
            "Menggunakan operator in, contohnya: "
            "'data' in teks. Hasilnya True jika ditemukan "
            "dan False jika tidak ditemukan."
        ),
        (
            "8. Apa arti hasil -1 dari find()?",
            "Artinya substring yang dicari tidak ditemukan "
            "dalam string."
        ),
        (
            "9. Mengapa normalisasi teks perlu dilakukan "
            "sebelum perbandingan?",
            "Agar spasi dan kapitalisasi teks konsisten "
            "sehingga data yang sama dapat dibandingkan "
            "dengan lebih tepat."
        ),
        (
            "10. Perintah apa yang digunakan untuk "
            "mengirim commit ke GitHub?",
            "Menggunakan perintah git push."
        )
    ]