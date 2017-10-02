#include <iostream>
#include <stdlib.h>
#include <stdio.h>
#include <cstdlib>
#include <ctime>
#include <math.h>
#include<conio.h>

using namespace std;

double Rumus(double x1, double x2){
   return (4-2.1*x1*x1+x1*x1*x1*x1/3)*x1*x1+x1*x2+(-4+4*x2*x2)*(x2*x2);
}

double probabi(double minState,double newState,int n){   //probabilitas
    return pow(2.71828183,(-(minState-newState)/n));
}

double Random (double x, double y){
  for(double x=(10);x<(-10);x++);
    cout<<1+(rand()%6);

}

int main(){
    double b; //minSTate nilai baru
    double a; // newState
    double x = -10;
    double y= 10;
    double n = 10;
    double nakhir = 0.00003;
    double alpha = 0.00005;
    double x1;
    double x2;
    x1 = Random(x,y);
    x2 = Random(x,y);
    double baru = Rumus(x,y);   //temperature

    while (n > nakhir)
    {
        for (int i = 0 ; i<1; i++)
        {
            x1 = Random(x,y);
            x2 = Random(x,y);
            a = Rumus(x1,x2); //hasil perhitungan fungsi awal
        }

        double a = Rumus(x1,x2);
        if (baru < a)
        {
            baru = a ;
        }
        else
        {
            if( probabi(a,b,n)> Random(2,4))
            {
                baru = a;
            }
        }
        n = n * alpha;
    }
        cout<<b<<endl;
}





