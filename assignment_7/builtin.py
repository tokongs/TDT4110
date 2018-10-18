import random

random_numbers = []

for x in range(100):
    random_numbers.append(random.randint(1, 10))

twos = 0
for x in random_numbers:
    if x == 2:
        twos +=1

print("Number of 2s:", twos)

sum =0
for x in random_numbers:
    sum += x

print("Sum of number:", sum)

temp = []
while random_numbers:
    min = random_numbers[0]
    for x in random_numbers:
        if x < min:
            min = x
    random_numbers.remove(min)
    temp.append(min)

random_numbers = temp
print("Numbers sorted: ", random_numbers)


type_number = []
for x in range(10):
    type_number.append(0)

for x in random_numbers:
    type_number[x-1] += 1

max = 0
for x in range(1, 10):
    if(type_number[x] > type_number[max]):
        max = x

print("There are most number:", max + 1)

temp = []
for x in reversed(random_numbers):
    temp.append(x)

print("Numbers reversed:", temp)

