import math


def distance_angle(position, target, alpha):
    x1, y1 = position
    x2, y2 = target
    dx = x2-x1
    dy = y2-y1
    distance = math.sqrt(dx**2+dy**2)
    try:
        angle = math.atan2(dy, dx) - alpha
    except ZeroDivisionError:
        angle = alpha
    return round(distance), round(math.degrees(angle))


if __name__ == '__main__':
    robot_xy = [3, 3]
    target_xy = [6, 7]
    alpha = math.radians(30)

    distance, angle = distance_angle(robot_xy, target_xy, alpha)

    print(str(distance) + ", " + str(angle))

    robot_xy = [3, 3]
    target_xy = [4, 2]
    alpha = math.radians(30)

    distance, angle = distance_angle(robot_xy, target_xy, alpha)

    print(str(distance) + ", " + str(angle))

    
