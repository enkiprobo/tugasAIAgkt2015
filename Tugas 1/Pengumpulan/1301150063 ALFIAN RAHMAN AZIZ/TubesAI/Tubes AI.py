import random

#Fungsi Nilai X1 dan X2
def FungsiSA(x1, x2):
    func = (4 - (2.1*(x1**2))+((x1**4)/3))*(x1**2) + (x1*x2) + (-4+(4*(x2**2)))*(x2**2)
    return func


#Fungsi Random dari -10 sampai 10
def randomvar ():
    return random.uniform(-10,10)



TemAwal = 1000
TemAkhir = 0.0063
Nilaix1 = randomvar()
Nilaix2 = randomvar()
MinAwal = FungsiSA(Nilaix1, Nilaix2)


while TemAwal > TemAkhir:
    for i in range(100):
        barux1 = randomvar()
        barux2 = randomvar()
        new = FungsiSA(barux1, barux2)
        if ( MinAwal > new):
            MinAwal = new
        elif (2.71828183**((MinAwal - new)/TemAwal) > random.random()):
            MinAwal = new
    TemAwal =  0.99* TemAwal

print(MinAwal)


