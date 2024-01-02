# TODO здесь писать код

N = int(input("Кол-во палок: "))
K = int(input("Кол-во бросков: "))

sticks = ['I'] * N

for _ in range(K):
    left, right = map(int, input("Бросок. Сбиты палки с номера до номера: ").split())
    for i in range(left - 1, right):
        sticks[i] = '.'

result = ''.join(sticks)
print("Результат:", result)