#!/usr/bin/python3
"""Defines a function."""


def text_indentation(text):
    """Function printing new lines after a text."""
    if not isinstance(text, str):
        raise TypeError('text must be a string')

    new_text = ""
    for line in text:
        if line == '.' or line == '?' or line == ':':
            new_text += line + '\n' * 2
        else:
            new_text += line

    print(new_text.strip())
