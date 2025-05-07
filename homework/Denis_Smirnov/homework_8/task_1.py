import random

salary = int(input('Укажите зарплату:'))
bonus = random.choice([True, False])

if bonus:
    salary += random.randint(100, 1000)

print(f"${salary}")
