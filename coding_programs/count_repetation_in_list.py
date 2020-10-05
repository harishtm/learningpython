# Find the counf of each item and find the max


class CountTheRepeated:

    def logic1(self, l):
        """
            Find the count and return the highest and lowest
        """
        res, temp = {}, []
        for i in l:
            if i not in temp:
                res[i] = 1
                temp.append(i)
            else:
                res[i] = res[i] + 1
        dt = self.get_max_val_by_key(res)
        mx, mi = dt[0], dt[1]
        return {mx:res[mx], mi:res[mi]}

    def logic2(self, l):
        """
            Find only the count
        """
        res = {}
        for i in l:
            try:
                res[i] += 1
            except KeyError:
                res[i] = 1
        return res

    def logic3(self, l):
        """
            Find only the count
        """
        res = {}
        list2 = list(set(l))
        for element in l:
            res[element] = l.count(element)
        return res

    def find_max(self, data):
        # return max(data, key=data.get)
        return max(data, key=lambda x:data[x])

    def get_max_val_by_key(self, data):
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
    data = ["apple", "orange", "banana", "orange", "apple", "banana", "pineapple",\
             "apple", "orange", "strawberry", "orange", "strawberry"]
    inst = CountTheRepeated()
    print(inst.logic1(data))
    print(inst.logic2(data))
    print(inst.logic3(data))

