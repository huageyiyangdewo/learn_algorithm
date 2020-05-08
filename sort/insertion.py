class InsertionSort(object):
    # 插入排序
    # 时间复杂度：O(n^2)

    @staticmethod
    def sort(arr):
        for i in range(len(arr)):
            # i与已经排好序的数组进行比较，按照倒叙的方式来比较，
            for j in range(i - 1, 0, -1):
                if arr[i] < arr[j]:
                    # 如果i小于j的值，交换两者的值和位置
                    arr[i], arr[j] = arr[j], arr[i]
                    i = j
                else:
                    break


