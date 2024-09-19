import math
def f_1(x):
    return 2*x - 2*(math.sin(x)+x*math.cos(x))*math.exp(-2*x*math.sin(x))
def f_2(x):
    return 2 + 4*((math.sin(x)+x*math.cos(x))**2)*math.exp(-2*x*math.sin(x)) - 2*(2*math.cos(x)-x*math.sin(x))*math.exp(-2*x*math.sin(x))

max_iterasi = 100
toleransi = 1e-6

def newton_raphson(x0 = 1,max_iterasi = 100, toleransi = 1e-6):
    x = x0
    n = 0
    while abs(f_1(x)) > toleransi and n < max_iterasi:
        n += 1
        if f_2(x) != 0:
            if f_1(x) != 0:
                x = x - f_1(x)/f_2(x)
            else:
                print("nilai divergen")
                return None
        else:
            print("Error dibagi nol")
            return None
    print(f"n_iterasi = {n}")
    print(f"nilai max f(x) = {x}")
    print(f"error = {f_1(x)}")
newton_raphson()