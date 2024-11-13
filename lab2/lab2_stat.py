import csv
from datetime import datetime, timedelta
from statistics import mean, mode, median
import os

# Получаем путь к директории, в которой находится скрипт
script_dir = os.path.dirname(os.path.abspath(__file__))
# Устанавливаем эту директорию как текущую
os.chdir(script_dir)

def read_data_from_file(filename):
    """Считывает данные из CSV-файла и возвращает их в виде списка строк."""
    data = []
    with open(filename, newline="") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Пропускаем заголовок
        for row in reader:
            # Преобразуем время из секунд в формат datetime
            seconds = float(
                row[0]
            )  # Предполагаем, что первый столбец - это время в секундах
            timestamp = (
                datetime(1970, 1, 1) + timedelta(seconds=seconds)
            ).time()  # Конвертируем в время
            value = float(row[1])  # Преобразуем значение
            data.append((timestamp, value))
    return data

def split_data(data, interval_minutes=5):
    """Разделяет данные на интервалы заданной длины в минутах."""
    intervals = []
    start_time = data[0][0]
    end_time = (
        datetime.combine(datetime.today(), start_time)
        + timedelta(minutes=interval_minutes)
    ).time()
    current_interval = []

    for timestamp, value in data:
        # Если текущее время попадает в интервал, добавляем значение
        if start_time <= timestamp < end_time:
            current_interval.append(value)
        else:
            # Сохраняем завершенный интервал и начинаем новый
            intervals.append((start_time, end_time, current_interval))
            start_time = end_time
            end_time = (
                datetime.combine(datetime.today(), start_time)
                + timedelta(minutes=interval_minutes)
            ).time()
            current_interval = [value]
    # Добавляем последний интервал
    if current_interval:
        intervals.append((start_time, end_time, current_interval))

    return intervals

def calculate_statistics(interval_data):
    """Вычисляет статистику для заданного интервала данных."""
    count = len(interval_data)
    avg = mean(interval_data)
    try:
        mod = mode(interval_data)
    except:
        mod = "Нет уникальной моды"
    med = median(interval_data)
    return count, avg, mod, med

def main():
    # Убедимся, что работаем в нужной папке
    print("Текущая рабочая директория:", os.getcwd())
    filename = "example.csv"
    data = read_data_from_file(filename)  # Чтение данных из файла
    intervals = split_data(data)  # Разделение данных на интервалы

    # Выводим статистику для каждого интервала
    for start, end, values in intervals:
        if values:  # Проверяем, что интервал не пустой
            count, avg, mod, med = calculate_statistics(values)
            print(f"Интервал {start} - {end}:")
            print(f"  Количество значений: {count}")
            print(f"  Среднее значение: {avg:.2f}")
            print(f"  Мода: {mod}")
            print(f"  Медиана: {med:.2f}")
            print()
main()
