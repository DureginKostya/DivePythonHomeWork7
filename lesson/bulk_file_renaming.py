"""Задание:
Напишите функцию группового переименования файлов. Она должна:
 принимать параметр желаемое конечное имя файлов.
При переименовании в конце имени добавляется порядковый номер.
 принимать параметр количество цифр в порядковом номере.
 принимать параметр расширение исходного файла.
Переименование должно работать только для этих файлов внутри каталога.
 принимать параметр расширение конечного файла.
 принимать диапазон сохраняемого оригинального имени.
Например, для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла.
К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик
файлов и расширение.

Соберите из созданных на уроке и в рамках домашнего задания функций пакет
для работы с файлами.
"""

from os import walk
from pathlib import Path


__all__ = ['rename_files']

AMOUNT_BORDERS_NAME = 2
LEFT_BORDER_NAME = 0
AMOUNT_DIGITS = 1
MIN_VALUE_COUNTER = 1
NAME_SCRIPT = 'bulk_file_renaming.py'
PATH_INTO_SCRIPT = r'/'


def _checking_user_extension(extension: str) -> bool:
    return extension.startswith('.') and extension[1:].isalnum()


def _checking_user_name_range(user_list: list[int]) -> bool:
    if len(user_list) == AMOUNT_BORDERS_NAME:
        if isinstance(user_list[0], int) and isinstance(user_list[1], int):
            if LEFT_BORDER_NAME < user_list[0] <= user_list[1]:
                return True
            return False
        return False
    return False


def _checking_user_number_digits(digit: int) -> bool:
    return isinstance(digit, int) and digit >= AMOUNT_DIGITS


def _checking_user_final_name(user_name: str) -> bool:
    return user_name is None or user_name.isalnum()


def _get_path_into_script() -> str | None:
    for dir_path, dir_name, file_name in walk(PATH_INTO_SCRIPT):
        if NAME_SCRIPT in file_name:
            return dir_path
    return None


def rename_files(original_extension: str, final_extension: str,
                 name_range: list[int], number_digits: int, final_name=None) -> None:
    directory = _get_path_into_script()
    if directory is not None:
        if (_checking_user_extension(original_extension) and
                _checking_user_extension(final_extension) and
                _checking_user_name_range(name_range) and
                _checking_user_number_digits(number_digits) and
                _checking_user_final_name(final_name)):
            global MIN_VALUE_COUNTER
            left_border = name_range[0]
            right_border = name_range[1]
            max_value_counter = 10 ** number_digits - 1
            for file in Path(Path(directory)).glob('*' + original_extension):
                file_name, *_ = file.name.split('.')
                length_name = len(file_name)
                if length_name < left_border:
                    left_border = length_name
                    right_border = length_name
                if final_name is not None:
                    new_file_name = (f'{file.parent}\\{file_name[left_border - 1: right_border]}_'
                                     f'{final_name}_{MIN_VALUE_COUNTER}{final_extension}')
                else:
                    new_file_name = (f'{file.parent}\\{file_name[left_border - 1: right_border]}_'
                                     f'{MIN_VALUE_COUNTER}{final_extension}')
                Path(file).rename(new_file_name)
                if MIN_VALUE_COUNTER < max_value_counter:
                    MIN_VALUE_COUNTER += 1
                else:
                    MIN_VALUE_COUNTER = 1
        else:
            print('Введено(-ы) некорректное(-ые) значения')
    else:
        print('Скрипт bulk_file_renaming.py не найден')


if __name__ == '__main__':
    rename_files('.docx', '.txt', [1, 3], 2)
