"""
    Program to increment the numeric value in a string and return the processed string

    Input: st = 'xrt123ish-9tq'
    Output: 'xrt124ish-8tq'
"""

import sys


def increment_integer_in_string(st):
    tmp, res = [], []
    for k, i in enumerate(st):
        if i == '-' and st[k+1].isdigit() or i.isdigit():
            tmp.append(i)
        else:
            if tmp:
                tmp = "".join(tmp)
                res.append(str(int(tmp)+1))
            res.append(i)
            tmp = []
    return "".join(res)


if __name__ == "__main__":
    if sys.version_info.major == 2 and sys.version_info.minor < 8:
        input = raw_input
    else:
        input = input
    st = input("Enter the string: ")
    print(increment_integer_in_string(st))