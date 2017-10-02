#include <stdio.h>
#include <stdlib.h>

double formula(double x1, double x2){
    double x;
    x = ((4-(2.1*x1*x1))+(pow(x1,4)/3))*(x1*x1)+(x1*x2)+(-4+(4*pow(x2,2)))*pow(x2,2);
    return x;
}

int main(){

    ("cls");
    printf("TUGAS BESAR ARTIFICIAL INTELLIGENCE\n");
    printf("-------------1301154147------------\n");
    printf(" \n");

    srand(time(NULL));//merupakan fungsi yang menentukan seed atau posisi awal dalam sebuah pengacakan ( random )
    int awal = 200;
    int akhir = 1;

    double x1 = (rand()/(double)RAND_MAX)*(10-(-10)+(-10));
    double x2 = (rand()/(double)RAND_MAX)*(10-(-10)+(-10));
    double bestState = formula(x1,x2);

    double batas = (10-(-10)+(-10));

    while (awal>akhir){
        double y1 = (rand()/(double)RAND_MAX)*batas;
        double y2 = (rand()/(double)RAND_MAX)*batas;
        double newState = formula(y1, y2);

        if (newState < bestState){
            bestState = newState;
        }
        else{
            double a = (rand()/(double)RAND_MAX)*(1);
            double b = 2.717;
            double temp1 = b;
            double c = newState - bestState;
            double temp2 = c;
            double p = pow(temp1,temp2);

            if (p>a){
                y1 = x1;
                y2 = x2;
            }
        }
        awal = awal * 0.9998;
    }

    printf("x1    : %e\n",x1);
    printf("x2    : %e\n",x2);
    printf("Hasil : %f\n",bestState);
    printf(" \n");
    printf("-----------------------------------");
    return 0;
}
