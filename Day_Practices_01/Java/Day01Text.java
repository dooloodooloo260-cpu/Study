
package Day_Practices_01.Java;

import java.util.HashMap;

class Day01Text {

    public static void main (String[] args ) {
    }

    static int[] twoSum(final int[] nums, final int target) {
        final HashMap<Integer, Integer> prevMap = new HashMap<>();

        for(int i = 0; i < nums.length; i++) {
            final int num = nums[i];
            final int diff = target - num;

            if (prevMap.containsKey(diff)) {
                return new int[] { prevMap.get(diff), i };
            }
            prevMap.put(num, i);
        }
        return new int[] {};
    }
}
