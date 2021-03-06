import string

### DO NOT MODIFY THIS FUNCTION ###
def load_words(file_name):
    print('Loading word list from file...')
    # inFile: file
    in_file = open(file_name, 'r')
    # line: string
    line = in_file.readline()
    # word_list: list of strings
    word_list = line.split()
    print('  ', len(word_list), 'words loaded.')
    in_file.close()
    return word_list

### DO NOT MODIFY THIS FUNCTION ###
def is_word(word_list, word):
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

### DO NOT MODIFY THIS FUNCTION ###
def get_story_string():
    """
    Returns: a joke in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

WORDLIST_FILENAME = 'words.txt'

class Message(object):
    ### DO NOT MODIFY THIS METHOD ###
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    ### DO NOT MODIFY THIS METHOD ###
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    ### DO NOT MODIFY THIS METHOD ###
    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words[:]

    def build_shift_dict(self, shift):
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
        self.add_case_shift_to_dictionary(string.ascii_lowercase, dictionary_to_return, shift)
        self.add_case_shift_to_dictionary(string.ascii_uppercase, dictionary_to_return, shift)

        return dictionary_to_return

    def add_case_shift_to_dictionary(self, case, dictionary_what, shift):
        for base_char in case:
            char_shift = ord(base_char) + shift
            if char_shift > ord(case[-1:]):
                char_shift -= len(case)
            dictionary_what[base_char] = chr(char_shift)

    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        shift_dict = self.build_shift_dict(shift)
        shifted_string = ""
        for unshifted_char in self.message_text:
            if unshifted_char in shift_dict:
                shifted_string += shift_dict.get(unshifted_char)
            else:
                shifted_string += unshifted_char
        return shifted_string

class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encrypting_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        Hint: consider using the parent class constructor so less 
        code is repeated
        '''
        super().__init__(text)
        self.shift = shift
        self.encrypting_dict = self.get_encrypting_dict()

    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''
        return self.shift

    def get_encrypting_dict(self):
        '''
        Used to safely access a copy self.encrypting_dict outside of the class
        
        Returns: a COPY of self.encrypting_dict
        '''
        return self.build_shift_dict(self.get_shift()).copy()

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''
        return self.apply_shift(self.get_shift())

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift (ie. self.encrypting_dict and 
        message_text_encrypted).
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        self.shift = shift


class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object

        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        super().__init__(text)

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value
        for decrypting it.

        Note: if multiple shifts are  equally good such that they all create
        the maximum number of you may choose any of those shifts (and their
        corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        best_shift_count = -1
        best_shift_value = -1
        best_shift_string = ""
        for shift_value in range(0, 26):
            shiftie = self.apply_shift(shift_value)
            split = shiftie.split(' ')
            current_shift_count = 0
            for single_split_word in split:
                if is_word(self.valid_words, single_split_word):
                    current_shift_count += 1
            if current_shift_count > best_shift_count:
                best_shift_string = shiftie
                best_shift_value = shift_value
                best_shift_count = current_shift_count
        return (best_shift_value, best_shift_string)


#Example test case (PlaintextMessage)
original_plain_text = 'hello my name is test'
plaintext = PlaintextMessage(original_plain_text, 6)
encrypted_text = plaintext.get_message_text_encrypted()
print(encrypted_text)
# print('jgnnq' == plaintext.get_message_text_encrypted())
# print(plaintext.get_shift() == 2)
# plaintext.change_shift(3)
# print(plaintext.get_shift() == 3)
# print('khoor' == plaintext.get_message_text_encrypted())

cipher_text_message = CiphertextMessage(encrypted_text)
# print(plaintext.get_message_text_encrypted())
decrytped_message = cipher_text_message.decrypt_message()
print(decrytped_message)
print(type(decrytped_message))
print(original_plain_text == decrytped_message)
# print(plaintext.get_shift() == 2)
# plaintext.change_shift(3)
# print(plaintext.get_shift() == 3)
# print('khoor' == plaintext.get_message_text_encrypted())
