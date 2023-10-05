"""Задание №4:
✔ Создайте функцию, которая создаёт файлы с указанным расширением.
Функция принимает следующие параметры:
✔ расширение
✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
✔ количество файлов, по умолчанию 42
✔ Имя файла и его размер должны быть в рамках переданного диапазона."""


from task02 import rnd_name
from random import randint


__all__ = ['create_files']


def create_files(extension: str, min_len_name=6,
                 max_len_name=30, min_byte=256, max_byte=4096, qty_files=42) -> None:
    for _ in range(qty_files):
        with open(rnd_name() + extension, 'wb') as f:
            f.write(bytes([randint(0, 255) for _ in range(randint(min_byte, max_byte))]))


if __name__ == '__main__':
    create_files('.txt')