# 1) Написать лямбда функцию, определяющую чётное/нечётное. Функция принимает параметр (число) и если чётное выдаёт
# слово 'Чётное', если нет, то - 'Нечётное'.

print(
    list(
        map(lambda num: 'Чётное' if num % 2 == 0 else 'Нечётное',
            [1, 2, 3, 4],
            )
    )
)

# 2) Дан список чисел. Вернуть список, где при помощи функции map(), каждое число переведено в строку. В качестве
# функции map() использовать lambda.

print(
    list(
        map(lambda num: f'{num}',
            [1, 2, 3, 4],
            )
    )
)

# 3) При помощи функции filter() из кортежа слов отфильтровать только те, которые, являются палиндромами,
# (которые, читаются одинаково в обе стороны)

print(
    list(
        filter(
            lambda word: word == word[::-1],
            ('казак', 'армян', 'доход', 'утро'),
        )
    )
)

# 4) Написать декоратор к 2 любым функциям, который бы считал и выводил время их выполнения.

from datetime import datetime


def main_decorator():
    def decorator(func):
        def wrapper(*args, **kwargs):
            start_time = datetime.now()
            func(*args, **kwargs)
            end_time = datetime.now()
            total_time = end_time - start_time
            print(f'Функция {func.__name__} выполнялась {total_time}\n')

        return wrapper

    return decorator


@main_decorator()
def is_even(number):
    return 'Чётное' if number % 2 == 0 else 'Нечётное'


@main_decorator()
def number_to_string(number):
    return str(number)


is_even(5000000000)
number_to_string(21231)


# 5) Сделать функцию которая на вход принимает строку, анализирует её исключительно методом .isdigit() без
# дополнительных библиотек и переводит строку в число. Функция умеет распознавать отрицательные числа и
# десятичные дроби.


def num_info(vvod: str) -> str | float:
    vyvod = ''
    errors = ''
    message = 'Вы ввели '
    for n in vvod:
        if n in ('-', '.', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
            vyvod += n
        else:
            errors += n

    if errors:
        message += f'не корректное число: {vvod}\n'
    else:
        if '.' in vyvod:
            message += 'дробное, '
        else:
            message += 'целое, '

        if '-' in vyvod:
            message += f'отрицательное число: {float(vvod)}\n'
        else:
            message += f'положительное число: {float(vvod)}\n'

    print(message)


num_info('-.777')


# 5') Вводиться строка(любая). Выводит число (тип float).
def str_num(vvod):
    for n in vvod:
        if n not in ('-', '.', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
            vvod = vvod.replace(n, '')
    float(vvod)

    print(vvod)


str_num('saad2sd2.ыф3asa')
