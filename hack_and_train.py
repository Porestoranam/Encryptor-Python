import math
import string


def new_char(char, shift):      # make new char with using value of shift
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


def make_dic_of_alphabet():     # base dict with null
    dic = dict()
    for symbol in string.ascii_letters:
        dic[symbol] = 0
    dic['length'] = 0
    return dic


def count_approximate(main_string):   # return dict of allocation(v) letters for main_string
    allocation_for_string = make_dic_of_alphabet()
    for symbol in main_string:
        if symbol in string.ascii_letters:
            allocation_for_string[symbol] += 1
    length = len(main_string)
    for key in allocation_for_string.keys():
        allocation_for_string[key] /= length    # float
    return allocation_for_string


def value_of_approximate(allocation_for_string, ideal_allocation):  # return value of similarity
    value = 0
    for letter in string.ascii_letters:
        value += math.fabs(allocation_for_string[letter] - ideal_allocation[letter])
    return value


def get_all_opportunities(main_string):  # get all strings we can
    opportunities_strings = []
    for shift in range(0, 26):
        current_string = ''
        for char in main_string:
            current_string += new_char(char, shift)
        opportunities_strings.append(current_string)
    return opportunities_strings


def count_ideal_allocation(text_for_train):         # return ideal_allocation approximation
    ideal_allocation = make_dic_of_alphabet()
    length_text_for_train = len(text_for_train)
    for symbol in text_for_train:
        if symbol in string.ascii_letters:
            ideal_allocation[symbol] += 1
    for letter in string.ascii_letters:
        ideal_allocation[letter] /= length_text_for_train
    ideal_allocation['length'] = length_text_for_train
    return ideal_allocation


def make_dict_of_strings_and_values(main_string, ideal_allocation):     # return value for each string
    opportunities_strings = get_all_opportunities(main_string)
    dict_of_strings_and_values = dict()
    for obj in opportunities_strings:
        allocation_for_string = count_approximate(obj)
        dict_of_strings_and_values[obj] = value_of_approximate(allocation_for_string, ideal_allocation)
    return dict_of_strings_and_values


def answer(main_string, ideal_allocation):  # return ans_string
    ans = 106.0
    ans_string = ''
    dict_of_strings_and_values = make_dict_of_strings_and_values(main_string, ideal_allocation)
    for key, value in dict_of_strings_and_values.items():
        if ans > value:
            ans = value
            ans_string = key
    return ans_string
