public class ArrayIf {
    public static void main (String[] args)
    {
        int[] days = {10, 20, 30};

        for (int i = 0; i < days.length; i++) {
            if (days[i] > 20) {
                System.out.println(days[i]);
            }
        }
    }
}