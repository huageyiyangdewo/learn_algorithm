class SelectionSort(object):
    # 选择排序
    # 时间复杂度：O(n^2)

    @staticmethod
    def sort(arr):
        for i in range(len(arr)):
            # 定义一个变量，存储最小元素的索引
            min_n = i
            for j in range(i + 1, len(arr)):
                if arr[min_n] > arr[j]:

                    min_n = j
            SelectionSort.exchange(arr, min_n, i)

    @staticmethod
    def exchange(arr, min_n, j):
        # 交换索引为min, j的值
        arr[min_n], arr[j] = arr[j], arr[min_n]

