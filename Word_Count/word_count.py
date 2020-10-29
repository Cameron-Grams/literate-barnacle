import re

def count_words(sentence):
    my_dict = {}
    wk_s = sentence
    wk_s = wk_s.lower()

    split = r"[^a-z|'{1}|\d]"
    segments = re.split(split, wk_s)

    segments = [i for i in segments if (i.isalnum() or "'" in i)]
    segments = [i.lstrip(r"[\'|\"]+") for i in segments]
    segments = [i.rstrip(r"[\'|\"]+") for i in segments]

    for n in segments:
        if n in my_dict.keys():
            my_dict[n] += 1
        else:
            my_dict[n] = 1

    return my_dict
