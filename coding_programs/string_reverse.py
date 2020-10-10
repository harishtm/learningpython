import sys

def custom_reverse(sample_str):
    """
        Function to reverse string without using [::-1] or built in
    """
    ch = list(sample_str)
    for i in range(len(sample_str) // 2):
        tmp = ch[i]
        ch[i] = ch[len(sample_str) - i -1]
        ch[len(sample_str) - i -1] = tmp
    return "".join(ch)


if __name__ == "__main__":

    if sys.version_info < (2,6,0):
        input = input
    else:
        input = raw_input

    sample_str = input("Enter the string to reverse: ")
    print(custom_reverse(sample_str))
