import math

x = 0.2

def ctg(x):
    return 1 / math.tan(x)

while x <= 0.8:
    if x < 0.5:
        func1 = abs(math.log(x)) ** 7
        print("Function 1:", func1)
    elif 0.5 <= x < 0.7:
        func2 = ctg(x + x**3)
        print("Function 2:", func2)
    elif x >= 0.7:   
        func3 = math.log(math.sin(x)) / math.log(5)
        print("Function 3:", func3)
    
    x += 0.02  



   
a = 0.1
b = 0.5
h = 0.05
d = 0.001
m = 20

def series_function(x):
    term = 1
    sum_series = 1
    n = 1
    while abs(term) > d:
        term *= (m - n + 1) * x / n
        sum_series += term
        n += 1
    return sum_series

x = a
while x <= b:
    print(f"x = {x:.2f}, y = {series_function(x):.6f}")
    x += h

