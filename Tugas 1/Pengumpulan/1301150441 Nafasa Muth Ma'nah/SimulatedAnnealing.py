import random

def HeuristicFunction(x1,x2):
	left = (4-(2.1*(x1**2))+((x1**4)/3))*(x1**2)+(x1*x2)+(-4+(4*(x2**2)))*(x2**2)
	return left

def Random():
	return random.uniform(-10,10)
def probability(min,new,awal):
	pangkat = -1*(new-min)/awal
	Probabilitas = 2.7182818284**(pangkat)
	return Probabilitas

Tawal = 100000
Takhir = 0.00001
x1 = Random()
x2 = Random()
minstate = HeuristicFunction(x1,x2)
while (Tawal>Takhir):
	for i in range(1,180):
		nx1 = Random()
		nx2 = Random()
		newstate = HeuristicFunction(nx1,nx2)
		if (minstate>newstate):
			minstate=newstate
			nx1 = x1
			nx2 = x2
		else:
			if (probability(minstate,newstate,Tawal)>random.random()):
				nx1 = x1
				nx2 = x2
				minstate = newstate
	Tawal = Tawal*0.999
for i in range(0,5):
	print(minstate)