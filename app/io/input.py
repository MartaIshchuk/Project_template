import pandas as pd

def input_from_console():
    """
    Returns:
        str: Текст, введений з консолі.
    """
    text = input("Введіть текст з консолі: ")
    return text


def input_from_file_builtin(filename):
    """
    Args:
        filename (str): Шлях до файлу, який потрібно зчитати.

    Returns:
        str: Текст, зчитаний з файлу.
    """
    try:
        with open(filename, 'r') as file:
            text = file.read()
        return text
    except FileNotFoundError:
        return "Файл не знайдено"


def input_from_file_pandas(filename):
    """
    Args:
        filename (str): Шлях до файлу, який потрібно зчитати.

    Returns:
        str: Текст, зчитаний з файлу.
    """
    try:
        data = pd.read_csv(filename)
        text = data.to_string(index=False, header=False)
        return text
    except FileNotFoundError:
        return "Файл не знайдено"


def read_file_2():
    return None


def read_file_3():
    return None