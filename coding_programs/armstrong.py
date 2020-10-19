"""
    Armstrong

    A positive integer is called an Armstrong number of order n if

    abcd... = a power n + b power n + c power n + d power n + ...

    153 = 1*1*1 + 5*5*5 + 3*3*3  // 153 is an Armstrong number.

"""

import sys


def armstrong(num):

    order = len(str(num))
    total_sum = 0
    temp = num

    while temp > 0:
        digit = temp % 10
        total_sum += digit ** order
        temp //= 10

    if num == total_sum:
        return "{} is an Armstrong number".format(num)
    else:
        return "{} is not an Armstrong number".format(num)


if __name__ == "__main__":
    if sys.version_info.major == 2 and sys.version_info.minor < 8:
        input = raw_input
    else:
        input = input
    num = int(input("Enter the number: "))
    print(armstrong(num))