import random

a1 = random.uniform(-10,10)
a2 = random.uniform(-10,10)

def fungsi(a1,a2):
    Flama =  (((4-(2.1*(a1**2)))+((a1**4)/3))*(a1**2))+(a1*a2)+((-4+(4*(a2**2)))*(a2**2))
    return Flama

temp = 100000000000000
Clrate = 0.99
min =0.001
cstate = fungsi(a1,a2)

while (temp > min) :
    for i in range (1,10):
        a1 = random.uniform(-10, 10)
        a2 = random.uniform(-10, 10)

        nstate = fungsi(a1, a2)

        if (nstate < cstate):
            cstate = nstate
        else:
            probabilitas = 2.7182818284 ** (-1 * (nstate - cstate) / temp)
            if (probabilitas > random.random()):
                cstate = nstate

    temp = temp * Clrate

print(cstate)