import random

#  while True:
#    print('строчка на экране')

required_number = 7
user_number = random.randint(a=0, b=10)

while required_number != user_number:
    user_number = random.randint(a=0, b=10)
    print(f'Пользователь ввёл число {user_number}')

iteretions_count = 10
i = 0

while i < iteretions_count:
    print(f'текущая итерация: {i}')
    i += 1

#    i = i + 1 тоже самое что и строчка сверху

users = [
    {'name': 'Oleg', 'age': 32},
    {'name': 'Sergei', 'age': 28},
    {'name': 'Olga', 'age': 25},
    {'name': 'Maria', 'age': 30},
]

from pprint import pprint

for user in users:
    pprint(f"Пользователю {user['name']} {user['age']} лет")

d = {
    "first": 1,
    "second": 2,
    'third': 3
}

for item in d:
    pprint(item)

for item in d.keys():
    pprint(item)

for item in d.values():
    pprint(item)

for item in d.items():
    pprint(item)

for key, value in d.items():
    pprint(f'Ключ: {key}, Значение: {value}')

# for i in rage - цикл с итератором

iteretions_count = 10

for i in range(3, iteretions_count, 2):
    print(f'Текущая итерация: {i}')


