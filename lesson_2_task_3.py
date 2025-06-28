import math


def square(x):

    s = x**2
    return s


x = float(input("Длинна стороны квадрата: "))
result = square(x)
rounded_result = math.ceil(result)


print(f'Округленная в большую сторону сумма - {rounded_result}')
