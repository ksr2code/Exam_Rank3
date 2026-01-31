#!/usr/bin/env python3

def whisper_cipher(text: str, shift: int) -> str:
    res = ""
    for c in text:
        if c.isalpha() and c.isupper():
            res += chr((ord(c) - 65 + shift) % 26 + 65)
        elif c.isalpha():
            res += chr((ord(c) - 97 + shift) % 26 + 97)
        else:
            res += c
    return res


def main():
    print(whisper_cipher("hello", 3))
    print(whisper_cipher("Hello World!", 1))
    print(whisper_cipher("xyz", 3))
    print(whisper_cipher("ABC123def", 5))
    print(whisper_cipher("", 10))
    print(whisper_cipher("abc", -3))


if __name__ == "__main__":
    main()


"""
Assignment name: py_whisper_cipher
Expected files: py_whisper_cipher.py
Allowed functions: None

Write a function that creates a simple cipher by shifting letters in a string by a given amount. Non-alphabetic characters should remain unchanged.

Your function must be declared as follows:

def whisper_cipher(text: str, shift: int) -> str:

Examples:

Input:  whisper_cipher("hello", 3)
Output: "khoor"

Input:  whisper_cipher("Hello World!", 1)
Output: "Ifmmp Xpsme!"

Input:  whisper_cipher("xyz", 3)
Output: "abc"

Input:  whisper_cipher("ABC123def", 5)
Output: "FGH123ijk"

Input:  whisper_cipher("", 10)
Output: ""
"""
