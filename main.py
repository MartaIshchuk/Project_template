import input
import output


def main():
    text_from_console = input.input_from_console()
    text_from_builtin_file = input.input_from_file_builtin("input.txt")
    text_from_pandas_file = input.input_from_file_pandas("input.csv")

    output.output_to_console(text_from_console)
    output.output_to_console(text_from_builtin_file)
    output.output_to_console(text_from_pandas_file)

    output.output_to_file_builtin("output.txt", text_from_console)
    output.output_to_file_builtin("output.txt", text_from_builtin_file)
    output.output_to_file_builtin("output.txt", text_from_pandas_file)


if __name__ == "__main__":
    main()
