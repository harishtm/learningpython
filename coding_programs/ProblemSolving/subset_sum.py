def subset_sum(numbers, target, partial=[]):

    """
    # For product combination
    if len(partial) == 2:
        s = partial[0] * partial[1]
    else:
        s = 0
    """

    s = sum(partial)

    # check if the partial sum is equals to target
    if s == target: 
        print("sum(%s)=%s" % (partial, target))
    if s >= target:
        return  # if we reach the number why bother to continue

    for i in range(len(numbers)):
        n = numbers[i]
        remaining = numbers[i+1:]
        subset_sum(remaining, target, partial + [n])

if __name__ == "__main__":

    # subset_sum(list(range(23, 34)), 957)
    subset_sum(list(range(23, 34)), 77)