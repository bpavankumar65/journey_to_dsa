def factorial(num):
    x = 1

    while num > 0:
        if num == 0:
            return 1
        x *= num
        num -= 1
    return x


def factorial_second(num):
    x = 1
    for i in range(num, 0, -1):
        if num == 0:
            return 1
        x *= i
    print(x)
    return x

    pass


def factorial_third(num):
    if num != 0:
        return num * factorial_third(num - 1)
    else:
        return 1


if __name__ == "__main__":
    print(factorial(0))
    print(factorial_second(0))
    print(factorial_third(7))
