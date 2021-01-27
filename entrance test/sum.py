def sum_function(n):
    n = int(n)
    if n < 1:
        raise ValueError
    current = 1
    sign = 1
    result = 0
    while current <= n:
        result += sign*current
        sign *= -1
        current += 2
    return result


if __name__ == '__main__':
    while True:
        n = input('Input n: ')
        if n == '0':
            break
        print(sum_function(int(n)))
