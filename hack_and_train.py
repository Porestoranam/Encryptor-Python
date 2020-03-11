import math
import string
import collections
from encode_and_decode import number_of_lowercase_letters
from encode_and_decode import caesar_encode_string

lowercase_set = set(string.ascii_lowercase)
letters_set = set(string.ascii_letters)


def count_ideal_allocation(text_for_train):
    """return ideal_allocation approximation"""
    ideal_allocation = collections.Counter(ch.lower() for ch in text_for_train if ch in letters_set)
    length = sum(ideal_allocation.values())
    for letter in lowercase_set:
        ideal_allocation[letter] /= length
    return ideal_allocation


def answer_shift_func(main_string, ideal_allocation):
    """returns answer shift, which fits us"""
    cur_allocation = collections.Counter(ch.lower() for ch in main_string if ch in letters_set)
    length = sum(cur_allocation.values())
    ans_shift = 0
    ans_value = float("inf")
    for shift in range(0, number_of_lowercase_letters):
        value_of_the_differences = 0
        for char in lowercase_set:
            cur_char = chr((ord(char) - ord('a') - shift) % number_of_lowercase_letters + ord('a'))
            value_of_the_differences += math.fabs(ideal_allocation[char] - cur_allocation[cur_char]/length)
        if value_of_the_differences < ans_value:
            ans_value = value_of_the_differences
            ans_shift = shift
    return ans_shift


def changed_text(main_string, ideal_allocation):
    """returns changed_text with the best approximation"""
    ans_shift = answer_shift_func(main_string, ideal_allocation)
    return caesar_encode_string(main_string, ans_shift)
