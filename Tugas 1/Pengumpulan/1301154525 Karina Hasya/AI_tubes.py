import random 

def karin(x1,x2):
	return ((4-(2.1*(x1**2))+((x1**4)/3))*(x1**2))+(x1*x2)+((-4+4*(x2**2))*(x2**2))

def cek():
	return random.uniform(-10,10)

x1,x2 = cek(), cek()
x = karin(x1,x2)
T1 = 200000
T2 = 1
alfa = 0.992
while (T1 > T2) :
	for i in range (0,100):
		y1,y2 = cek(),cek()
		y=karin(y1,y2)

		if (y<x): 
			x = y 
			x1 = y1 
			x2 = y2 
		else:
			probabilty = 2.718281824**((-(y-x))/T1)
			if (probabilty > random.random()):
					x = y 
					x1 = y1 
					x2 = y2
	T1 = T1*alfa
print (x) 