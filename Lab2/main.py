# Python Implementation

# Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Merge Sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

# Recursive Binary Search
def recursive_binary_search(arr, target, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return recursive_binary_search(arr, target, low, mid - 1)
    else:
        return recursive_binary_search(arr, target, mid + 1, high)

# Find Maximum (Divide and Conquer)
def find_max(arr):
    if len(arr) == 1:
        return arr[0]
    mid = len(arr) // 2
    left_max = find_max(arr[:mid])
    right_max = find_max(arr[mid:])
    return max(left_max, right_max)

# Unit Tests
if __name__ == "__main__":
    # Test Insertion Sort
    test_arr = [64, 34, 25, 12, 22, 11, 90]
    assert insertion_sort(test_arr.copy()) == sorted(test_arr)

    # Test Merge Sort
    assert merge_sort(test_arr.copy()) == sorted(test_arr)

    # Test Recursive Binary Search
    sorted_arr = sorted(test_arr)
    target = 22
    assert recursive_binary_search(sorted_arr, target, 0, len(sorted_arr) - 1) == sorted_arr.index(target)

    # Test Find Max
    assert find_max(test_arr) == max(test_arr)

    print("All tests passed!")
