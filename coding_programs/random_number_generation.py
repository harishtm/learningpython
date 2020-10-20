import sys
import time

def random_number(x):
    random = int(time.time() * 1000)
    random %= x
    return "The random number generated is {}".format(random)


if __name__ == "__main__":

    if sys.version_info.major == 2 and sys.version_info.minor < 8:
        input = raw_input
    else:
        input = input

    rg_num = int(input("Enter the number to get random number with in that number: "))
    print(random_number(rg_num))
