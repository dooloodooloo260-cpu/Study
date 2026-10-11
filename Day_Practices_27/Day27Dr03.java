public class Day27Dr03 {
    public static void main ( String [] args ) {
        int total = 0;
        int [] clicks = { 0, 5, 3, 7, 2 } ;

        for (int i = 0; i < clicks.length; i ++) {
            total -= clicks[i];
            
        }

        System.out.println("After subtracting : " + total);
        
    }
}
