#!/usr/bin/python3
"""
Module for appending text to a file.
"""


def append_text_to_file(file_path="", text_to_append=""):
    """
    append_text_to_file - Appends a string to the end of a text file (UTF-8) and returns the number of characters added.

    Args:
        file_path (str): The path of the file to which text should be appended.
        text_to_append (str): The text to be appended to the file.

    Returns:
        int: The number of characters written to the file.
    """
    with open(file_path, mode="a", encoding="UTF-8") as file:
        return file.write(text_to_append)

