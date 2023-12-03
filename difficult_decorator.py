# 2.2 Напиши декоратор log_function,
# который будет записывать информацию о вызовах функции, такую как имя функции, переданные аргументы и результат выполнения, в файл лога. Каждый вызов функции должен создавать новую запись в файле.
#   тут надо использовать контекстный менеджер для записи в файл

#   Пример использования:

#   @log_function("log.txt")
#   def calc_add(a, b):
#     return a + b

#   После выполнения кода, файл "log.txt" должен содержать
# записи о вызове функции в следующем формате:
#   Function: add
#   Arguments: (2, 3)
#   Result: 5
#   Timestamp: <временная метка>
# А тут узнаём, что такое timestamp (используется повсеместно).
# Используй модуль datetime


from datetime import datetime


def log_function(filename):
    def decorator(func):
        def wrapper(*args):
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open(filename, "a") as file:
                file.write(f"Function: {func.__name__}\n")
                file.write(f"Arguments: {args}\n")
                file.write(f"Result: {func(*args)}\n")
                file.write(f"Timestamp: {timestamp}\n")
                file.write("-" * 10 + "\n")

        return wrapper

    return decorator


@log_function("log.txt")
def calc_add(a, b):
    return a + b


calc_add(2, 3)
