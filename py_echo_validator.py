#!/usr/bin/env python3

def echo_validator(text: str) -> bool:
    if text == "":
        return False
    new_text = "".join(c.lower() for c in text if c.isalpha())
    start = 0
    end = len(new_text) - 1

    while (start < end):
        if new_text[start] != new_text[end]:
            return False
        start += 1
        end -= 1

    return True


print(echo_validator("racecar"))
print(echo_validator("A man a plan a canal Panama"))
print(echo_validator("race a car"))
print(echo_validator("Was it a car or a cat I saw"))
print(echo_validator("hello"))
print(echo_validator("Madam I'm Adam"))
print(echo_validator(""))


"""
Assignment name  : py_echo_validator
Expected files   : py_echo_validator.py
Allowed functions: None
--------------------------------------------------------------------------------

Write a function that checks if a string is a palindrome, ignoring spaces and case, only cons

Your function must be declared as follows:

def echo_validator(text: str) -> bool:

Examples:

Input: echo_validator("racecar")
Output: True

Input: echo_validator("A man a plan a canal Panama")
Output: True

Input: echo_validator("race a car")
Output: False

Input: echo_validator("Was it a car or a cat I saw")
Output: True

Input: echo_validator("hello")
Output: False

Input: echo_validator("Madam Im Adam")
Output: True

Input: echo_validator("")
Output: False
"""
