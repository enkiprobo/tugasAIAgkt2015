'''
    PROGRAM    : simple implementation of simulated annealing
    CREATED BY : Enki Probo Sidhi
'''
import random, math

def function(x1, x2): # the mathematical function to be solved
    x1, x2 = float(x1), float(x2)
    
    return (4-2.1*x1**2+x1**4/3)*x1**2+x1*x2+(-4+4*x2**2)*x2**2

def prob(new_state, current_state, t): # for calculating probability
    current_state, new_state = float(current_state), float(new_state)
    
    return math.exp(-(new_state-current_state)/t)

def main(numberoflooping): # main program
    for i in range(numberoflooping):
        t = 1000 
        tcool = 0.0001
        alpha = 0.99

        x1best, x2best = random.uniform(-10, 10), random.uniform(-10, 10)
        bsf = current_state = function(x1best, x2best) # double assignment

        while t > tcool:
            for j in range(100):
                x1, x2 = random.uniform(-10, 10), random.uniform(-10, 10)
                new_state = function(x1, x2)
                if new_state < current_state:
                    x1best, x2best = x1, x2
                    bsf = current_state = new_state # double assignment
                elif prob(new_state, current_state, t) > random.random():
                    current_state = new_state
            t = t * alpha

        print i+1,". minimum value of the function is",bsf
        print "with x1:",x1best,"and x2:",x2best

main(1) # run the program 1 times