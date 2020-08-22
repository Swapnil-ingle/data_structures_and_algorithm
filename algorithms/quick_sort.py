class QuickSort:
    def __init__(self, arr):
        self.arr = arr

    def sort(self):
        self._quicksort(self.arr, 0, len(self.arr))
        return self.arr

    def _quicksort(self, arr, start, end):
        if (start < end):
            q = self._partition(arr, start, end)
            self._quicksort(arr, start, q)
            self._quicksort(arr, q + 1, end)

    def _partition(self, arr, start, end):
        pivot = arr[start]
        partition_pos = start - 1
        for i in range(start, end):
            if (arr[i] <= pivot):
                partition_pos += 1
                if (partition_pos != i):
                    arr[i], arr[partition_pos] = arr[partition_pos], arr[i]
        arr[start], arr[partition_pos] = arr[partition_pos], arr[start]
        return partition_pos


# Driver Code
quickSort = QuickSort([17, 2, 6, 19, 23, 8, 5, 10, 3, 27, 7, 1, 52, 4, 9])
print(quickSort.sort())
