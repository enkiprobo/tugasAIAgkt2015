#include <iostream>
#include<stdlib.h>
#include<ctime>
#include<math.h>

using namespace std;
double x1,x2;
double a1,a2;
double tAwal, tAkhir;
double f,f1,b,d,q,e,p;
double rumus (double x1,double x2)
{
    double f;
    f=((4-(2.1*x1*x1)+((x1*x1*x1*x1)/3))*(x1*x1))+(x1*x2)+((-4+(4*(x2*x2)))*(x2*x2));
    return f;
}

int main()
{
    srand(time(0));
    x1 = (rand()/(double)RAND_MAX)*(10-(-10))+(-10);
    x2 = (rand()/(double)RAND_MAX)*(10-(-10))+(-10);

    f = rumus(x1,x2);
    tAwal= 18000; //temperatur
    b = 0.0000009; // ketika perulangan berhenti
    tAkhir = 0.8; // nilai random
    while (tAwal > b)
    {
        a1 = (rand()/(double)RAND_MAX)*(10-(-10))+(-10);
        a2 = (rand()/(double)RAND_MAX)*(10-(-10))+(-10);

        f1 = rumus (a1,a2);
        d = f1-f;
        q = (-d/tAwal);
        e = 2.71828; //eksponen
        p = pow(e,q); //kuadrat
        tAwal=tAwal*tAkhir;
        if (d<0)
        {
            x1=a1;
            x2=a2;
            f = f1;
        }
        else if (d>0) {
            x1=a1;
            x2=a2;
        }
    }
    cout<<"Hasil : " << f << endl;
}
