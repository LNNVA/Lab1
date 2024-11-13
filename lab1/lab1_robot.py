# Задаем границы поля
FIELD_WIDTH = 100
FIELD_HEIGHT = 100

def lab_1():
    # Задаем начальную позицию робота
    x, y = 1, 1
    path = [(x, y)]  # Путь, пройденный роботом
    # Обрабатываем команды
    for command in commands:
        line, steps = command.split(',') # разделяем команду на направление и нужное колличество шагов
        steps = int(steps)

        if line == 'R':  # Движение вправо
            for i in range(steps):
                x += 1
                if x > FIELD_WIDTH:  # Проверка выхода за пределы поля
                    print("Ошибка: выход за границу поля вправо.")
                    return
                path.append((x, y)) # добавляем координату в список пройденного пути

        elif line == 'L':  # Движение влево
            for i in range(steps):
                x -= 1
                if x < 1:
                    print("Ошибка: выход за границу поля влево.")
                    return
                path.append((x, y))

        elif line == 'D':  # Движение вниз
            for i in range(steps):
                y += 1
                if y > FIELD_HEIGHT:
                    print("Ошибка: выход за границу поля вниз.")
                    return
                path.append((x, y))

        elif line == 'U':  # Движение вверх
            for i in range(steps):
                y -= 1
                if y < 1:
                    print("Ошибка: выход за границу поля вверх.")
                    return
                path.append((x, y))
    # Выводим результат
    print("Координаты для робота:")
    for coord in path:
        print(f"{coord[0]},{coord[1]}") # выводим пройденный путь
        
# Пример использования
commands = ["L,8", "D,16"]
lab_1()
