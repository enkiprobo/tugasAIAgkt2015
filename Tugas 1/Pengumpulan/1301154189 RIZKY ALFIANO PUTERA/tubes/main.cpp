#include <iostream>
#include<stdlib.h>
#include<stdio.h>
#include<ctime>
#include<math.h>

using namespace std;
double fungsi(double x1, double x2)
{
    double f;
    f = ((4-(2.1*(x1*x1))+((x1*x1*x1*x1)/3))*(x1*x1))+(x1*x2)+((-4+(4*(x2*x2)))*(x2*x2));
    return f;
}


int main(){

    double range;
    srand (time(0));
    range= (-10,10);

    double x1= (rand()/(double)RAND_MAX)* range;
    double x2= (rand()/(double)RAND_MAX)* range;
    double f= fungsi(x1,x2);

    double t= 1700;
    double c= 1;
    double a= 0.8999;

    while (t > c){
        double xx1 = (rand()/(double)RAND_MAX)*(10, -10);
        double xx2 = (rand()/(double)RAND_MAX)*(10, -10);
        double f1 = fungsi(xx1,xx2);
        double d = f1-f;
        double q = (-d/t);
        double e = 2.690;
        double p = pow(e,q);
        t=t*a;
        if (d<0)
        {
            x1=xx1;
            x2=xx2;
            f = f1;
        }
        else if (d>0) {
            x1=xx1;
            x2=xx2;
        }

    }
    cout<<"selamat datang" << endl;
    cout<<"Nilai X1: " <<x1 <<endl;
    cout<<"Nilai X2: " <<x2 <<endl;
    cout<<"hasil: " <<f <<endl;
    }


