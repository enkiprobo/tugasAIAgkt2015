package tubes_ai;

import java.util.Random;

public class Tubes_AI {
    
    static double temp,alpha,x1,x2,state_awal,state_akhir,bsf,eksponen,probabilitas,deltaE,AkuMod,fr;
    
    public static double fungsi(double x1, double x2){
        double f;
        f = (4 - 2.1*(Math.pow(x1,2)) + (Math.pow(x1,4)/3)) * (Math.pow(x1,2)) + x1*x2 + (-4+4*(Math.pow(x2,2)))*(Math.pow(x2,2));
        return f;
    }
    
    public static double BilRand(){
        Random random = new Random();
        double angka = random.nextInt(20) + (-10) - random.nextDouble();
        return angka;
    }
    
    public static void main(String[] args) {
     
        x1 = 0;
        x2 = 0;
        fr = 1.5;
        temp = 10000;
        alpha = 0.99;
        eksponen = 2.71828183;
        state_akhir = fungsi(x1,x2);
        bsf = state_akhir;
                
        while(temp > 0.53145){
            for (int i = 0; i < 100; i++) {
                x1 = BilRand(); // Nilai dari x1 nya dirandom antara -10 sampai 10
                x2 = BilRand(); // Nilai dari x2 nya dirandom antara -10 sampai 10
                state_awal = fungsi(x1,x2); // state awalnya dimasukkan ke fungsi dari x1 dan x2 yang sudah dirandom
                if(state_awal < state_akhir){
                    state_akhir = state_awal;
                    bsf = state_awal;
                }else if(state_akhir < state_awal){
                    deltaE = -(state_awal - state_akhir)/temp;
                    probabilitas = Math.pow(eksponen,deltaE);
                    if(probabilitas > Math.random()){
                        state_akhir = state_awal;
                    }
                } 
            }
            temp = temp * alpha;
        }        
            AkuMod = (1 - ((bsf - fr)/fr))*100; 
            
            System.out.println("=== Hasil Simulated Annealing ===");
            System.out.println();
            System.out.println("Nilai x1 = " + x1);
            System.out.println("Nilai x2 = " + x2);
            System.out.println("Fx(x1,x2) = " + bsf);
            System.out.println();
            System.out.println("Akurasi Model = " + AkuMod + "%");
    }
}