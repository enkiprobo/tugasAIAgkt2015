import random

#deklarasi nilai random
x1 = random.uniform(-10,10)
x2 = random.uniform(-10,10)

#deklarasi function

def simulated(x1,x2):
    return(4-2.1*(x1**2) + ( x1**4)/3)*(x1**2) + (x1*x2) + (-4 + 4*(x2**2))*(x2**2)


def probalitas(Nilai1,Nilai2,min):
    return 2.71828183**(-(Nilai2-Nilai1))/min


L = 1000000
min = 1
alpha = 0.99
Nilai1 = simulated(x1,x2)
fr = 1.5

while (L>min):
    y1 = random.uniform(-10,10)
    y2 = random.uniform(-10,10)
    Nilai2 = simulated(y1,y2)
    if (Nilai1>Nilai2):
        x1=y1;
        x2=y2;
        Nilai1 = Nilai2
    elif (probalitas(Nilai1,Nilai2,L)>random.random()):
            x1=y1
            x2=y2
    L *= alpha
    mod = (1-((Nilai1-fr)/fr))*100

print ("x1 :",Nilai1,"")
print ("x2 :",Nilai1,"")
print ("f(x1,x2) :" ,x1,"")

print ("Akurasi Model : ",mod,"%") 


