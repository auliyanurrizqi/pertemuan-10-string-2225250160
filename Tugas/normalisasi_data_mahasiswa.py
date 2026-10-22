def normalisasi_nama(nama):
    """Membersihkan spasi dan menyeragamkan format nama."""
    nama = " ".join(nama.strip().split())
    return nama.title()


def buat_inisial(nama):
    """Membuat inisial dari setiap kata dalam nama."""
    nama_bersih = normalisasi_nama(nama)
    kata = nama_bersih.split()
    return "".join(k[0] for k in kata)


def normalisasi_kode(kode):
    """Mengubah kode kelas menjadi huruf kapital dan tanda hubung."""
    kata = kode.strip().upper().split()
    return "-".join(kata)


def main():
    print("=" * 40)
    print(" NORMALISASI DATA MAHASISWA")
    print("=" * 40)

    nama = input("Nama mahasiswa : ")
    kode = input("Kode kelas     : ")

    nama_bersih = normalisasi_nama(nama)
    kode_bersih = normalisasi_kode(kode)
    jumlah_kata = len(nama_bersih.split())
    inisial = buat_inisial(nama)

    print("\nHasil Normalisasi")
    print("-" * 40)
    print(f"Nama bersih : {nama_bersih}")
    print(f"Kode kelas  : {kode_bersih}")
    print(f"Jumlah kata : {jumlah_kata}")
    print(f"Inisial     : {inisial}")
    print("-" * 40)


if __name__ == "__main__":
    main()
