# TODO здесь писать код

import random

first_team = [round(random.uniform(5, 10), 2) for _ in range(20)]
second_team = [round(random.uniform(5, 10), 2) for _ in range(20)]

print("Первая команда:", first_team)
print("Вторая команда:", second_team)

winners = [max(a, b) for a, b in zip(first_team, second_team)]

print("Победители тура:", winners)