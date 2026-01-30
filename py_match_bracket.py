#!/usr/bin/env python3

def is_valid_parentheses(s):
    stack = []
    pairs = {'(': ')', '[': ']', '{': '}'}
    for char in s:
        if char in pairs:
            stack.append(char)
        elif not stack or pairs[stack.pop()] != char:
            return False
    return len(stack) == 0


def main():
    s = input().strip()
    print("True" if is_valid_parentheses(s) else "False")


if __name__ == "__main__":
    main()
