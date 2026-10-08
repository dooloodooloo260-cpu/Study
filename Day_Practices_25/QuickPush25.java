

public class QuickPush25 {
    public static void main(String[] args) { 
        int[] scores = { 85, 92, 78, 90, 88};
        int sum =0;
        for (int i =0 ; i < scores.length; i++) {
            sum += scores[i];
        }
        System.out.println("Day25 Sum: " + sum);
    }
}
