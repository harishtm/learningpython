def greeting(name: str) -> str:
    return 'Hello ' + name


if __name__ == '__main__':
    name = int(input('Enter your name : '))
    print(greeting(name))
