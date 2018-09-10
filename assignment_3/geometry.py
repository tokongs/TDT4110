r = 0.5
n = 4

x = 1
result = 0

while n >= 0:
    result += x
    x *= r
    n -= 1

print("Summen av rekken er", result)


limit = 2
result = 0
x = 1
number = 0
tol = 0.001

while abs(result - limit) >= tol:
    result += x
    x *= r
    number += 1

print("For å være innenfor tolreansegrensen:", tol, "kjørte løkkken", number, "ganger")
print("Differansen mellom virkelig og esimert verdi var da",  abs(result-limit))

