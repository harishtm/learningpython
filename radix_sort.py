import sys

def radixsort(array):
    RADIX = 5
    maxLength = False
    tmp, placement = -1, 1

    while not maxLength:
        maxLength = True
        # declare and initialize buckets
        buckets = [list() for _ in range(RADIX)]

        # split array between list
        for i in array:
            tmp = i / placement
            buckets[tmp % RADIX].append(i)
            if maxLength and tmp > 0:
                maxLength = False

        # empty lists into array
        a = 0
        for b in range(RADIX):
            buck = buckets[b]
            for i in buck:
                array[a] = i
                a += 1

        # move to next
        placement *= RADIX
    return buckets


if __name__ == "__main__":
    if sys.version_info.major < 3:
        input_function = raw_input
    else:
        input_function = input

    user_input = input_function("Enter number seperated by comma:\n")
    unsorted = [int(item) for item in user_input.split(',')]
    print radixsort(unsorted)
