# TODO здесь писать код

def generate_list(n):
    result_list = []
    for i in range(n):
        if i % 2 == 0:
            result_list.append(1)
        else:
            result_list.append(i % 5)
    return result_list

length_of_list = int(input("Введите длину списка: "))

result = generate_list(length_of_list)
print(f"Результат: {result}")