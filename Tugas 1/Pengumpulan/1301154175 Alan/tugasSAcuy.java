/**
 *
 * @author AlanMaulana(1301154175)
 * if 39 07
 */
import java.text.DecimalFormat;
import java.util.Random;
public class tugasSAcuy{

    /**
     * @param args the command line arguments
     */
     public static void main(String[] args) {
        double FgsiAwal=0,FgsiBaru=0;
        double coolingRate = 0.9999;
        double tmp = 9999;
        FgsiAwal=fungsi();
        do {
            FgsiBaru=fungsi();
            if(FgsiBaru<FgsiAwal){
                FgsiAwal=FgsiBaru;
            }else
            {
                if (Math.exp(-1*((FgsiBaru-FgsiAwal)/tmp))> Math.random()*1+0){
                    FgsiAwal=FgsiBaru;
                }
            }
            tmp*=coolingRate;
        }
        while (tmp>1);
        System.out.println("hasilJawaban: "+FgsiAwal);
    }

    public static double fungsi(){
        double x1=Math.random()* 10+(-10);
        double x2=Math.random()* 10+(-10);
        return ((4-(2.1*(x1*x1))+((x1*x1*x1*x1)/3))*(x1*x1))+(x1*x2)+((-4+(4*(x2*x2)))*(x2*x2));
    }

}
