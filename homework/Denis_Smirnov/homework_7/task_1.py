secret_number = 8

while True:
    user_input = int(input("Угадайте число от 1 до 10: "))
    if user_input == secret_number:
        print("Поздравляю! Вы угадали!")
        break
    else:
        print("Попробуйте снова")
