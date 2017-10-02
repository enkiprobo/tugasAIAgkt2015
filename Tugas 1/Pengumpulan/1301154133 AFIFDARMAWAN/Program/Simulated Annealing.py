import random
import math

x1 = random.uniform(-10,10)
x2 = random.uniform(-10,10)
def bilangan (x1,x2):
    bil = ((4-(2.1*x1**2)+((x1**4)/3))*(x1**2)+(x1*x2)+(-4+(4*(x2**2))*x2**2))
    return bil
temp = 7777
a = 0.9
min = 0.007
bilangan(x1,x2)

while (temp > min):
        x1 = random.uniform(-10,10)
        x2 = random.uniform(-10,10)
        bilangan2 = ((4-(2.1*x1**2)+((x1**4)/3))*(x1**2)+(x1*x2)+(-4+(4*(x2**2))*x2**2))
        r=random.uniform(0,1)
        if (bilangan > bilangan2):
            bilangan = bilangan2
        else :
            if((math.exp((bilangan-bilangan2)/temp))> r ):
                bilangan = bilangan2
        temp = temp * a

print " nilai minimalnya adalah " ,bilangan