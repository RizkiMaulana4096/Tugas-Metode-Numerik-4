u = 0
n = 100 #batas iterasi maksimal
x = 1
def f(x):
    return (20/((x**2)+2*x+10))
p = f(x)
while p != f(p) and u < n:
    u += 1
    x = p
    p = f(x)
print(f'akar iterasi sederhana: {x}')