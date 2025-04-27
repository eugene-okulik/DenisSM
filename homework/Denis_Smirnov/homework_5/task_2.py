response1 = "результат операции: 42"
response2 = "результат операции: 514"
response3 = "результат работы программы: 9"

colon_position1 = response1.index(':')
number_position1 = response1[colon_position1 + 2:]
number_from_response1 = int(number_position1)
result1 = number_from_response1 + 10
print(result1)

colon_position2 = response2.index(':')
number_position2 = response2[colon_position2 + 2:]
number_from_response2 = int(number_position2)
result2 = number_from_response2 + 10
print(result2)

colon_position3 = response3.index(':')
number_position3 = response3[colon_position3 + 2:]
number_from_response3 = int(number_position3)
result3 = number_from_response3 + 10
print(result3)
