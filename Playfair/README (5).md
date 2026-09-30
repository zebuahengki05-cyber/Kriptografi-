# Playfair Cipher

Aplikasi enkripsi dan dekripsi **Playfair Cipher** berbasis Python (CLI).

## Deskripsi
Playfair Cipher adalah cipher **digraf** (mengenkripsi dua huruf sekaligus) yang memakai matriks kunci 5x5. Karena memproses pasangan huruf, cipher ini lebih sulit dipecahkan dengan analisis frekuensi huruf tunggal.

## Cara Kerja
1. **Buat matriks 5x5** dari kunci: tulis huruf kunci tanpa duplikat, lalu lengkapi dengan sisa alfabet. Huruf `J` digabung dengan `I`.
2. **Bagi plaintext menjadi pasangan huruf.** Jika dua huruf dalam pasangan sama, sisipkan `X` di antaranya. Jika jumlah huruf ganjil, tambahkan `X` di akhir.
3. **Enkripsi tiap pasangan:**
   - Satu **baris** yang sama: ambil huruf di sebelah kanan (dekripsi: kiri).
   - Satu **kolom** yang sama: ambil huruf di bawahnya (dekripsi: atasnya).
   - Berbeda baris dan kolom: bentuk persegi panjang, ambil huruf di sudut lain pada baris yang sama.

Contoh matriks dengan kunci `PLAYFAIR EXAMPLE`:

```
P L A Y F
I R E X M
B C D G H
K N O Q S
T U V W Z
```

Contoh:

| Plaintext | Kunci | Ciphertext |
|-----------|-------|------------|
| HIDE THE GOLD | PLAYFAIR EXAMPLE | BMODZBXDNAGE |

Hasil dekripsi: `HIDETHEGOLDX` (spasi hilang dan `X` di akhir adalah huruf pengisi).

## Fitur
- Enkripsi teks dengan kunci berupa kata
- Dekripsi teks dengan kunci berupa kata
- Menampilkan matriks kunci 5x5 pada setiap proses

## Cara Menjalankan
Pastikan Python 3 sudah terpasang, lalu jalankan:

```bash
python playfair.py
```

Contoh tampilan:

```
=== PLAYFAIR CIPHER ===
1. Enkripsi
2. Dekripsi
0. Keluar
Pilih menu: 1
Masukkan teks: HIDE THE GOLD
Masukkan kunci: PLAYFAIR EXAMPLE

Matriks kunci:
P L A Y F
I R E X M
B C D G H
K N O Q S
T U V W Z
Hasil: BMODZBXDNAGE
```

## Struktur File
```
03-playfair-cipher/
├── playfair.py
└── README.md
```

## Catatan
- Hanya huruf A-Z yang diproses; spasi, angka, dan tanda baca dibuang.
- Hasil dekripsi bisa mengandung huruf `X` pengisi yang perlu dibaca menyesuaikan konteks.
