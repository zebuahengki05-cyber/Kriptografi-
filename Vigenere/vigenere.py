"""Aplikasi Vigenere Cipher (CLI)."""


def vigenere(text, key, decrypt=False):
    key = [ord(k) - ord("A") for k in key.upper() if k.isalpha()]
    if not key:
        raise ValueError("Kunci harus berisi huruf.")
    hasil, i = [], 0
    for ch in text:
        if ch.isalpha():
            shift = -key[i % len(key)] if decrypt else key[i % len(key)]
            base = ord("A") if ch.isupper() else ord("a")
            hasil.append(chr((ord(ch) - base + shift) % 26 + base))
            i += 1
        else:
            hasil.append(ch)
    return "".join(hasil)


def main():
    while True:
        print("\n=== VIGENERE CIPHER ===")
        print("1. Enkripsi\n2. Dekripsi\n0. Keluar")
        pilih = input("Pilih menu: ").strip()
        if pilih == "0":
            break
        if pilih not in {"1", "2"}:
            print("Menu tidak valid.")
            continue
        teks = input("Masukkan teks: ")
        key = input("Masukkan kunci (huruf): ")
        try:
            print("Hasil:", vigenere(teks, key, decrypt=(pilih == "2")))
        except ValueError as e:
            print(e)


if __name__ == "__main__":
    main()
