import java.sql.*;

public class DbQuiz {
    public static void main(String[] args) {
        String url = "jdbc:postgresql://localhost:5432/gantulkhuurariunbileg";
        String user = "gantulkhuurariunbileg";
        String password = "";   // Postgres.app бол хоосон үлдээж болно

        try {
            Connection conn = DriverManager.getConnection(url, user, password);
            Statement stmt = conn.createStatement();
            ResultSet rs = stmt.executeQuery(
                "SELECT id, question, answer FROM quiz_app.questions ORDER BY id");

            while (rs.next()) {
                int id = rs.getInt("id");
                String q = rs.getString("question");
                System.out.println(id + ". " + q);
            }

            conn.close();
            System.out.println("=== Connected to PostgreSQL! ===");
        } catch (SQLException e) {
            System.out.println("Connection failed!");
            e.printStackTrace();
        }
    }
}