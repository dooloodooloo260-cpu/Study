public class Day27Dr05 {
    public static void main (String[] args) {
        int total = 0; 
        int count = 0;
        int [] numbers = { 10,20,5};

        for (int i = 0; i < numbers.length; i++) {
            total += numbers[i];
            count++;
        }
        System.out.println(" I added " + count + " numbers. Sum: " + total + "."); 
            
        }
    } 
