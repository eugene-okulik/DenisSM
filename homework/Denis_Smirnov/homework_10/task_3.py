num1 = float(input("Первое число:"))
num2 = float(input("Второе число:"))


def dec_operation(func):
    def wrapper(first, second):
        if first < 0 or second < 0:
            operation = '*'
        elif first == second:
            operation = '+'
        elif first > second:
            operation = '-'
        else:
            operation = '/'

        return func(first, second, operation)

    return wrapper


@dec_operation
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '*':
        return first * second
    elif operation == '/':
        return first / second
    return None


result = calc(num1, num2)

print(result)
