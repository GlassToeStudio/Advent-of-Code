from itertools import cycle, repeat

with open('input16', 'r') as data:
    data = data.read().strip()

def phase(number):
    new_number = []
    for i, digit in enumerate(number, start=1):
        coefficients = (coef for base in cycle((0,1,0,-1)) for coef in repeat(base, i))
        next(coefficients)
        new_number.append(abs(sum(digit * next(coefficients) for digit in number)) % 10)
    return new_number

number = list(map(int, data))
for _ in range(100):
    number = phase(number)

print(''.join(map(str, number[:8]))) # Part 1

number = (list(map(int, data)) * 10000)[int(data[:7]):] # Slice at offset

for i in range(100):
    sum_ = sum(number) # Coefficients form upper-triangular matrix of all ones.
    for j, digit in enumerate(number):
        number[j] = abs(sum_) % 10
        sum_ -= digit

print(''.join(map(str, number[:8]))) # Part 2
