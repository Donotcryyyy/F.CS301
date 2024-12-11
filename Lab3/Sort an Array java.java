class Solution {
    public int[] sortArray(int[] nums) {
        if (nums == null || nums.length <= 1) {
            return nums;
        }
        return mergeSort(nums);
    }

  
    private int[] mergeSort(int[] nums) {
        if (nums.length <= 1) {
            return nums;
        }


        int mid = nums.length / 2;
        int[] left = new int[mid];
        int[] right = new int[nums.length - mid];

    
        System.arraycopy(nums, 0, left, 0, mid);
        System.arraycopy(nums, mid, right, 0, nums.length - mid);

        left = mergeSort(left);
        right = mergeSort(right);

      
        return merge(left, right);
    }

   
    private int[] merge(int[] left, int[] right) {
        int[] result = new int[left.length + right.length];
        int i = 0, j = 0, k = 0;

   
        while (i < left.length && j < right.length) {
            if (left[i] <= right[j]) {
                result[k++] = left[i++];
            } else {
                result[k++] = right[j++];
            }
        }

        
        while (i < left.length) {
            result[k++] = left[i++];
        }
        while (j < right.length) {
            result[k++] = right[j++];
        }

        return result;
    }
}
