public class MedianOfTwoSortedArrays {
    public static double findMedianSortedArrays(int[] first, int[] second) {
        if (first.length > second.length) {
            return findMedianSortedArrays(second, first);
        }
        if (first.length + second.length == 0) {
            throw new IllegalArgumentException("At least one array must contain a value.");
        }

        int leftSize = (first.length + second.length + 1) / 2;
        int low = 0;
        int high = first.length;

        while (low <= high) {
            int firstPartition = low + (high - low) / 2;
            int secondPartition = leftSize - firstPartition;

            int firstLeft = firstPartition == 0
                    ? Integer.MIN_VALUE : first[firstPartition - 1];
            int firstRight = firstPartition == first.length
                    ? Integer.MAX_VALUE : first[firstPartition];
            int secondLeft = secondPartition == 0
                    ? Integer.MIN_VALUE : second[secondPartition - 1];
            int secondRight = secondPartition == second.length
                    ? Integer.MAX_VALUE : second[secondPartition];

            if (firstLeft <= secondRight && secondLeft <= firstRight) {
                int leftMaximum = Math.max(firstLeft, secondLeft);
                if ((first.length + second.length) % 2 == 1) {
                    return leftMaximum;
                }

                int rightMinimum = Math.min(firstRight, secondRight);
                return ((double) leftMaximum + rightMinimum) / 2;
            }
            if (firstLeft > secondRight) {
                high = firstPartition - 1;
            } else {
                low = firstPartition + 1;
            }
        }

        throw new IllegalArgumentException("Both arrays must be sorted in ascending order.");
    }

    public static void main(String[] args) {
        System.out.println(findMedianSortedArrays(
                new int[] { 1, 3 },
                new int[] { 2 }));
    }
}
