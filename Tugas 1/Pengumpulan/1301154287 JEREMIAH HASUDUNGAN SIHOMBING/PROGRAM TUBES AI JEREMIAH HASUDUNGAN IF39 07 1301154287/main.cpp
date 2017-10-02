#include <iostream>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <conio.h>
#include <time.h>

using namespace std;

///Variabel
double X1;
double X2;
double Y1;
double Y2;
double z;
double tmax;
double cDown;
double temp;
double alpha;
double State;
double newState;
double s;
double e;


///Fungsi dan Fungsi untuk membangkitkan nilai acak

Function_state (double X1, double X2){

    double f=((4-(2.1*X1*X1)+((X1*X1*X1*X1)/3))*(X1*X1))+(X1*X2)+((-4+(4*(X2*X2)))*(X2*X2));
    return f;
}
int main()

{
    srand(time(0));
    X1= (rand()/(double)RAND_MAX)*(10-(-10))-(-10);
    X2= (rand()/(double)RAND_MAX)*(10-(-10))-(-10);
    State   = Function_state(X1,X2);
    tmax    = 10000000;
    cDown   = 1;
    alpha   = 0.001;

    while (tmax > cDown)
    {
        Y1=(rand()/(double)RAND_MAX)*(10-(-10))-(-10);
        Y2=(rand()/(double)RAND_MAX)*(10-(-10))-(-10);
        newState = Function_state(Y1,Y2);
        temp = (-(State-newState))/tmax;
        e = 2.71828183;
        s = pow(e,temp);
        tmax = tmax*alpha;

        if(temp<0){
            X1=Y1;
            X2=Y2;
            State = newState;
        }
        else{
            X1=Y1;
            X2=Y2;
        }
    }

    cout<<" X1 = "<<X1<<endl;
    cout<<" X2 = "<<X2<<endl;
    cout<<" State = "<<State<<endl;

}
