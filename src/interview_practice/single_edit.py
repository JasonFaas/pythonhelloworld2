#two words one edit

def two_words_same_with_one_edit(first, second):
    if abs(len(first) - len(second)) > 1:
        return False

    long = first
    short = second
    if len(long) < len(short):
        short = first
        long = second

    difference_detected = False
    if len(long) == len(short):
        for i in range(len(long)):
            if short[i] != long[i]:
                if difference_detected:
                    return False
                else:
                    difference_detected = True
    else:
        for i in range(len(short)):
            if not difference_detected:
                if short[i] != long[i]:
                    difference_detected = True

            if difference_detected and short[i] != long[i+1]:
                return False

    return True

import numpy as np





assert_array = np.empty(shape=0, dtype=bool)
# assert_array = np.append(assert_array, [True], axis=0)
# assert_array = np.append(assert_array, [not two_words_same_with_one_edit("ab", "")], axis=0)
# assert_array = np.append(assert_array, [not two_words_same_with_one_edit("", "ba")], axis=0)
# assert_array = np.append(assert_array, [two_words_same_with_one_edit("a", "a")], axis=0)
# assert_array = np.append(assert_array, [two_words_same_with_one_edit("a", "")], axis=0)
# assert_array = np.append(assert_array, [two_words_same_with_one_edit("", "a")], axis=0)
# assert_array = np.append(assert_array, [two_words_same_with_one_edit("abc", "abcd")], axis=0)
# assert_array = np.append(assert_array, [two_words_same_with_one_edit("abd", "abcd")], axis=0)
# assert_array = np.append(assert_array, [not two_words_same_with_one_edit("bbc", "abcd")], axis=0)
# assert_array = np.append(assert_array, [two_words_same_with_one_edit("abce", "abcd")], axis=0)
# assert_array = np.append(assert_array, [not two_words_same_with_one_edit("bbce", "abcd")], axis=0)
assert two_words_same_with_one_edit("bc", "abc")
assert two_words_same_with_one_edit("abc", "ac")
print(assert_array)
