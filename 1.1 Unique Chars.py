# -*- coding: utf-8 -*-

def is_unique_chars_string(string, is_unicode):
    alphabet = 0x10FFFF + 1 if is_unicode else 128
    if len(string) > alphabet:
        return False

    checker = 0
    for char in string:
        if checker & (1 << ord(char)):
            return False
        else:
            checker |= (1 << ord(char))
    return True

assert is_unique_chars_string('tar', False) == True
assert is_unique_chars_string(u'啊啊', True) == False