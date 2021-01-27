def display_factors(n):
    print("The factors of", n, "are:")
    for i in range(1, n + 1):
        if n % i == 0:
            print(i)


if __name__ == '__main__':
    display_factors(16)
