def is_rotation(str0, str1):
    return True if (str0 + str0).find(str1) >= 0 else False

assert is_rotation('abc', 'bca') == True
assert is_rotation('abc', 'bba') == False