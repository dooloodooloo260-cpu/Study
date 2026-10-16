public class LongestPalindromicSubstring {
    public static String longestPalindrome(String text) {
        if (text.isEmpty()) {
            return "";
        }

        int start = 0;
        int end = 0;
        for (int center = 0; center < text.length(); center++) {
            int oddLength = expandFromCenter(text, center, center);
            int evenLength = expandFromCenter(text, center, center + 1);
            int length = Math.max(oddLength, evenLength);

            if (length > end - start + 1) {
                start = center - (length - 1) / 2;
                end = center + length / 2;
            }
        }

        return text.substring(start, end + 1);
    }

    private static int expandFromCenter(String text, int left, int right) {
        while (left >= 0 && right < text.length()
                && text.charAt(left) == text.charAt(right)) {
            left--;
            right++;
        }
        return right - left - 1;
    }

    public static void main(String[] args) {
        System.out.println(longestPalindrome("babad"));
    }
}
