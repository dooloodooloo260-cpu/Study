import java.util.HashMap;
import java.util.Map;

public class LongestSubstringWithoutRepeatingCharacters {
    public static int lengthOfLongestSubstring(String text) {
        Map<Character, Integer> lastSeen = new HashMap<>();
        int windowStart = 0;
        int longest = 0;

        for (int windowEnd = 0; windowEnd < text.length(); windowEnd++) {
            char current = text.charAt(windowEnd);
            Integer previousIndex = lastSeen.get(current);
            if (previousIndex != null && previousIndex >= windowStart) {
                windowStart = previousIndex + 1;
            }

            lastSeen.put(current, windowEnd);
            longest = Math.max(longest, windowEnd - windowStart + 1);
        }

        return longest;
    }

    public static void main(String[] args) {
        System.out.println(lengthOfLongestSubstring("abcabcbb"));
    }
}
