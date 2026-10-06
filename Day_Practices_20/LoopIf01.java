
/** 1 ээс 10 хүртэлх тэгш тоог гарсан анхааруулага өөрөө хийгээгүй тусламж авсан. */
public class LoopIf01 {
    public static void main(String[]args) {
        for ( int i = 2; i <= 10; i ++) 
        { 
            if (i % 2 == 0 )
            System.out.println(i);
        }
    }
}
