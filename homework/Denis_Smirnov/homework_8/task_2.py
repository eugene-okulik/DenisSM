import sys
sys.set_int_max_str_digits(100000)

def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def get_fibonacci(n):
    fib = fibonacci_generator()
    for _ in range(n - 1):
        next(fib)
    return next(fib)


print("Пятое число:", get_fibonacci(5))
print("Двухсотое число:", get_fibonacci(200))
print("Тысячное число:", get_fibonacci(1000))
print("Стотысячное число:", get_fibonacci(100000))
