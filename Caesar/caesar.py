"""Aplikasi Caesar Cipher (CLI)."""


def shift_text(text, key, decrypt=False):
    if decrypt:
        key = -key
    hasil = []
    for ch in text:
        if ch.isalpha():
            base = ord("A") if ch.isupper() else ord("a")
            hasil.append(chr((ord(ch) - base + key) % 26 + base))
        else:
            hasil.append(ch)
    return "".join(hasil)


def brute_force(cipher):
    for k in range(1, 26):
        print(f"Key {k:2}: {shift_text(cipher, k, decrypt=True)}")


def main():
    while True:
        print("\n=== CAESAR CIPHER ===")
        print("1. Enkripsi\n2. Dekripsi\n3. Brute force\n0. Keluar")
        pilih = input("Pilih menu: ").strip()
        if pilih == "0":
            break
        if pilih not in {"1", "2", "3"}:
            print("Menu tidak valid.")
            continue
        teks = input("Masukkan teks: ")
        if pilih == "3":
            brute_force(teks)
            continue
        try:
            key = int(input("Masukkan kunci (angka): "))
        except ValueError:
            print("Kunci harus berupa angka.")
            continue
        if pilih == "1":
            print("Hasil enkripsi:", shift_text(teks, key))
        else:
            print("Hasil dekripsi:", shift_text(teks, key, decrypt=True))


if __name__ == "__main__":
    main()
