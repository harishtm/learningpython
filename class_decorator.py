def validate(func):

    def inner(a, b):
        if b == 0:
            print("Zero division error in function decorator")
            return
        return func(a, b)
    return inner


@validate
def divide_1(a, b):
    return a/b


class DivisionValidator:

    def __init__(self, func):
        self.function = func

    def __call__(self, a, b):
        if b == 0:
            print("Zero division error in class decorator")
            return
        return self.function(a, b)

@DivisionValidator
def divide_2(a, b):
    return a/b

if __name__ == "__main__":
    divide_1(1, 0)
    divide_2(1, 0)