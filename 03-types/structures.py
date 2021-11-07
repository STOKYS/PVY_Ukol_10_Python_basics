import re
import string
import sys


def char_frequency(sentence):
    sntc_dict = {}
    for x in sentence:
        keys = sntc_dict.keys()
        if x in keys:
            sntc_dict[x] += 1
        else:
            sntc_dict[x] = 1
    sntc_list = [(x, y) for x, y in sntc_dict.items()]
    sntc_list.sort(key=lambda x: x[1], reverse=True)
    return sntc_list


def main():
    sentence = "Tři sta třicet tři stříbrných stříkaček stříkalo přes tři sta třicet tři stříbrných střech"
    print(f"Veta: {sentence}\nCetnost pismen: {char_frequency(sentence)}")


if __name__ == "__main__":
    main()