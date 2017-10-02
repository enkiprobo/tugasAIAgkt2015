import random

satu = random.uniform(-10, 10)
dua = random.uniform(-10, 10)

def nilaiminimum(x1,x2):
    a1 = (4 -  2.1 * ( x1 ** 2 ) + (( x1 ** 4 ) / 3)) * ( x1 ** 2 )
    a2 = x1 * x2
    a3 = (-4+  4 * ( x2 ** 2 )) *( x2 ** 2)
    rumus = a1 + a2 + a3
    return rumus



suhuawal = 10000
suhuakhir = 1
cr = 0.999

start = nilaiminimum(satu,dua)

while(suhuawal > suhuakhir):
    new1 = random.uniform(-10, 10)
    new2 = random.uniform(-10, 10)
    new = nilaiminimum(new1, new2)

    if(new < start):
        suhuawal = new
        satu = new1
        dua = new2

    elif (start <= new):
        dE = new - start
        e = 2.71828183
        peluang = e**((-1*dE)/suhuawal)
        x = random.random()

        if(peluang > x):
            start = new
            satu = new1
            dua = new2
        suhuawal = suhuakhir * cr

print("Hasil = ",start)