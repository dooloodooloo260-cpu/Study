public class CounterA01 {
    public static void main (String [] args) {
        int count = 0; 
        for (int i = 1; i <= 20; i ++) {
            if (i % 2 == 0) {
                count++;
            }
        }
        System.out.println("I counted " + count + "even numbers. ");
        System.out.println("би" + count + "ширхэг тэгш тоо тоолоо.");
    
    }
}