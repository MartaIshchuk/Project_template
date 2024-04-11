# input.py

def read_file_2(filename):
    with open(filename, 'r') as f:
        data = f.read()
    return data

def read_file_3(filename):
    with open(filename, 'r') as f:
        data = f.readlines()
    return data


