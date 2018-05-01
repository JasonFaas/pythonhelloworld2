import string

def build_shift_dict(shift):
    '''
    Creates a dictionary that can be used to apply a cipher to a letter.
    The dictionary maps every uppercase and lowercase letter to a
    character shifted down the alphabet by the input shift. The dictionary
    should have 52 keys of all the uppercase letters and all the lowercase
    letters only.

    shift (integer): the amount by which to shift every letter of the
    alphabet. 0 <= shift < 26

    Returns: a dictionary mapping a letter (string) to
             another letter (string).
    '''
    dictionary_to_return = {}
    addCaseShiftToDictionary(string.ascii_lowercase, dictionary_to_return, shift)
    addCaseShiftToDictionary(string.ascii_uppercase, dictionary_to_return, shift)

    return dictionary_to_return


def addCaseShiftToDictionary(case, dictionary_what, shift):
    for base_char in case:
        char_shift = ord(base_char) + shift
        if char_shift > ord(case[-1:]):
            char_shift -= len(case)
        dictionary_what[base_char] = chr(char_shift)


print(build_shift_dict(3))
print(string.ascii_letters)
print(string.ascii_lowercase)
