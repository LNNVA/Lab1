import ctypes

# Загружаем библиотеку
test_lib = ctypes.CDLL('./libtest.so')

# Устанавливаем restype и argtypes для calculate_primes
test_lib.calculate_primes.restype = ctypes.POINTER(ctypes.c_int)
test_lib.calculate_primes.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int)]

def get_primes(n):
    """Получает простые числа при помощи calculate_primes."""
    count = ctypes.c_int()  # Создаём переменную для хранения количества простых чисел
    primes_ptr = test_lib.calculate_primes(n, ctypes.byref(count))  # Вызываем C-функцию
    primes = [primes_ptr[i] for i in range(count.value)]  # Преобразуем указатель в список Python
    return primes

def check_goldbach(n):
    if n <= 2 or n % 2 != 0:
        raise ValueError("Число должно быть чётным и больше 2")

    primes = get_primes(n)
    for prime in primes:
        if (n - prime) in primes:
            print(f"{n} = {prime} + {n - prime}")
            return True
    print(f"Не удалось найти разложение для {n}")
    return False

# Пример
n = int(input("Введите чётное число больше 2: "))
check_goldbach(n)
