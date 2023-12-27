# TODO здесь писать код

def get_vowels(text):
    vowels = "аеёиоуыэюя"  # Гласные буквы в русском алфавите
    vowels_list = [char.lower() for char in text if char.lower() in vowels]
    return vowels_list

user_text = input("Введите текст: ")

vowels_result = get_vowels(user_text)
vowels_count = len(vowels_result)

print(f"Список гласных букв: {vowels_result}")
print(f"Длина списка: {vowels_count}")