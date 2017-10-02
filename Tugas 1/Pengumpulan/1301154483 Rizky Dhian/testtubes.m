function testtubes
x1 = 8 ;
x2 = -2 ;
currentstate = (4-2.1* x1^2 + x1^4/3)* x1^2+x1*x2+(-4+4*x2^2)* x2^2;
T1 = 10000;
T2 = 1;
A = 0.99;

while T1>T2
   x1baru =(10-(-10)).*rand(1,1) + -10;
   x2baru =(10-(-10)).*rand(1,1) + -10;
   newstate = (4-2.1* x1baru^2 + x1baru^4/3)* x1baru^2+x1baru*x2baru+(-4+4*x2baru^2)* x2baru^2;
   DeltaE = newstate-currentstate;
   if DeltaE < 0
       currentstate=newstate ;
       x1=x1baru;
       x2=x2baru;
   else
       prob=exp(-DeltaE/T1);
       R=rand();
       if R<prob
           currentstate=newstate ;
           x1=x1baru;
           x2=x2baru;
       end
           
   end
   T1=T1*A;
   
end
fprintf('x1 : %f\n',x1);
fprintf('x2 : %f\n',x2);
fprintf('hasil : %f\n',currentstate);