def voltage_to_centimeters(v, p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    alpha = (y1-y2)/(x1-x2)
    beta = y1-alpha*x1
    cm = alpha*v + beta
    return int(cm*100)


if __name__ == '__main__':
    p1 = [0.5, 1.3]
    p2 = [3, 0.1]
    print(voltage_to_centimeters(0.5, p1, p2))
