import os
from datetime import datetime, timedelta


def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            yield line.strip()


def process_line(line):
    parts = line.strip().split(' ', 3)

    number = parts[0].rstrip('.')
    date_part = parts[1]
    time_part = parts[2]
    command = parts[3].replace(' - ', '')

    datetime_str = f"{date_part} {time_part}"
    dt = datetime.strptime(datetime_str, "%Y-%m-%d %H:%M:%S.%f")

    return number, dt, command


def process_date(number, dt):
    if number == '1':
        new_date = dt + timedelta(weeks=1)
        print(f"Дата {dt} через неделю: {new_date}")

    elif number == '2':
        weekday = dt.strftime("%A")
        print(f"Дата {dt} — это {weekday}")

    elif number == '3':
        days_ago = (datetime.now() - dt).days
        print(f"Дата {dt} была {days_ago} дней назад")


base_path = os.path.dirname(__file__)
parent_folder = os.path.dirname(os.path.dirname(base_path))
file_path = os.path.join(parent_folder, 'eugene_okulik', 'hw_13', 'data.txt')

if not os.path.exists(file_path):
    raise FileNotFoundError(f"Файл '{file_path}' не найден")

for line in read_file(file_path):
    number, dt, command = process_line(line)
    process_date(number, dt)
