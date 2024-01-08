# Fungsi untuk membersihkan teks, mengubah ke huruf besar, dan menggantikan 'J' dengan 'I'
def prepare_text(text):
    text = ''.join([char.upper() for char in text if char.isalpha() or char == ' '])
    text = text.replace('J', 'I')
    return text

# Fungsi untuk menghasilkan matriks Playfair berdasarkan kunci
def generate_key_square(key):
    key_square = [['' for _ in range(5)] for _ in range(5)]
    key = prepare_text(key)
    alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'

    # Menyusun kunci dan alfabet ke dalam satu string unik
    key = key + alphabet
    key = ''.join(sorted(set(key), key=key.find))

    # Mengisi matriks Playfair dengan karakter dari kunci dan alfabet yang belum terpakai
    k = 0
    for i in range(5):
        for j in range(5):
            key_square[i][j] = key[k]
            k += 1

    return key_square

# Fungsi untuk mencari posisi karakter dalam matriks Playfair
def find_char(char, key_square):
    for i in range(5):
        for j in range(5):
            if key_square[i][j] == char:
                return i, j
    # Menambahkan penanganan jika karakter tidak ditemukan
    return -1, -1

# Fungsi untuk enkripsi teks menggunakan Playfair Cipher
def encrypt(plaintext, key):
    plaintext = prepare_text(plaintext)
    key_square = generate_key_square(key)
    cipher_text = ''

    for i in range(0, len(plaintext), 2):
        char1 = plaintext[i]
        char2 = plaintext[i + 1] if i + 1 < len(plaintext) else 'X'

        row1, col1 = find_char(char1, key_square)
        if row1 == -1:
            # Menangani karakter yang tidak ditemukan
            # Misalnya, tambahkan pesan kesalahan atau karakter pengganti
            continue

        row2, col2 = find_char(char2, key_square)
        if row2 == -1:
            # Menangani karakter yang tidak ditemukan
            # Misalnya, tambahkan pesan kesalahan atau karakter pengganti
            continue

        if row1 == row2:
            cipher_text += key_square[row1][(col1 + 1) % 5] + key_square[row2][(col2 + 1) % 5]
        elif col1 == col2:
            cipher_text += key_square[(row1 + 1) % 5][col1] + key_square[(row2 + 1) % 5][col2]
        else:
            cipher_text += key_square[row1][col2] + key_square[row2][col1]

    return cipher_text

# Fungsi untuk dekripsi teks menggunakan Playfair Cipher
def decrypt(ciphertext, key):
    key_square = generate_key_square(key)
    plain_text = ''

    for i in range(0, len(ciphertext), 2):
        char1 = ciphertext[i]
        char2 = ciphertext[i + 1]

        row1, col1 = find_char(char1, key_square)
        if row1 == -1:
            # Menangani karakter yang tidak ditemukan
            # Misalnya, tambahkan pesan kesalahan atau karakter pengganti
            continue

        row2, col2 = find_char(char2, key_square)
        if row2 == -1:
            # Menangani karakter yang tidak ditemukan
            # Misalnya, tambahkan pesan kesalahan atau karakter pengganti
            continue

        if row1 == row2:
            plain_text += key_square[row1][(col1 - 1) % 5] + key_square[row2][(col2 - 1) % 5]
        elif col1 == col2:
            plain_text += key_square[(row1 - 1) % 5][col1] + key_square[(row2 - 1) % 5][col2]
        else:
            plain_text += key_square[row1][col2] + key_square[row2][col1]

    return plain_text.replace('X', '')

if __name__ == "__main__":
    # Contoh penggunaan
    plaintext = "Afif Khalid Fadhillah"
    keyword = "Magetan"

    # Enkripsi
    ciphertext = encrypt(plaintext, keyword)
    print(f"Plaintext: {plaintext}")
    print(f"Ciphertext: {ciphertext}")

    # Dekripsi
    decrypted_text = decrypt(ciphertext, keyword)
    print(f"Decrypted Text: {decrypted_text}")