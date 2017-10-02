import random

x1 = random.uniform(-10, 10);
x2 = random.uniform(-10, 10);
newx1=x1;
newx2=x2;
currentstate = ((4-(2.1*(x1**2))+((x1**4)/3))*(x1**2))+(x1*x2)+((-4+(4*(x2**2)))*(x2**2));
temperatures = 1000000;
temperatures_min = 0.000001;
alphas = random.uniform(0.8,0.999999);
counter = 1;

print "~~~Hasil Pencarian Nilai Optimal Minimum dengan Simulated Annealing~~~";
print "Tentukan Nilai Optimal Minimum dari Fungsi :";
print " f( x1, x2)= [4 - 2.1x1^2 + x1^4/3] x1^2 + x1x2 + (-4 + 4x2^2)x2^2  ";
print "";
print "";

while (temperatures > temperatures_min or bestsofarstate>0):
        newx1 = random.uniform(-10, 10);
        newx2 = random.uniform(-10, 10);
        newstate = ((4 - (2.1 * (newx1 ** 2)) + ((newx1 ** 4) / 3)) * (newx1 ** 2)) + (newx1 * newx2) + ((-4 + (4 * (newx2 ** 2))) * (newx2 ** 2));
        testing = newstate - currentstate;

        if testing < 0:
            bestsofarx1 = newx1;
            bestsofarx2 = newx2;
            currentstate = newstate;
            bestsofarstate = newstate;
        else :
            probstat = 2.71828 ** -((newstate - currentstate) / temperatures);
            if probstat > random.random():
                bestsofarx1 = newx1;
                bestsofarx2 = newx2;
                currentstate = newstate;
                bestsofarstate = newstate;
        '''
        print "Hasil Iterasi ke - ",counter;
        print "X1 : ", newx1;
        print "X2 : ", newx2;
        print "Hasil Sementara : ", newstate;
        print " "
        '''
        counter = counter + 1;
        temperatures = temperatures * alphas;

print "Hasil Optimal Minimum"
print ""
print "X1 : ", bestsofarx1;
print "X2 : ", bestsofarx2;
print "Hasil : ", bestsofarstate;
