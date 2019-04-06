def new_char(char, shift):
    """make new char using value of shift"""
    ord_char = ord(char)
    dis_from_cap_a = ord_char - ord('A')
    dis_from_cap_z = ord('Z') - ord_char
    dis_from_a = ord_char - ord('a')
    dis_from_z = ord('z') - ord_char
    if (dis_from_cap_a >= 0) and (dis_from_cap_z >= 0):
        new_ord = (ord_char - ord('A') + shift) % 26 + ord('A')
        return chr(new_ord)
    elif (dis_from_a >= 0) and (dis_from_z >= 0):
        new_ord = (ord_char - ord('a') + shift) % 26 + ord('a')
        return chr(new_ord)
    else:
        return char


def caesar_encode_string(main_string, shift):
    """"encode caesar string"""
    new_string = ''
    for char in main_string:
        new_string += new_char(char, shift)
    return new_string


def caesar_decode_string(main_string, shift):
    return caesar_encode_string(main_string, (-1) * shift)


def vigenere_encode(my_string, key):
    """return string encode like vigenere"""
    length = len(key)
    new_string = ''
    for i in range(0, len(my_string)):
        cur_key = key[i % length]
        if (ord(cur_key) >= ord('a')) and (ord(cur_key) <= ord('z')):
            new_string += new_char(my_string[i], ord(cur_key) - ord('a'))
        elif (ord(cur_key) >= ord('A')) and (ord(cur_key) <= ord('Z')):
            new_string += new_char(my_string[i], ord(cur_key) - ord('A'))
        else:
            new_string += my_string[i]
    return new_string


def vigenere_decode(my_string, key):
    """return string decode like vigenere"""
    length = len(key)
    new_string = ''
    for i in range(0, len(my_string)):
        cur_key = key[i % length]
        if (ord(cur_key) >= ord('a')) and (ord(cur_key) <= ord('z')):
            new_string += new_char(my_string[i], ord('a') - ord(cur_key))
        elif (ord(cur_key) >= ord('A')) and (ord(cur_key) <= ord('Z')):
            new_string += new_char(my_string[i],  ord('A') - ord(cur_key))
        else:
            new_string += my_string[i]
    return new_string
