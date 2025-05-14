import random

start_ch = 0x4e00
end_ch = 0x9fff

def CharacterReplace(string):
    string_list = list(string)
    while True:
        ran_int = random.randint(0, len(string)-1)
        if start_ch <= ord(string[ran_int]) <= end_ch:
            break
    while True:
        ori = string_list[ran_int]
        string_list[ran_int] = chr(random.randint(start_ch, end_ch))
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
    char = chr(random.randint(start_ch, end_ch))
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

# 示例
original_sentence = "这是个示例中文句子"
new_sentence = CharacterSwap(original_sentence)

print("原始句子:", original_sentence)
print("新句子:", new_sentence)