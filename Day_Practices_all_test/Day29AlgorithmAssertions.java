import java.util.Arrays;

public class Day29AlgorithmAssertions {
    public static void main(String[] args) {
        check(Arrays.equals(
                        TwoSum.twoSum(new int[] { 3, 3 }, 6),
                        new int[] { 0, 1 }),
                "Two Sum must handle duplicate values.");
        check(Arrays.equals(
                        TwoSum.twoSum(new int[] { -3, 4, 3, 90 }, 0),
                        new int[] { 0, 2 }),
                "Two Sum must handle negative values.");
        expectIllegalArgument(
                () -> TwoSum.twoSum(new int[] { 1, 2 }, 8),
                "Two Sum must report when no answer exists.");

        check(
                toArray(AddTwoNumbers.addTwoNumbers(list(9, 9, 9), list(1)))
                        .equals(Arrays.asList(0, 0, 0, 1)),
                "Add Two Numbers must carry across every digit.");
        check(
                toArray(AddTwoNumbers.addTwoNumbers(list(0), list(0)))
                        .equals(Arrays.asList(0)),
                "Add Two Numbers must preserve zero.");

        check(
                LongestSubstringWithoutRepeatingCharacters.lengthOfLongestSubstring("") == 0,
                "Longest substring of an empty string must have length zero.");
        check(
                LongestSubstringWithoutRepeatingCharacters.lengthOfLongestSubstring("bbbbb") == 1,
                "Longest substring must handle repeated characters.");
        check(
                LongestSubstringWithoutRepeatingCharacters.lengthOfLongestSubstring("pwwkew") == 3,
                "Longest substring must move the window correctly.");

        check(
                MedianOfTwoSortedArrays.findMedianSortedArrays(new int[0], new int[] { 3 }) == 3.0,
                "Median must handle an empty first array.");
        check(
                MedianOfTwoSortedArrays.findMedianSortedArrays(
                        new int[] { 1, 2 }, new int[] { 3, 4 }) == 2.5,
                "Median must average the middle values for even input.");
        check(
                MedianOfTwoSortedArrays.findMedianSortedArrays(
                        new int[] { 1, 3 }, new int[] { 2 }) == 2.0,
                "Median must handle unequal array lengths.");
        expectIllegalArgument(
                () -> MedianOfTwoSortedArrays.findMedianSortedArrays(new int[0], new int[0]),
                "Median must reject two empty arrays.");

        check(
                LongestPalindromicSubstring.longestPalindrome("cbbd").equals("bb"),
                "Longest palindrome must handle even-length results.");
        check(
                LongestPalindromicSubstring.longestPalindrome("a").equals("a"),
                "Longest palindrome must handle a single character.");
        check(
                LongestPalindromicSubstring.longestPalindrome("").isEmpty(),
                "Longest palindrome of an empty string must be empty.");
        String tiedPalindrome = LongestPalindromicSubstring.longestPalindrome("babad");
        check(
                tiedPalindrome.equals("bab") || tiedPalindrome.equals("aba"),
                "Longest palindrome must return either longest result for a tie.");

        System.out.println("Day 29 edge-case checks passed.");
    }

    private static AddTwoNumbers.ListNode list(int... values) {
        AddTwoNumbers.ListNode dummy = new AddTwoNumbers.ListNode(0);
        AddTwoNumbers.ListNode current = dummy;
        for (int value : values) {
            current.next = new AddTwoNumbers.ListNode(value);
            current = current.next;
        }
        return dummy.next;
    }

    private static java.util.List<Integer> toArray(AddTwoNumbers.ListNode node) {
        java.util.List<Integer> values = new java.util.ArrayList<>();
        while (node != null) {
            values.add(node.val);
            node = node.next;
        }
        return values;
    }

    private static void expectIllegalArgument(Runnable action, String message) {
        try {
            action.run();
        } catch (IllegalArgumentException expected) {
            return;
        }
        throw new AssertionError(message);
    }

    private static void check(boolean condition, String message) {
        if (!condition) {
            throw new AssertionError(message);
        }
    }
}
