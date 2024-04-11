import pandas as pd

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
