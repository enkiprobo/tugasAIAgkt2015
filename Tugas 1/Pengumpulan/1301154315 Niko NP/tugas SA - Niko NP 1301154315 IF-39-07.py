import random
import math

def rumus(N1, N2) :
    fungsi = ((4 - (2.1 * (N1 ** 2)) + ((N1 ** 4) / 3))) * (N1 ** 2) + (N1 * N2) + (-4 + (4 * (N2 ** 2))) * (N2 ** 2)
    return fungsi

S1 = random.uniform(-10, 10)
S2 = random.uniform(-10, 10)

f = rumus(S1,S2)

Smax = 1000000  #temp
A = 0.99 #coolingrate
S = 1 #batas minimum temp

while (Smax > S):
    N1 = random.uniform(-10, 10)
    N2 = random.uniform(-10, 10)
    f2 = rumus(N1, N2)
    if (f > f2):
        f = f2
    else:
        t = (f - f2) / Smax
        e = math.exp(t)
        if (e > random.uniform(0, 1)):
            f = f2
    Smax = Smax * A
print(S1)
print(S2)
print(f)

