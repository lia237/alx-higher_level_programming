#!/usr/bin/python3
"""
Module for saving an object to a JSON file.
"""
import json


def save_object_to_json_file(obj, file_path):
    """
    save_object_to_json_file - Writes an object to a text file using JSON representation.

    Args:
        obj: The object to be saved to the JSON file.
        file_path (str): The path of the JSON file where the object should be saved.
    """
    with open(file_path, "w") as json_file:
        json.dump(obj, json_file)

