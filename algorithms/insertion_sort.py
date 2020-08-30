class InsertionSort:
    def __init__(self, arr):
        self.arr = arr
        self.sortedArr = [None] * len(arr)

    def sort(self):
        for i in range(0, len(self.arr)):
            confusedElement = self.arr[i]

            if (self.sortedArr[0] is None):
                self.sortedArr[0] = confusedElement
                continue

            for j in range((len(self.sortedArr) - 1), -1, -1):
                sortedElement = self.sortedArr[j]

                if (sortedElement is None):
                    continue

                if (sortedElement > confusedElement):
                    self.sortedArr[j] = confusedElement
                    self.sortedArr[j+1] = sortedElement
                else:
                    self.sortedArr[j+1] = confusedElement
                    break

        return self.sortedArr

# Driver Code
insertionSort = InsertionSort([17, 2, 6, 19, 23, 8, 5, 10, 3, 27, 7, 1, 52, 4, 9])
print(insertionSort.sort())
insertionSort = InsertionSort([5,8,6,4,5,1,4,45,4,8,5,54,5,45,21,98,54,21,1,5])
print(insertionSort.sort())