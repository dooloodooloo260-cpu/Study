public class Day27Dr01 {
    public static void main(String[] args) {
        int total = 0; 
        int [] clicks = { 5, 3, 7, 2} ;

        for ( int i = 0; i < clicks.length; i++) {
            total += clicks[i]; 
        }

        System.out.println("I built a counter app.");
        System.out.println("The total is :" + total);
    }}