
def sort3way(a, arr_size):

    low = 0
    mid = 0
    high = arr_size - 1

    while mid <= high:
        if a[mid] == 0:
            a[low], a[mid] = a[mid], a[low]
            low += 1
            mid += 1
        elif a[mid] == 1:
            mid += 1
        else:
            a[mid], a[high] = a[high], a[mid]
            high -= 1
    print("The sorted array is\n")
    return a


if __name__ == '__main__':
    array = input("Enter the 0,1,2 as comma separated: ")
    array = [int(i) for i in array.split(',')]
    print(sort3way(array, len(array)))

