# personal library that features word/sentence processing, and more
from vars.ascii import *

alphabet = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
             'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
               's', 't', 'u', 'v', 'w', 'x', 'y', 'z' ]



class KermLib():
    def __init__(self, version):
        self.version = version

    def text_extraction(self, complex_string):  # removes special characters and converts sentence to simple lowercase text
        new_string_list = []
        new_string_list_words_joined = []
        complex_string = complex_string.lower()
        complex_string_list = complex_string.split()
        for word in complex_string_list:    # creates a list of sub-lists, each sub-list contains each char for each word
            new_string = [char for char in word if char in alphabet]
            new_string_list.append(new_string)
        for sub_list in new_string_list:    # joins each sub-list
            joined_sub_list = ''.join(sub_list)
            new_string_list_words_joined.append(joined_sub_list)
        simplified_string = ' '.join(new_string_list_words_joined)  # joins each list back into a string
        return simplified_string
    
    def get_user_input(self, list_of_permitted_inputs): # only returns a value if its in a list. List must only contain strings
        while True:
            user_input = str(input())
            if user_input not in list_of_permitted_inputs:
                print('Input not recognized. Please try again:')
                continue
            else:
                return user_input
            
    def ascii_run(self):
        print(ascii_kermitine_portrait)
        print(ascii_kermitine)

    def object_matcher(self, principal_object, list_of_potential_objects, target_attribute): # matches 2 objects based on a shared attribute
        for object in list_of_potential_objects:                                        # ATTRIBUTE MUST BE STR
            if getattr(object, target_attribute) == getattr(principal_object, target_attribute):
                return principal_object, object
        return 'no matching objects found'
    


            
            
KermLib = KermLib('2024.11.28.2000.alpha')
