import random

tAwal = 1500
al = 0.999
r = random.uniform(0, 1)
ulang = range(103)
x1 = random.uniform(-10, 10)
x2 = random.uniform(-10, 10)

def rumus(x1,x2) :
    fungsi = (4-2.1*(x1**2) + (x1**4)/3)*(x1**2) + (x1*x2) + (-4 +4 *(x2**2))*(x2**2)
    return fungsi

def eksponensial(stateBaru, minState, tAwal) :
    e = 2.71828183
    return e **(-(stateBaru-minState)/tAwal)

minState = rumus(x1, x2)

while (tAwal>0.0001) :
    x1 = random.uniform(-10, 10)
    x2 = random.uniform(-10, 10)
    stateBaru = rumus(x1,x2)
    for a in ulang:
        if (stateBaru<minState) :
            if (eksponensial(stateBaru, minState, tAwal) > r)  :
                minState = stateBaru
        else :
            minSate = stateBaru
    tAwal = tAwal*al

print(minState)