import json
import os

# Получаем путь к директории, в которой находится скрипт
script_dir = os.path.dirname(os.path.abspath(__file__))
# Устанавливаем эту директорию как текущую
os.chdir(script_dir)

def load_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    print("Содержимое файла:")
    print(json.dumps(data, indent=4, ensure_ascii=False))
    return data

def edit_json(data):
    """Редактирование файла."""
    while True:
        field = input("Введите поле для редактирования (или 'stop' для завершения): ")
        if field.lower() == 'stop': 
            break
        elif field in data:
            new_value = input(f"Введите новое значение для '{field}': ")
            data[field] = new_value
            print(f"Поле '{field}' обновлено на '{new_value}'")
        else:
            print(f"Поле '{field}' не найдено.")
    return data

def save_json(data, save_path):
    """Сохраняет"""
    try:
        with open(save_path, 'w') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
        print(f"Файл сохранён в {save_path}")
    except Exception as e:
        print(f"Ошибка при сохранении файла: {e}")

def main():
    # Указываем путь к загружаемому файлу JSON
    file_path = 'test.json'
    # Загружаем и отображаем
    data = load_json(file_path)
    # Редактируем
    data = edit_json(data)
    # После завершения редактирования предлагаем сохранить изменения
    save_choice = input("Хотите сохранить изменения? (yes/no): ")
    if save_choice == 'yes':
        save_dir = input("Введите директорию для сохранения файла (например, './'): ")
        save_path = os.path.join(save_dir, 'new_test.json')
        # Проверка корректности данных JSON перед сохранением
        try:
            json.dumps(data)  # Проверяем, можно ли преобразовать данные в JSON
            save_json(data, save_path)
        except (TypeError, ValueError) as e:
            print("Ошибка: некорректные данные JSON. Файл не был сохранён.")
            print(f"Описание ошибки: {e}")
    else:
        print("Изменения не были сохранены.")

main()
