# Task: Напиши генератор even_numbers, который генерирует все чётные числа от 0 до заданного предела.
#     Пример использования:
#     even_numbers_list = even_numbers(10)
#     for number in even_numbers_list:
#       print(number)


def even_numbers(number: int):
    i = 0
    while i <= number:
        if number % 2 == 0:
            yield i
        i += 1


even_numbers_list = even_numbers(10)
for number in even_numbers_list:
    print(number)
