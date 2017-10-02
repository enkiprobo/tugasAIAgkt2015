import random


# definisi fungsi
def fungsi(a, b):
    return ((4 - (2.1 * (a ** 2)) + ((a ** 4) / 3)) * (a ** 2)) + (a * b) + ((-4 + (4 * (b ** 2))) * (b ** 2))



def probabilitas(a, b, c):
    return 2.71828183 ** ((a-b)/c)



# deklarasi variabel
temp = 10000
alpha = 0.999
r = random.uniform(0,1)
x1 = random.uniform(-10, 10)
x2 = random.uniform(-10, 10)
bestsofar = fungsi(x1, x2)

#algoritma SA
while (temp > 0.00001):
    for x in range(30):
        x1 = random.uniform(-10, 10)
        x2 = random.uniform(-10, 10)
        newstate = fungsi(x1, x2)
        if (newstate>bestsofar):
            if (probabilitas(bestsofar, newstate, temp) > r):
                    bestsofar = newstate

        else:
                bestsofar = newstate

    temp=alpha*temp

print(bestsofar)
