// Java Implementation

import java.util.Arrays;

public class Lab3 {

    // Insertion Sort
    public static void insertionSort(int[] arr) {
        for (int i = 1; i < arr.length; i++) {
            int key = arr[i];
            int j = i - 1;

            while (j >= 0 && arr[j] > key) {
                arr[j + 1] = arr[j];
                j--;
            }
            arr[j + 1] = key;
        }
    }

    // Merge Sort
    public static void mergeSort(int[] arr, int left, int right) {
        if (left < right) {
            int mid = (left + right) / 2;

            mergeSort(arr, left, mid);
            mergeSort(arr, mid + 1, right);

            merge(arr, left, mid, right);
        }
    }

    private static void merge(int[] arr, int left, int mid, int right) {
        int n1 = mid - left + 1;
        int n2 = right - mid;

        int[] L = new int[n1];
        int[] R = new int[n2];

        System.arraycopy(arr, left, L, 0, n1);
        System.arraycopy(arr, mid + 1, R, 0, n2);

        int i = 0, j = 0, k = left;

        while (i < n1 && j < n2) {
            if (L[i] <= R[j]) {
                arr[k] = L[i];
                i++;
            } else {
                arr[k] = R[j];
                j++;
            }
            k++;
        }

        while (i < n1) {
            arr[k] = L[i];
            i++;
            k++;
        }

        while (j < n2) {
            arr[k] = R[j];
            j++;
            k++;
        }
    }

    // Recursive Binary Search
    public static int recursiveBinarySearch(int[] arr, int target, int low, int high) {
        if (low > high) {
            return -1;
        }
        int mid = (low + high) / 2;
        if (arr[mid] == target) {
            return mid;
        } else if (arr[mid] > target) {
            return recursiveBinarySearch(arr, target, low, mid - 1);
        } else {
            return recursiveBinarySearch(arr, target, mid + 1, high);
        }
    }

    // Find Maximum (Divide and Conquer)
    public static int findMax(int[] arr, int left, int right) {
        if (left == right) {
            return arr[left];
        }
        int mid = (left + right) / 2;
        int leftMax = findMax(arr, left, mid);
        int rightMax = findMax(arr, mid + 1, right);
        return Math.max(leftMax, rightMax);
    }

    // Unit Tests
    public static void main(String[] args) {
        int[] testArr = {64, 34, 25, 12, 22, 11, 90};

        // Test Insertion Sort
        int[] insertionArr = testArr.clone();
        insertionSort(insertionArr);
        System.out.println("Insertion Sort: " + Arrays.toString(insertionArr));

        // Test Merge Sort
        int[] mergeArr = testArr.clone();
        mergeSort(mergeArr, 0, mergeArr.length - 1);
        System.out.println("Merge Sort: " + Arrays.toString(mergeArr));

        // Test Recursive Binary Search
        Arrays.sort(testArr);
        int target = 22;
        int index = recursiveBinarySearch(testArr, target, 0, testArr.length - 1);
        System.out.println("Binary Search for " + target + ": " + index);

        // Test Find Max
        int max = findMax(testArr, 0, testArr.length - 1);
        System.out.println("Find Max: " + max);
    }
}