import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class TwoSum {
    public static int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> indices = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            if (indices.containsKey(complement)) {
                return new int[] { indices.get(complement), i };
            }
            indices.put(nums[i], i);
        }

        throw new IllegalArgumentException("No two numbers add up to the target.");
    }

    public static void main(String[] args) {
        int[] result = twoSum(new int[] { 2, 7, 11, 15 }, 9);
        System.out.println(Arrays.toString(result));
    }
}
