import sys
import math
import matplotlib.pyplot as plt

x_0 = 0
x_n = 1

y_0 = 2

N = (10, 20, 30)
n = None


def get_y(x):
    return math.sqrt(4 - 2 * x * x)


def f(x, y):
    return -2 * x / y


def df1(x, y):
    return (-2 * (y ** 2) - 4 * (x**2)) / (y ** 3)


def df2(x, y):
    return -4 * (y - x) / (y ** 3)


def df3(x, y):
    return 12 * (x - y) / y ** 4


def get_arrs(f):
    f(n)

    for _n in N:
        x, y = euler(_n)
        plt.plot(x, y, label=f"N={_n}")

    arr_x = [x_0 + i * (x_n - x_0) / n for i in range(n + 1)]
    arr_y = list(map(get_y, arr_x))

    return arr_x, arr_y


def main():
    global n
    n = int(sys.argv[1])

    '''Эйлер'''
    arr_x, arr_y = get_arrs(euler)
    plt.plot(arr_x, arr_y, label="Эйлер")
    plt.legend()
    plt.show()

    '''С пересчетом'''
    arr_x, arr_y = get_arrs(euler_with_recalc)
    plt.plot(arr_x, arr_y, label="Эйлер с пересчетом")
    plt.legend()
    plt.show()

    '''Тейлор'''
    arr_x, arr_y = get_arrs(taylor)
    plt.plot(arr_x, arr_y, label="Тейлор")
    plt.legend()
    plt.show()


def euler(n):
    act_x = [x_0]
    act_y = [y_0]
    x = x_0
    h = (x_n - x_0) / n

    for i in range(n):
        y = (act_y[i] + math.sqrt(((act_y[i] ** 2) - 8 * (x + h) * h))) / 2
        x += h
        act_y.append(y)
        act_x.append(x)

    return act_x, act_y


def euler_with_recalc(n):
    act_x = [x_0]
    act_y = [y_0]
    x = x_0
    h = (x_n - x_0) / n

    for i in range(n):
        y_ = act_y[i] + h * f(x, act_y[i])
        y = act_y[i] + h / 2 * (f(x, act_y[i]) + f(x + h, y_))
        x += h
        act_y.append(y)
        act_x.append(x)

    return act_x, act_y


def taylor(n):
    act_x = [x_0]
    act_y = [y_0]
    x = x_0
    h = (x_n - x_0) / n

    for i in range(n):
        y = act_y[i] + h * f(x, act_y[i]) + (h ** 2) / 2 * df1(x, act_y[i])
        x += h
        act_y.append(y)
        act_x.append(x)

    return act_x, act_y


if __name__ == '__main__':
    main()
