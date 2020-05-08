class BubbleSort(object):
    # 冒泡排序
    # 时间复杂度：O(n^2)

    @staticmethod
    def sort(arr):
        # 对可迭代对象进行排序
        for i in range(len(arr) - 1, 0, -1):
            for j in range(i):
                BubbleSort.greater(arr, j)

    @staticmethod
    def greater(arr, j):
        # 判断索引为j和j+1的值的大小
        if arr[j] > arr[j+1]:
            BubbleSort.exchange(arr, j, j+1)

    @staticmethod
    def exchange(arr, i, j):
        # 交换索引为i, j的值
        arr[i], arr[j] = arr[j], arr[i]


