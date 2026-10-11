public class Day27Dr04 {
    public static void main ( String [] args) {
        int total = 0;
        int count = 0;
        int [] clicks = { 10, 20, 5};

         for (int i = 0; i < clicks.length; i ++) {
            total -= clicks[i];
            if (clicks[i] > 10) {
                count++;
            }
        }

        System.out.println(count + " clicks were bigger than ten. " + total );
        

    }
}
