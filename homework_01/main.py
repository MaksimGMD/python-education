"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*args):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел

    """
    # * первое что пришло в голову
    # res = []

    # for i in args:
    #     res.append(i**2)
    # return res

    return [x**2 for x in args]


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_prime(numbers):
    res = []
    for number in numbers:
        is_prime = True
        for i in range(2, number):
            if number % i == 0:
                is_prime = False
        if is_prime and number > 1:
            res.append(number)
    return res


def filter_numbers(numbers, filter):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    """

    if filter == ODD:
        return [x for x in numbers if x % 2]
    elif filter == EVEN:
        return [x for x in numbers if x % 2 == 0]
    elif filter == PRIME:
        return is_prime(numbers)


print(filter_numbers([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], ODD))
