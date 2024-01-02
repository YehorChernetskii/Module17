# TODO здесь писать код

def encrypt_caesar_russian(message, shift):
    russian_alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    encrypted_message = ''

    for char in message:
        if char.isalpha() and char.lower() in russian_alphabet:
            is_upper = char.isupper()
            char_index = (russian_alphabet.index(char.lower()) + shift) % 32
            encrypted_char = russian_alphabet[char_index]
            encrypted_message += encrypted_char.upper() if is_upper else encrypted_char
        else:
            encrypted_message += char

    return encrypted_message

message = input("Введите сообщение: ")
shift = int(input("Введите сдвиг: "))
result = encrypt_caesar_russian(message, shift)
print("Зашифрованное сообщение:", result)