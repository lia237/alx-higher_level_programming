#!/usr/bin/python3
"""
Module for reading and printing the content of a text file.
"""


def read_and_print_text_file(file_path=""):
    """
    read_and_print_text_file - reads a text file (UTF-8) and prints its content to stdout.

    Args:
        file_path (str): The path to the text file to be read and printed.
    """
    with open(file_path, "r", encoding="UTF-8") as file:
        for line in file:
            print(line, end="")

