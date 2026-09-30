# Caesar Cipher

Aplikasi enkripsi dan dekripsi **Caesar Cipher** berbasis Python (CLI).

## Deskripsi
Caesar Cipher adalah cipher substitusi monoalfabetik klasik. Setiap huruf pada plaintext digeser sejauh **k** posisi di alfabet. Nama cipher ini berasal dari Julius Caesar yang konon memakainya untuk mengamankan pesan militernya.

## Cara Kerja
Rumus:

- Enkripsi: `C = (P + k) mod 26`
- Dekripsi: `P = (C - k) mod 26`

Keterangan: `P` = posisi huruf plaintext (A=0 ... Z=25), `C` = posisi huruf ciphertext, `k` = kunci (jumlah pergeseran).

Contoh (k = 3):

| Plaintext  | Ciphertext |
|------------|------------|
| Hello, World! | Khoor, Zruog! |

Huruf besar/kecil dipertahankan, sedangkan angka, spasi, dan tanda baca tidak diubah.

## Fitur
- Enkripsi teks dengan kunci angka
- Dekripsi teks dengan kunci angka
- **Brute force**: mencoba seluruh 25 kemungkinan kunci untuk memecahkan ciphertext

## Cara Menjalankan
Pastikan Python 3 sudah terpasang, lalu jalankan:

```bash
python caesar.py
```

Contoh tampilan:

```
=== CAESAR CIPHER ===
1. Enkripsi
2. Dekripsi
3. Brute force
0. Keluar
Pilih menu: 1
Masukkan teks: Hello, World!
Masukkan kunci (angka): 3
Hasil enkripsi: Khoor, Zruog!
```

## Struktur File
```
01-caesar-cipher/
├── caesar.py
└── README.md
```

## Kelemahan
Ruang kunci hanya 25, sehingga mudah dipecahkan dengan brute force atau analisis frekuensi huruf.
