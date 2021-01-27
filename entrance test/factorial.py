def factorial(n):
    if n <= 1:
        return 1
    else:
        return n*factorial(n-1)


def factorial2(n):
    if n <= 0:
        return 1
    else:
        return n*factorial(n-1)


def factorial3(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res


if __name__ == '__main__':
    print(factorial(5))
    print(factorial2(5))
    print(factorial3(5))
