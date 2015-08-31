def is_permutation_sort(str0, str1):
    if len(str0) != len(str1):
        return False
    return sorted(str0) == sorted(str1)

assert is_permutation_sort('abc', 'cba') == True
assert is_permutation_sort('abc', 'a') == False
assert is_permutation_sort('abc ', ' acb') == True

def is_permutation_count(str0, str1):
    if len(str0) != len(str1):
        return False
    count = dict()
    for char in str0:
        count.setdefault(char, 0)
        count[char] += 1
    for char in str1:
        count.setdefault(char, 0)
        count[char] -= 1
        # because lengths are equal
        if count[char] < 0:
            return False
    return True

assert is_permutation_count('abc', 'cba') == True
assert is_permutation_count('abc', 'a') == False
assert is_permutation_count('abc ', ' acb') == True
