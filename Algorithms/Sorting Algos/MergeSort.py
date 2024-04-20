def MergeSort(arr):
    if len(arr) > 1:
        lsa = arr[:len(arr)//2]
        rsa = arr[len(arr)//2:]

        # Recursively sort both left and right subarrays
        MergeSort(lsa)
        MergeSort(rsa)

        i = j = k = 0  # Indexes for left subarray, right subarray, and merged array

        # Merge the sorted subarrays
        while i < len(lsa) and j < len(rsa):
            if lsa[i] < rsa[j]:
                arr[k] = lsa[i]
                i += 1
            else:
                arr[k] = rsa[j]
                j += 1
            k += 1

        # Copy the remaining elements of left subarray
        while i < len(lsa):
            arr[k] = lsa[i]
            i += 1
            k += 1

        # Copy the remaining elements of right subarray
        while j < len(rsa):
            arr[k] = rsa[j]
            j += 1
            k += 1

a1 = [3, 1, 2, 4, 1, 5, 2, 6, 4]
MergeSort(a1)
print(a1) # [1, 1, 2, 2, 3, 4, 4, 5, 6]

