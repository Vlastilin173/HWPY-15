#Из ДЗ №1 задача 3

import logging
import argparse
from typing import List

# Настройка логирования
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def list_of_duplicates(_list_integer: List[int]) -> List[int]:
    """Функция для поиска дубликатов в списке."""
    duplicates = set()
    for item in _list_integer:
        if _list_integer.count(item) > 1:
            duplicates.add(item)
    return list(duplicates)


def main(list_integer: List[int]):
    """Основная функция для обработки и вывода результата."""
    logging.info(f"Список обработки: {list_integer}")
    result = list_of_duplicates(list_integer)
    print(f"Дубликаты: {result}")
    logging.info(f"Дубликаты: {result}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Найдите дубликаты в списке целых чисел."
    )
    parser.add_argument(
        "-l", "--list", nargs="+", type=int, help="Список целых чисел для обработки."
    )
    args = parser.parse_args()

    if args.list:
        main(args.list)
    else:
        list_integer = [10, 20, 30, 40, 50, 60, 30, 10, 20]

        main(list_integer)