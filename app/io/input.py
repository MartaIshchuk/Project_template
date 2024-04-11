import pandas as pd

def input_from_console():

    text = input("Введіть текст з консолі: ")
    return text

def input_from_file_builtin(filename):

    try:
        with open(filename, 'r') as file:
            text = file.read()
        return text
    except FileNotFoundError:
        return "Файл не знайдено"

def input_from_file_pandas(filename):

    try:
        data = pd.read_csv(filename)
        text = data.to_string(index=False, header=False)
        return text
    except FileNotFoundError:
        return "Файл не знайдено"
