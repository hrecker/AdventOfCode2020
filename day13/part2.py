from math import gcd
from functools import reduce

buses = []
#indices = []
modulo = []

with open("input.txt") as input:
    input.readline()
    index = 0
    for bus in input.readline().strip('\n').split(','):
        if bus != 'x':
            buses.append(int(bus))
            #indices.append(index)
            modulo.append((int(bus) - index) % int(bus))
        index += 1

#print("buses: " + str(buses))
#print("")

# This is copied from https://rosettacode.org/wiki/Chinese_remainder_theorem#Python
def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod
 
def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

# Not even sure if this is guaranteed to give a correct answer
print(str(chinese_remainder(buses, modulo)))
