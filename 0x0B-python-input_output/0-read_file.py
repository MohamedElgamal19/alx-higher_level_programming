#!/usr/bin/python3
'''function that reads a text file
'''


def read_file(filename=""):
    '''Let print the contents of UTF8 text file
    '''
    with open(filename, encoding="utf-8")as f:
        print(f.read(), end="")
