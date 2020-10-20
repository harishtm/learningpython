import random
import sys

def random_element_uppercase(st):
    ch = list(st)
    random_list = random.sample(range(len(ch)), len(ch)//2)
    for i, _ in enumerate(ch):
        if i in random_list:
            ch[i] = ch[i].upper()
    return "".join(ch)


if __name__ == "__main__":

    if sys.version_info.major == 2 and sys.version_info.minor < 8:
        input = raw_input
    else:
        input = input

    sample_str = input("Enter the string to convert random elements to upper case: ")
    print(random_element_uppercase(sample_str))
