"""Aplikasi Playfair Cipher (CLI). Huruf J digabung dengan I."""


def buat_matriks(key):
    key = "".join(c for c in key.upper().replace("J", "I") if c.isalpha())
    seen = []
    for c in key + "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if c not in seen:
            seen.append(c)
    return [seen[i:i + 5] for i in range(0, 25, 5)]


def cari(matriks, ch):
    for r, baris in enumerate(matriks):
        if ch in baris:
            return r, baris.index(ch)


def siapkan_pasangan(text):
    text = "".join(c for c in text.upper().replace("J", "I") if c.isalpha())
    pasangan, i = [], 0
    while i < len(text):
        a = text[i]
        b = text[i + 1] if i + 1 < len(text) else "X"
        if a == b:
            pasangan.append((a, "X"))
            i += 1
        else:
            pasangan.append((a, b))
            i += 2
    return pasangan


def proses(text, key, decrypt=False):
    m = buat_matriks(key)
    d = -1 if decrypt else 1
    hasil = []
    for a, b in siapkan_pasangan(text):
        r1, c1 = cari(m, a)
        r2, c2 = cari(m, b)
        if r1 == r2:
            hasil += [m[r1][(c1 + d) % 5], m[r2][(c2 + d) % 5]]
        elif c1 == c2:
            hasil += [m[(r1 + d) % 5][c1], m[(r2 + d) % 5][c2]]
        else:
            hasil += [m[r1][c2], m[r2][c1]]
    return "".join(hasil)


def tampilkan_matriks(key):
    print("\nMatriks kunci:")
    for baris in buat_matriks(key):
        print(" ".join(baris))


def main():
    while True:
        print("\n=== PLAYFAIR CIPHER ===")
        print("1. Enkripsi\n2. Dekripsi\n0. Keluar")
        pilih = input("Pilih menu: ").strip()
        if pilih == "0":
            break
        if pilih not in {"1", "2"}:
            print("Menu tidak valid.")
            continue
        teks = input("Masukkan teks: ")
        key = input("Masukkan kunci: ")
        tampilkan_matriks(key)
        print("Hasil:", proses(teks, key, decrypt=(pilih == "2")))


if __name__ == "__main__":
    main()
