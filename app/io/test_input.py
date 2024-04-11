# input.py

def read_file_2(filename):
    with open(filename, 'r') as f:
        data = f.read()
    return data

def read_file_3(filename):
    with open(filename, 'r') as f:
        data = f.readlines()
    return data


# test_input.py

import pytest
from input import read_file_2, read_file_3

@pytest.fixture
def file2_content():
    return "This is a sample text from file 2."

@pytest.fixture
def file3_lines():
    return ["Line 1\n", "Line 2\n", "Line 3\n"]

def test_read_file_2(file2_content):
    content = read_file_2('file2.txt')
    assert content == file2_content

def test_read_file_3(file3_lines):
    lines = read_file_3('file3.txt')
    assert lines == file3_lines
