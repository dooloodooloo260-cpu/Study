import javax.swing.*;
import java.awt.FlowLayout;

public class CounterApp {
    public static void main (String [] args) {
        JFrame frame = new JFrame ("Миний тоолуур"); 
        frame.setSize(350, 180);

        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setLayout(new FlowLayout());

        JLabel asklabel = new JLabel("Тоо бич :");
        JTextField inputField = new JTextField(8);
        // 8 үсгийн өргөнтэй талбар

        JButton addBtn = new JButton("+ Нэм");
        JButton subBtn = new JButton("- Хас");
        JLabel resultLabel = new JLabel("Үр дүн: 0");

        // Нэмэх товч 
        addBtn.addActionListener(e -> {
            int num =
            Integer.parseInt(inputField.getText()); 

        // Текст -> Тоо 
        int current = 

        Integer.parseInt(resultLabel.getText().replace("Үр дүн: ",""));

        int sum = current + num;
        resultLabel.setText("Үр дүн: " + sum);
        });

        // Хасах товч 
        subBtn.addActionListener(e -> {
            int num =
            Integer.parseInt(inputField.getText());
            int current = 
            Integer.parseInt(resultLabel.getText().replace("Үр дүн: ",""));

            int diff = current - num ;
            resultLabel.setText("Үр дүн: + diff");
        });

        frame.add(asklabel);
        frame.add(inputField);
        frame.add(addBtn);
        frame.add(subBtn);
        frame.add(resultLabel);
        frame.setVisible(true);
    }
}