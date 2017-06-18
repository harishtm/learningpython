import sys


def linear_search(sequence, item):

    for index, value in enumerate(sequence):
        if item == value:
            return index
    return None


if __name__ == '__main__':
    if sys.version_info.major < 3:
        input_function = raw_input
    else:
        input_function = input

    user_input = input_function("Enter the number in sequence seperated by comma : ")
    sequence = [int(item) for item in user_input.split(',')]
    target = int(input_function("Enter the number to be found in the sequence : "))
    result = linear_search(sequence, target)
    if result is not None:
        print "Item {0} found at position {1}".format(str(target), str(result))
    else:
        print "Not found"
