

def sort1(arr):

    """
        Approach 1
    """

    l, s = len(arr), sum(arr)
    res = [0] * (l-s) + [1] * s
    return res


def sort2(arr):

    """
        Approach 2
    """

    res = [[], []]

    for i in arr:
        res[i].append(i)
    return res[0] + res[1]


if __name__ == '__main__':
    array = input("Enter the 0,1 as comma separated: ")
    array = [int(i) for i in array.split(',')]
    print(sort2(array))

