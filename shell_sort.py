import sys


def shell_sort(array):
    n = len(array)
    gap = n/2
    while gap > 0:
        for i in range(gap, n):
            temp = array[i]
            j = i
            while j >= gap and array[j-gap] > temp:
                array[j] = array[j-gap]
                j -= gap
            array[j] =  temp
        gap /= 2
    return array


if __name__ == '__main__':
    if sys.version_info.major < 3:
        input_function = raw_input
    else:
        input_function = input
    user_input = input_function("Enter numbers seperated by comma : ")
    unsortedlist = [int(item) for item in user_input.split(',')]
    print shell_sort(unsortedlist)
