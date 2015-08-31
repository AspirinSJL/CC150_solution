def compress_string(string):
    if len(string) == 0:
        return ''

    # http://stackoverflow.com/questions/19926089/python-equivalent-of-java-stringbuffer
    # ''.join(string_list) or ''.join([`int` for int in int_list]) is fastest
    # some Python implementations like CPython have in-place optimization for string concatenation
    compressed_string_buffer = []
    compress_char = string[0]
    count = 0
    for char in string:
        if char == compress_char:
            count += 1
        else:
            compressed_string_buffer.append(compress_char + `count`)
            compress_char = char
            count = 1
    compressed_string_buffer.append(compress_char + `count`)
    compressed_string = ''.join(compressed_string_buffer)
    return compressed_string if len(compressed_string) < len(string) else string

assert compress_string('aabccccaaa') == 'a2b1c4a3'

