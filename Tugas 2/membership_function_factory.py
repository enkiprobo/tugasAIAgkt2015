import math

def linear_up(x,a,b):
    if x <= a:
        return 0.
    elif x <= b:
        return (x-a)/(b-a)

def linear_down(x,a,b):
    if x >= b:
        return 0.
    elif x >= a: 
        return (b-x)/(b-a)

def sigmoid_up(x,a,b,c):
    if x <= a:
        return 0.
    elif x <= b:
        return 2*((x-a)/(c-a))**2
    elif x < c:
        return 1-2*((c-x)/(c-a))**2
    else:
        return 1.

def sigmoid_down(x,a,b,c):
    if x <= a:
        return 1.
    elif x <= b:
        return 1-2*((x-a)/(c-a))**2
    elif x < c:
        return 2*((c-x)/(c-a))**2
    else:
        return 0.

def triangle(x,a,b,c):
    if x <= a or x >= c:
        return 0.
    elif x <= b:
        return (x-a)/(b-a)
    else:
        return -(x-c)/(c-b)

def trapesium(x,a,b,c,d):
    if x <= a:
        return 0.
    elif x < b:
        return (x-a)/(b-a)
    elif x <= c:
        return 1.
    elif x >= d:
        return 0.
    else:
        return -(x-d)/(d-c)

def phi(x,c,b):
    if x <= c:
        return sigmoid_up(x, c-b, c-b/2, c)
    else:
        return 1 - sigmoid_up(x, c, c+b/2, c+b)

def beta(x,c,b):
    return 1/(1+((x-c)/b)**2)

def gauss(x,c,b):
    return math.exp(-b*(c-x)**2)

def membership_function(function, x, param):
    x = float(x)
    a = float(param['a'])
    b = float(param['b'])
    c = float(param['c'])
    d = float(param['d'])

    if d != -1:
        return function(x,a,b,c,d)
    elif a == -1 and c != -1:
        return function(x,c,b)
    elif c != -1:
        return function(x,a,b,c)
    else:
        return function(x,a,b)