/** 1 - 30-ийн хооронд 3- аар хуваагддаг тоонуудыг нийлбэр */
public class LoopIfTestC13 {
    public static void main (String []args ) {
        int sum = 0; 
        for ( int i = 1; i <= 30 ; i ++) {
            if(i % 3 == 0){
                sum += i;
            }

        }
        System.out.println("Sum: " + sum);
    }
}