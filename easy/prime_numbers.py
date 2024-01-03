def get_prime(num):
    if num == 1 or num == 0:
        print('not possible')
        return 0
    if (num % 2) == 0 or (num % 3) == 0:
        if num == 3:
            print(num)
            print(num - 1)
        elif num == 2:
            print(num)
        else:
            get_prime(num - 1)
    else:
        print(num)
        get_prime(num - 1)


def get_prime_list(num):
    x = [0]
    x.pop()
    while num > 1:
        if (num % 2) == 0 or (num % 3) == 0:
            if num == 3:
                x.append(num)
            elif num == 2:
                x.append(num)
        else:
            x.append(num)
        num -= 1
    return x


if __name__ == "__main__":
    get_prime(0)
    print(get_prime_list(20))
