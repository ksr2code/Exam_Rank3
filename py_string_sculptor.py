#!/usr/bin/env python3

def string_sculptor(text: str) -> str:
    res = ""
    lower = 1
    for c in text:
        if c.isalpha() and lower:
            res += c.lower()
            lower = 0
        elif c.isalpha():
            res += c.upper()
            lower = 1
        elif c.isspace():
            res += c
            lower = 1
        else:
            res += c
    return res


def main():
    print(string_sculptor("hello"))
    print(string_sculptor("Hello World"))
    print(string_sculptor("abc123def"))
    print(string_sculptor("Python3.9!"))
    if string_sculptor("") == "":
        print('""')


if __name__ == "__main__":
    main()


"""
Assignment name: py_string_sculptor
Expected files: py_string_sculptor.py
Allowed functions: None

Write a function that transforms a string by alternating the case of alphabetic characters only. Non-alphabetic characters remain unchanged and are ignored for the purpose of alternation. The first alphabetic character should be lowercase, the second uppercase, the third lowercase, and so on.

Your function must be declared as follows:
def string_sculptor(text: str) -> str:

Examples:

Input:  string_sculptor("hello")
Output: "hElLo"

Input:  string_sculptor("Hello World")
Output: "hElLo wOrLd"

Input:  string_sculptor("abc123def")
Output: "aBc123DeF"

Input:  string_sculptor("Python3.9!")
Output: "pYtHoN3.9!"

Input:  string_sculptor("")
Output: ""
"""
