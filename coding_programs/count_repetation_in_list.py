# Find the counf of each item and find the max

def count_repetation(l):
    res, temp = {}, []
    for i in l:
        if i not in temp:
            res[i] = 1
            temp.append(i)
        else:
            res[i] = res[i] + 1
    dt = get_max_val_by_key(res)
    mx, mi = dt[0], dt[1]
    return {mx:res[mx], mi:res[mi]}


"""
# Other way
def count_repetation(l):
    res = {}
    for i in l:
        try:
            res[i] += 1
        except KeyError:
            res[i] = 1
    return res
"""

def find_max(data):
    # return max(data, key=data.get)
    return max(data, key=lambda x:data[x])

def get_max_val_by_key(data):
    max_value = None
    min_value = None
    for key in data:
        if max_value is None or max_value < data[key]:
            max_value = data[key]
            max_key = key
        if min_value is None or min_value > data[key]:
            min_value = data[key]
            min_key = key
    return max_key, min_key


if __name__ == "__main__":
    l = ['apple', 'mango', 'apple', 'mango', 'orange', 'apple']
    print(count_repetation(l))


# duplicates