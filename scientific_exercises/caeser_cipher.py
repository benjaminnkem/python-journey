word = "benjamin nkem"
alphabets = "abcdefghijklmnopqrstuvwxyz"
cipher_move = 3


def encrypt(word_input):
    crypt_word = ""

    for i in word_input.lower():
        letter = i
        if letter == " ":
            crypt_word += " "
            continue
        letter_index = alphabets.find(letter)

        if letter_index + cipher_move > len(alphabets) - 1:
            index_offset = letter_index + cipher_move - len(alphabets)
            crypt_word += alphabets[index_offset]
        else:
            crypt_word += alphabets[letter_index + cipher_move]

    return crypt_word


def decrypt(encrypted_word):
    decrypted_word = ""

    for i in encrypted_word.lower():
        letter = i
        if letter == " ":
            decrypted_word += " "
            continue
        letter_index = alphabets.find(letter)

        if letter_index - cipher_move < 0:
            index_offset = len(alphabets) - 1 - letter_index
            decrypted_word += alphabets[index_offset]
        else:
            decrypted_word += alphabets[letter_index - cipher_move]

    return decrypted_word


encrypt_result = encrypt(word)
print('encrypt_result', encrypt_result)  # ehqmdplqqnhpwrfkxnzx

decrypt_result = decrypt(encrypt_result)
print(decrypt_result)  # benjaminnkemtochukwu
