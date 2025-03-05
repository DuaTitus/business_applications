import math


def f(x):
    return 3 - 0.5 * (x ** 0.5) - math.exp(-0.5 * (x ** 2))


def bisection_method(func, a, b, tol=1e-5, max_iter=100):
    if func(a) * func(b) >= 0:
        raise ValueError("Функция должна иметь разные знаки на концах интервала")

    iteration = 0
    while (b - a) / 2 > tol and iteration < max_iter:
        midpoint = (a + b) / 2
        if func(midpoint) == 0:
            return midpoint
        elif func(a) * func(midpoint) < 0:
            b = midpoint
        else:
            a = midpoint
        iteration += 1

    return (a + b) / 2


bisection_root = bisection_method(f, 0, 100)
print(f'Приблизительный корень: {bisection_root}')
