import sys


def binary_search(sorted_collection, item):
    low = 0
    high = len(sorted_collection) - 1

    while low <= high:
        mid = (low + high) // 2
        current_item = sorted_collection[mid]
        if current_item == item:
            return mid
        else:
            if item < current_item:
                high = mid - 1
            else:
                low = mid + 1
    return None


def __assert_sorted(sequence):
    if sequence != sorted(sequence):
        raise ValueError('Collection must be sorted')
    return True


if __name__ == '__main__':

    if sys.version_info.major < 3:
        input_function = raw_input
    else:
        input_function = input
    user_input = input_function('Enter the numbers seperated by comas : ')
    sequence = [int(item) for item in user_input.split(',')]
    try:
        __assert_sorted(sequence)
    except ValueError:
        sys.exit('Sequence must be sorted to apply binary search')
    target = int(input_function('Enter the item to find in the list : '))
    result = binary_search(sequence, target)
    if result != None:
        print "{0} found at position {1}".format(target, result)
    else:
        print "Not found"

