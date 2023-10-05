"""Задание №1:
✔ Напишите функцию, которая заполняет файл
(добавляет в конец) случайными парами чисел.
✔ Первое число int, второе - float разделены вертикальной чертой.
✔ Минимальное число - -1000, максимальное - +1000.
✔ Количество строк и имя файла передаются как аргументы функции."""


from random import randint, uniform


__all__ = ['rnd_num']


def rnd_num(counter: int, file_name: str) -> None:
    with open(file_name, 'a', encoding='UTF-8') as f:
        for i in range(counter):
            f.write(f'{randint(-1000, 1000)} / {uniform(-1000, 1000)} \n')


if __name__ == '__main__':
    # rnd_num(5, r'E:\GeekBrains\DiveIntoPython\Seminars\Seminar07\Task\numbers.txt')
    rnd_num(5, 'E:\\GeekBrains\\DiveIntoPython\\Seminars\\Seminar07\\Task\\numbers.txt')
