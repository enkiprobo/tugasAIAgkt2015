function TugasAI_SimulatedAnnaeling
x1 = 2;
x2 = 1;
minstate=(4-2.1* x1^2 + x1^4/3)* x1^2+x1*x2+(-4+4*x2^2)*x2^2;
%randi([-10 10],1,1)
%nilaiminstate = (minstate)
temp1 = 100;
temp2 = 10;
alpha = 0.8;


while temp1 > temp2
    newx1 = x1;
    %x1 yang baru di random
    newx1 = (10-(-10).*rand(1,1)) +-10;
    newx2 = x2;
    %x2 yang baru dirandom
    newx2 = (10-(-10).*rand(1,1)) +-10;
    newstate = (4-2.1* x1^2 + x1^4/3)* x1^2+x1*x2+(-4+4*x2^2)*x2^2;
    delta = newstate - minstate;
    
    if delta < 0
        minstate = newstate;
        x1=newx1;
        x2=newx2;
    else
        %rumus prob = exp(-delta/temp)
        prob=exp(-delta/temp1);
        r=rand();
        if r<prob
            minstate=newstate;
            x1=newx1;
            x2=newx2;
        end
    end
    %rumus T = alpha * T
    %alpha = 0.8
    temp1=temp1*alpha;
end

% akurasi = (1-(f(x1)-

%disp('x1= %f\n',x1);
fprintf('x1 = %f\n',x1);
fprintf('x2 = %f\n',x2);
fprintf('f(x1,x2) = %f\n',minstate);
        

% temp = alpha*temp
% end