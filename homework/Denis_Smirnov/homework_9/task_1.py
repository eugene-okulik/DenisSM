from datetime import datetime

date_str = "Jan 15, 2023 - 12:05:33"
date_obj = datetime.strptime(date_str, "%b %d, %Y - %H:%M:%S")

print("Полное название месяца:", date_obj.strftime("%B"))
print("Дата:", date_obj.strftime("%d.%m.%Y, %H:%M"))

temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27, 22, 22, 23, 25, 29, 29, 31, 33, 31, 30, 32,
                30, 28, 24, 23]

hot_days = list(filter(lambda temp: temp > 28, temperatures))
max_temp = max(hot_days)
min_temp = min(hot_days)
avg_temp = round(sum(hot_days) / len(hot_days), 1)

print("Самая высокая температура:", max_temp)
print("Самая низкая температура:", min_temp)
print("Средняя температура:", avg_temp)
