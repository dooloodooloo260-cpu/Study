

public class IfApp {
    public static void main(String[]args) {
        int days = 0;
        int goal = 90; 
        int half = goal /2 ;

        if (days == 0) {
            System.out.println("Start today!");
        } else if (days >= goal) {
            System.out.println("GOAL REACHED!");
        } else if (days >= half ) {
            System.out.println("Half way there!");
        } else {
            System.out.println("Keep going" + (goal - days) + "days left");
        }

    }
}
