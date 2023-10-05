"""Задание №7
✔ Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
✔ Каждая группа включает файлы с несколькими расширениями.
✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки."""


import os
import pathlib


__all__ = ['sort_files']


# def sort_files(path):
#     os.chdir(path)
#     ext = {}
#     for i in path.iterdir():
#         if i.is_file():
#             ext[i.suffix] = ext.get(i.suffix, []) + [i]
#     for key, value in ext.items():
#         os.mkdir(key)
#         for file in value:
#             try:
#                 file.replace(path/key/file.name)
#             except PermissionError:
#                 continue


def sort_files(path: str) -> None:
    os.chdir(path)
    files = os.listdir()
    ext = {}
    for i in files:
        *_, extension = i.split('.')
        ext[extension] = ext.get(extension, []) + [i]
    for key, value in ext.items():
        os.mkdir(key)
        for i in value:
            os.replace(i, f'{key}\\{i}')


if __name__ == '__main__':
    # sort_files(pathlib.Path(r'E:\GeekBrains\DiveIntoPython\Seminars\Seminar07\Task\Example'))
    sort_files(r'E:\GeekBrains\DiveIntoPython\Seminars\Seminar07\Task\Example')
