import sys


def bubble_sort(unsorted_list):
    length = len(unsorted_list)
    for i in range(length-1, -1, -1):
        for j in range(i):
            if unsorted_list[j] > unsorted_list[j+1]:
                unsorted_list[j], unsorted_list[j+1] = unsorted_list[j+1], unsorted_list[j]
    return unsorted_list


if __name__ == "__main__":
    if sys.version_info.major < 3:
        input_function = raw_input
    else:
        input_function = input

    user_input = input_function("Enter number seperated by comma:\n")
    unsorted = [int(item) for item in user_input.split(',')]
    print bubble_sort(unsorted)
