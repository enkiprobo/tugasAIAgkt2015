import random

a,b= random.uniform(-10,10),random.uniform(-10,10) #inisialisasi x2
def fungsitubes(a,b):
    l = (((4-(2.1*(a**2)))+((a**4)/3))*(a**2)) +  (a*b) +  ((-4 + (4*(b**2)))*(b**2))
    return l
def probability(minimum,new,suhuawal):
    p=2.7182818284**(-1*(new-minimum)/suhuawal)
    return p
minimumstate=fungsitubes(a,b)
tmp = 9999999
min = 0.0001
cool = 0.9
while tmp>min :
    a,b=random.uniform(-10,10), random.uniform(-10,10)
    newstate=fungsitubes(a,b)
    if (minimumstate>newstate):
        minimumstate=newstate
    else :
        z=(newstate-minimumstate)/tmp
        if (probability(minimumstate,newstate,tmp)>random.random()):
            minimumstate=newstate
    tmp = tmp*cool
print(minimumstate)
print(fungsitubes(1,0))

#print(a)