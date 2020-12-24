from collections import Counter
import re


def single_byte_xor(hex_string):
    hex_array = bytearray.fromhex(hex_string)
    string_array = []
    for i in range(256):
        new_array = bytearray([i ^ byte for byte in hex_array])
        try:
            string = new_array.decode('ascii')
        except:
            string = ""
        if string:
            string_array.append(string)
    return string_array


def get_scores(string_array):
    frequency_table = {'e': .1202, 't': .91, 'a': .812, 'o': .768,
                       'i': .731, 'n': .695, 's': .628, 'r': .602,
                       'h': .592, 'd': .432, 'l': .398, 'u': .288,
                       'c': .271, 'm': .261, 'f': .230, 'y': .211,
                       'w': .209, 'g': .203, 'p': .182, 'b': .149,
                       'v': .111, 'k': .069, 'x': .017, 'q': .011,
                       'j': .01, 'z': .07}
    score_array = []
    regex = re.compile("[^abcdefghijklmnopqrstuvwxyz]")
    for string in string_array:
        score = 0
        modified_string = regex.sub('', string.lower())
        if modified_string:
            char_frequency = Counter(modified_string)
            for char in frequency_table.keys():
                score += abs((char_frequency.get(char, 0) - frequency_table[char] * len(modified_string)) ** 2 / (
                        frequency_table[char] * len(modified_string)))
            score_array.append(score / len(modified_string))
        else:
            score_array.append(1e100)
    return score_array


def get_min_score_index(score_array):
    min_index = 0
    min_score = score_array[0]
    test_array = []
    for i, score in enumerate(score_array):
        if score < min_score:
            min_index = i
            min_score = score
            test_array.append(i)
    return min_index


if __name__ == "__main__":
    string_array = single_byte_xor(input("Enter a hex string: "))
    score_array = get_scores(string_array)
    min_index = get_min_score_index(score_array)
    print(string_array[min_index])
