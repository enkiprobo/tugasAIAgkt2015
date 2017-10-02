import random
x1 = random.randint(-10,10)
x2 = random.randint(-10,10)
n1, n2 = x1, x2
cs = float
bsf = float
fns = 0
initial_state = ((4-2.1*x1**2+(x1**4)/3)*x1**2+x1*n2+(-4+4*x2**2)*x2**2)
cs = initial_state
bsf = cs

print("Mencari nilai Minimum dari:")
print("f(x1,x2)=(4-2.1*x1^2+(x1^4)/3)*x1^2+x1*n2+(-4+4*x2^2)*x2^2")
print("Dengan -10<=x1<=10 dan -10<=x2<=10")
print("Tekan enter untuk memulai")
input()

while cs != fns:
    n1 = random.randint(-10,10)
    n2 = random.randint(-10,10)
    ns = ((4-2.1*n1**2+(n1**4)/3)*n1**2+n1*n2+(-4+4*n2**2)*n2**2)
    delta_state = ns-cs
    if delta_state < 0:
        x1=n1
        x2=n2
        if ns<bsf:
            bsf=ns
            a1=x1
            a2=x2
            print("Best so far : ",bsf)
            print("Dengan x1 : ",a1,"dan x2 : ",a2)
            print()
            cs=bsf

    else:
        n1 = random.randint(-10,10)
        n2 = random.randint(-10,10)
print("-------------------------------")
print("Nilai minimum adalah : ", bsf)
print("Dengan x1 : ",a1,"dan x2 : ",a2)
input()




















