import sys

def selection_sort(array):
    length = len(array)
    for i in range(length):
        least = i
        for k in range(i+1, length):
            if array[k] < array[least]:
                least = k
        array[least], array[i] = array[i], array[least]
    return array


if __name__ == "__main__":
    if sys.version_info.major < 3:
        input_function = raw_input
    else:
        input_function = input
    user_input = input_function("Enter numbers seperated by comma : ")
    unsortedlist = [int(i) for i in user_input.split(',')]
    print selection_sort(unsortedlist)
