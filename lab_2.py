import math
import numpy as np

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

def secant_method_np(func, x0, x1, tol=1e-5, max_iter=100):
    for i in range(max_iter):
        f_x0 = func(x0)
        f_x1 = func(x1)
        if np.abs(f_x1) < tol:
            return x1
        x2 = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)
        x0, x1 = x1, x2
    raise ValueError("Метод секущих не сошелся")

def numerical_derivative(func, x, h=1e-5):
    return (func(x + h) - func(x)) / h

def newton_method_numerical(func, x0, tol=1e-5, max_iter=100, h=1e-5):
    x = x0
    for i in range(max_iter):
        f_x = func(x)
        df_x = numerical_derivative(func, x, h)
        if np.abs(f_x) < tol:
            return x
        if df_x == 0:
            raise ValueError("Производная равна нулю. Метод Ньютона не может продолжаться.")
        x = x - f_x / df_x
    raise ValueError("Метод Ньютона не сошелся")

newton_root = newton_method_numerical(f, 3.0)
print(f"Приближенное значение корня (метод Ньютона): {newton_root}")

secant_root = secant_method_np(f, 1.0, 3.0)
print(f"Приближенное значение корня (метод секущих): {secant_root}")

bisection_root = bisection_method(f, 0, 100)
print(f"Приближенное значение корня (метод бисекции): {bisection_root}")
