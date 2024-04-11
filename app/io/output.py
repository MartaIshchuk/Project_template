def output_to_console(text):
    """
    Args:
        text (str): Текст, який потрібно вивести у консоль.

    Returns:
        None
    """
    print(text)


def output_to_file_builtin(filename, text):
    """
    Args:
        filename (str): Шлях до файлу, в який потрібно записати текст.
        text (str): Текст, який потрібно записати у файл.

    Returns:
        None
    """
    try:
        with open(filename, 'w') as file:
            file.write(text)
        print("Текст успішно записано у файл", filename)
    except Exception as e:
        print("Під час запису сталася помилка:", str(e))
