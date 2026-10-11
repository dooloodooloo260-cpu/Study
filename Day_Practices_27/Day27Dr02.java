public class Day27Dr02 {
    public static void main (String[] args) {
        int total = 0; 
        int [] clicks = {10,20,5} ;

        for (int i = 0; i < clicks.length; i++) 
        {
            total += clicks[i];
        }

        System.out.println("Sum of clicks: " + total);

        System.out.println(" I  counted " + clicks.length + " clicks.");
        
    }
}