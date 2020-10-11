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

    if sys.version_info.major == 2 and sys.version_info.minor < 8:
        input = raw_input
    else:
        input = input

    sample_str = input("Enter the string to reverse: ")
    print("Slicing technique", sample_str[::-1])
    print("using reversed", "".join(reversed(sample_str)))
    print(custom_reverse(sample_str))

# Slicing technique is more effecient
# https://dbader.org/blog/python-reverse-string