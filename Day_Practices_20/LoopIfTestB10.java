/**
  10. 1- 100-д сүүлийн цифр нь 5 байх тоо хэд байгаа вэ?
 */
public class LoopIfTestB10 {

    public static void main (String [] args) {
        int count = 0 ;
        for (int i = 1; i <= 100; i ++) {
            if (i % 10 == 5) {
                count++;
            }
        }
        System.out.println(count);
    }
}