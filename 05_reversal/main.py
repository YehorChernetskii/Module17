# TODO здесь писать код

def reverse_between_h(input_string):
    first_h_index = input_string.find('h')
    last_h_index = input_string.rfind('h')

    if first_h_index != -1 and last_h_index != -1 and first_h_index < last_h_index:
        prefix = input_string[:first_h_index + 1]
        suffix = input_string[last_h_index:]
        middle_part = input_string[first_h_index + 1:last_h_index][::-1]

        result = prefix + middle_part + suffix
        return result
    else:
        return "Ошибка: не найдены две буквы 'h' или первая буква 'h' расположена после последней."

user_input = input("Введите строку: ")
result = reverse_between_h(user_input)
print(result)