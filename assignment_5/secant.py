from math import e

def f(x):
    return (x-12)*e**(x/2)-8*(x+2)**2

def g(x):
    return -x-2*x**2-5*x**3+6*x**4

print(f(0))
print(g(1))


def differentiate(x_k, x_k1, func):
    return (func(x_k)-func(x_k1))/(x_k-x_k1)

print(differentiate(9, 10, f))

def secant_method(x0, x1, func, tol):
    xn = x1 - func(x1)/differentiate(x0, x1, func)
    y = func(xn)
    while not(y < tol and y > -tol):
        x0 = x1
        x1 = xn
        xn = x1 - func(x1)/differentiate(x0, x1, func)
        y = func(xn)



    return xn

    
print(secant_method(11, 13, f, 0.00001))
print(secant_method(1, 2, g, 0.00001))
print(secant_method(0, 1, g, 0.00001))