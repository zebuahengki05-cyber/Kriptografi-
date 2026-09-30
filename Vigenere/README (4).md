# Vigenere Cipher

Aplikasi enkripsi dan dekripsi **Vigenere Cipher** berbasis Python (CLI).

## Deskripsi
Vigenere Cipher adalah cipher substitusi **polialfabetik**. Berbeda dengan Caesar yang memakai satu pergeseran tetap, Vigenere memakai kunci berupa kata sehingga tiap huruf digeser dengan nilai yang berbeda-beda mengikuti huruf kunci. Hal ini membuatnya lebih tahan terhadap analisis frekuensi sederhana.

## Cara Kerja
Rumus:

- Enkripsi: `C(i) = (P(i) + K(i mod n)) mod 26`
- Dekripsi: `P(i) = (C(i) - K(i mod n)) mod 26`

Keterangan: `P` = huruf plaintext, `K` = huruf kunci (A=0 ... Z=25), `n` = panjang kunci. Kunci diulang sampai sepanjang teks.

Contoh:

| Plaintext | Kunci | Ciphertext |
|-----------|-------|------------|
| ATTACK AT DAWN | LEMON | LXFOPV EF RNHR |

Proses:

```
Plaintext : A T T A C K   A T   D A W N
Kunci     : L E M O N L   E M   O N L E
Ciphertext: L X F O P V   E F   R N H R
```

Spasi, angka, dan tanda baca tidak diubah dan tidak menggeser posisi kunci.

## Fitur
- Enkripsi teks dengan kunci berupa kata
- Dekripsi teks dengan kunci berupa kata
- Validasi kunci (harus mengandung huruf)

## Cara Menjalankan
Pastikan Python 3 sudah terpasang, lalu jalankan:

```bash
python vigenere.py
```

Contoh tampilan:

```
=== VIGENERE CIPHER ===
1. Enkripsi
2. Dekripsi
0. Keluar
Pilih menu: 1
Masukkan teks: ATTACK AT DAWN
Masukkan kunci (huruf): LEMON
Hasil: LXFOPV EF RNHR
```

## Struktur File
```
02-vigenere-cipher/
├── vigenere.py
└── README.md
```

## Kelemahan
Bisa dipecahkan dengan metode Kasiski atau Index of Coincidence jika kunci pendek dan teks cukup panjang.
