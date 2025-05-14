import random
import string

letters_low = list(string.ascii_lowercase)
letters_up = list(string.ascii_uppercase)
letters = letters_low + letters_up
def CharacterReplace(string):
    string_list = list(string)
    while True:
        ran_int = random.randint(0, len(string)-1)
        if string[ran_int] in letters:
            break
    while True:
        ori = string_list[ran_int]
        string_list[ran_int] = random.choice(letters)
        if string_list[ran_int] != ori:
            break
    return ''.join(string_list)

def CharacterDelete(string):
    string_list = list(string)
    ran_int = random.randint(0, len(string)-1)
    del string_list[ran_int]
    return ''.join(string_list)

def CharacterAdd(string):
    ran_int = random.randint(0, len(string))
    char = random.choice(letters)
    return string[:ran_int] + char + string[ran_int:]

def SpaceAdd(string):
    ran_int = random.randint(0, len(string))
    return string[:ran_int] + " " + string[ran_int:]

def CharacterSwap(string):
    string_list = list(string)
    while True:
        ran_int_1 = random.randint(0, len(string)-1)
        ran_int_2 = random.randint(0, len(string)-1)
        if string[ran_int_1] != string[ran_int_2]:
            string_list[ran_int_1], string_list[ran_int_2] = string_list[ran_int_2], string_list[ran_int_1]
            break
    return "".join(string_list)

a = "abcdefg"
b1 = CharacterReplace(a)
b2 = CharacterDelete(a)
b3 = CharacterAdd(a)
b4 = SpaceAdd(a)
b5 = CharacterSwap(a)
print(b1)
print(b2)
print(b3)
print(b4)
print(b5)