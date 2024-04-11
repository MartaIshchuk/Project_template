def output_to_console(text):
    print(text)

def output_to_file_builtin(filename, text):

    try:
        with open(filename, 'w') as file:
            file.write(text)
        print("Текст успішно записано у файл", filename)
    except Exception as e:
        print("Під час запису сталася помилка:", str(e))
