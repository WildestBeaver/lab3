# function - y=2^x + ln(-5x)

import math

# f1 = 2 ^ x
def sub_func_1(x: [int, float]) -> [int, float]:
    return math.pow(2, x)

# f2 = ln(-5x)
def sub_func_2(x: [int, float]) -> [int, float]:
    return math.log(-5 * x)

# y = f1 + f2
def main_func(x: [int, float]) -> [int, float]:
    return sub_func_1(x) + sub_func_2(x)
