def process_response(response):
    number_str = response.split(':')[-1]
    number = int(number_str.strip())
    return number + 10


response1 = "результат операции: 42"
response2 = "результат операции: 514"
response3 = "результат работы программы: 9"

print(process_response(response1))
print(process_response(response2))
print(process_response(response3))
