# TODO здесь писать код

def compress_list(lst):
    non_zero_elements = [elem for elem in lst if elem != 0]

    zeros = [0] * (len(lst) - len(non_zero_elements))

    lst[:] = non_zero_elements + zeros


numbers = [2, 0, 3, 4, 0, 1, 0, 5, 0, 6]
print("Исходный список:", numbers)

compress_list(numbers)
print("Сжатый список:", numbers)

non_zero_numbers = [elem for elem in numbers if elem != 0]
print("Список без нулей:", non_zero_numbers)