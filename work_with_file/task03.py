"""Задание №3:
✔ Напишите функцию, которая открывает на чтение созданные
в прошлых задачах файлы с числами и именами.
✔ Перемножьте пары чисел. В новый файл сохраните
имя и произведение:
✔ если результат умножения отрицательный, сохраните имя
записанное строчными буквами и произведение по модулю
✔ если результат умножения положительный, сохраните имя
прописными буквами и произведение округлённое до целого.
✔ В результирующем файле должно быть столько же строк,
сколько в более длинном файле.
✔ При достижении конца более короткого файла,
возвращайтесь в его начало."""


from task01 import rnd_num
from task02 import rnd_name_in_file


__all__ = ['open_file']


def len_list(list1: list[str], list2: list[str]) -> list[str]:
    if len(list2) > len(list1):
        temp = len(list1)
        for i in range(len(list2)):
            if i > len(list1) - 1:
                list1.append(list1[i % temp])
    elif len(list1) > len(list2):
        temp = len(list2)
        for i in range(len(list1)):
            if i > len(list2) - 1:
                list2.append(list2[i % temp])
    return list1, list2


def open_file(file_name: str, file_num: str, output: str):
    with (
        open(file_name, 'r') as a,
        open(file_num, 'r') as b,
        open(output, 'a') as c
    ):
        names = a.read().strip().split('\n')
        num = b.read().strip().split('\n')
        for i, j in zip(*len_list(names, num)):
            first, second = map(float, j.split('/'))
            mult = first * second
            if mult < 0:
                c.write(f'{i.lower()} {abs(mult)} \n')
            else:
                c.write(f'{i.upper()} {int(mult)} \n')


if __name__ == '__main__':
    rnd_num(10, 'numbers.txt')
    rnd_name_in_file(5, 'names.txt')
    open_file('names.txt', 'numbers.txt', 'new_file.txt')
