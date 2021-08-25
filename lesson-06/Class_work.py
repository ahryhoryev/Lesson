my_dict = {"apple": "яблоко",
           "house": "дом",
           "sky": "небо"}

dict_rus_to_eng = {
    value: key
    for key, value in my_dict.items()
}


def from_eng_to_rus(eng):
    rus = my_dict[eng]
    return rus


print(from_eng_to_rus("apple"))


def from_rus_to_eng(rus):
    eng = my_dict[rus]
    return eng

print(from_rus_to_eng("яблоко"))