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
