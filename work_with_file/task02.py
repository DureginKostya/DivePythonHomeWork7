"""Задание №2:
✔ Напишите функцию, которая генерирует
псевдоимена.
✔ Имя должно начинаться с заглавной буквы,
состоять из 4-7 букв, среди которых
обязательно должны быть гласные.
✔ Полученные имена сохраните в файл."""

from random import randint


__all__ = ['rnd_name']


VOWELS = 'AEYUIOaeyuio'


def rnd_name() -> str:
    name_len = randint(4, 7)
    while True:
        name = ''
        for i in range(name_len):
            name += chr(randint(65, 90))
        for i in name:
            if i in VOWELS:
                return name.capitalize()


def rnd_name_in_file(counter: int, file_name: str) -> None:
    with open(file_name, 'a') as f:
        for i in range(counter):
            f.write(rnd_name() + '\n')


if __name__ == '__main__':
    rnd_name_in_file(5, r'E:\GeekBrains\DiveIntoPython\Seminars\Seminar07\Task\names.txt')
    # rnd_name_in_file(5, 'E:\\GeekBrains\\DiveIntoPython\\Seminars\\Seminar07\\Task\\names.txt')
