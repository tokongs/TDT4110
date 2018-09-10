k = int(input("Hvor mange tall vil du regne ut "))

fib = [0 for x in range(k)]
fib[0] = 0
fib[1] = 1

summ = 1
for x in range(2, k):
    fib[x] = fib[x-1] + fib[x-2]
    summ += fib[x]

print("Fibonacci talled på", k, "er", fib[k-1])
print("Summen av tallene opp til fibonacci tallet på", k, "er", summ)


print("Rekken går som følger")
for x in range(0, k):
    print(fib[x])
