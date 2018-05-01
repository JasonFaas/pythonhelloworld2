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

def apply_shift(message_text, shift):
    '''
    Applies the Caesar Cipher to self.message_text with the input shift.
    Creates a new string that is self.message_text shifted down the
    alphabet by some number of characters determined by the input shift

    shift (integer): the shift with which to encrypt the message.
    0 <= shift < 26

    Returns: the message text (string) in which every character is shifted
         down the alphabet by the input shift
    '''
    shift_dict = build_shift_dict(shift)
    shifted_string = ""
    for unshifted_char in message_text:
        shifted_string += shift_dict.get(unshifted_char)
    return shifted_string


print(build_shift_dict(3))
print(apply_shift("abcdef", 3))
print(apply_shift("abcdef", 2) == "cdefgh")
# print(string.ascii_letters)
# print(string.ascii_lowercase)
