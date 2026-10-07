public class LoopIfTestB08 {
    public static void main (String [] args) {
        int count = 0;
        for ( int i = 1; i <= 200; i ++) {
            if (i % 11 == 0) {
                count++;
            }
        }
        System.out.println(count);
    }
}
