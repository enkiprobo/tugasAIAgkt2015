#include <iostream>
#include <time.h>
#include <stdlib.h>
#include <math.h>

using namespace std;

double fungsi(float x1, float x2)
{
    return (4-2.1*x1*x1+((x1*x1*x1*x1)/3)*x1*x1)+(x1*x2)+(-4+(4*(x2*x2))*x2*x2);
}

double fRand(double fMin, double fMax)
{

    double f = (rand()/(double)RAND_MAX)*(fMax-fMin)+fMin;
    return f;
}


int main()
{
 srand(time(0));

 int Tawal;
 int Takhir;
 double bof;
 double newstate;
 double alpha;

 Tawal = 500;
 Takhir = 0.5;
 alpha = 0.99;
 double x1= fRand(-10,10);
 double x2= fRand(-10,10);
 bof= fungsi(x1,x2);
 while (Tawal > Takhir){
        for (int i=0; i<100; i++) {
            x1= fRand(-10,10);
            x2= fRand(-10,10);
            newstate= fungsi(x1,x2);
            if (bof > newstate){
                bof = newstate;
            }
            else{
                double e= 2.71828;
                double deltae=- (newstate-bof)/Tawal;
                double rumusdeltae = pow(e, deltae);
                if(rumusdeltae > fRand(0,1)){
                    bof = newstate;
                }
            }
        }
        Tawal = alpha*Tawal;
 }
 cout<<bof<<endl;
}
