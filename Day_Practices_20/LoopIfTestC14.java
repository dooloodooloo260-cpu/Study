/** 1 - 1000-ийн 7-оор хуваагддаг тоонуудын нийлбэр */
public class LoopIfTestC14 {
    public static void main (String [] args) {
        int sum = 0 ; 
        for (int i = 1; i <=1000; i ++) {
            if (i % 7 == 0) {
                sum += i;
            }

        }
        System.out.println(sum);
    }
}