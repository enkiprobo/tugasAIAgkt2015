import random
import math

x1 = random.uniform(-10,10) #fungsi random untuk men-generate x1 antara -10 sampai 10
x2 = random.uniform(-10,10) #fungsi random untuk men-generate x2 antara -10 sampai 10

def Fungsi(x1,x2):
    isiF = (4-2.1*x1**2+x1**4./3)*x1**2+x1*x2+(-4+4*x2**2)*x2**2
    return isiF

tempAwal = 1000
alfa = 0.99 #dimana nilainya antara 0.8 - 0.99
tempAkhir = 0.01 #temp akhir akan berhenti pada 0,01 dan akan menghasilkan nilai minimum
Fungsi1 = Fungsi(x1,x2) #current state

while (tempAwal > tempAkhir):
    for i in range(50) : #dilakukan looping tambahan agar x1 dan x2 lebih sering digenerate
         x1 = random.uniform(-10,10)
         x2 = random.uniform(-10,10)
         Fungsi2 = Fungsi(x1,x2)
         r = random.uniform(0,1) #new state

    if(Fungsi1 > Fungsi2):
        Fungsi1 = Fungsi2
    else:
        if((math.exp((Fungsi1-Fungsi2)/tempAwal)) > r): #cek probabilitas dimana currentState - newState
            Fungsi1 = Fungsi2
        tempAwal = tempAwal * alfa

print "Hasil minimum dari fungsi adalah: ",Fungsi1