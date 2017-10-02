import random

x1= random.uniform(-10,10)
x2= random.uniform(-10,10)
bestsofar = ((4-(2.1*(x1**2))+((x1**4)/3))*(x1**2)+(x1*x2)+(-4-(4*(x2**2)))*(x2**2))

z= bestsofar
T= 1050
Tmin = 1
exp= 2.71828

while (T > Tmin):
      a= random.uniform(-10,10)
      b= random.uniform(-10,10)
      fbaru= ((4-(2.1*(a**2))+((a**4)/3))*(a**2)+(a*b)+(-4+(4*(b**2)))*(b**2))
      if(fbaru < z):
         x1=a
         x2=b
         z=fbaru
      else:
           AE= (fbaru-z)
           if((exp)**(-AE/T) > random.uniform(0,1)):
              x1=a
              x2=b
           T= T*0.999
           
      print(z)
print (z)
