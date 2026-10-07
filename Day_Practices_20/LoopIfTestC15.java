/** 10 - 99-ийн тэгш тоонуудын нийлбэр "дундаж биш, нийлбэр" */
public class LoopIfTestC15 {
    public static void main ( String [] args ) {
        int sum = 0; 
        for ( int i = 10; i <= 99; i++) {
            if(i % 2 == 0){
                sum +=i;
            }
        }
        System.out.println(sum);
      }
}