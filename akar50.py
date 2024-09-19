def f(x):
    return (x**2)-50
def biseksi(f,a,b ,toleransi ,max_iterasi = 100):
    if f(a)*f(b) > 0 :
        print(f"akar tidak ditemukan di antara {a} dan {b}")
    n = 0
    while b-a > toleransi and n < max_iterasi:
        x = (a+b)/2
        if f(x) == 0:
            return x
        elif f(a)*f(x) < 0:
            b = x
        else:
            a = x
        n += 1
    print(f"n_iterasi = {n}")
    print(f"error biseksi = {b-a}")
    return (a+b)/2

def regulafalsi(f,a,b,toleransi ,max_iterasi = 100):
    if f(a)*f(b) > 0 :
        print(f"akar tidak ditemukan di antara {a} dan {b}")
    n = 0
    x = (a*f(b)-b*f(a))/(f(b)-f(a))
    while abs(f(x)) > toleransi and n < max_iterasi:
        n += 1
        if f(x) == 0:
            print(f"n_iterasi = {n}")
            print(f"error regulfalsi = {f(x)}")
            return x
        elif f(a)*f(x) < 0:
            b = x
        else:
            a = x
        x = (a*f(b)-b*f(a))/(f(b)-f(a))
    print(f"n_iterasi  = {n}")
    print(f"error regulafalsi = {f(x)}")
    return x

a, b = 0, 10
k = 1
for i in range (1,7):
    k *= 0.1
    print(f"batas toleransi = {k}")
    akar50b = biseksi(f,a,b,k)
    print(f"akar50 Biseksi = {akar50b}")
    akar50rf = regulafalsi(f,a,b,k)
    print(f"akar50 Regulafalsi = {akar50rf}")
    print("---------------------------------------")