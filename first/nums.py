def plus(a, b):
    return a + b


def minus(a, b):
    return a - b


def nul(a, b):
    return a * b


for i in range(-12, 8, 2):
    print(i, end="; ")

if __name__ == '__main__':
    print(plus(2, 2))
    print(minus(4, 2))
    print(nul(3, 3))
