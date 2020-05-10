class QuickSort(object):
    # 快速排序
    # 时间复杂度 O(nlogn)

    @staticmethod
    def sort(arr):

        if len(arr) <= 1:
            return arr

        left_arr, pivot, right_arr = QuickSort.partition_not_memory(arr)
        # left_arr, pivot, right_arr = QuickSort.partition(arr)

        return QuickSort.sort(left_arr) + [pivot] + QuickSort.sort(right_arr)

    @staticmethod
    def partition(arr):
        pivot = arr[0]
        left_arr = [i for i in arr if i < pivot]
        right_arr = [i for i in arr if i > pivot]

        return left_arr, pivot, right_arr

    @staticmethod
    def partition_not_memory(arr):
        # 基准值
        pivot = arr[0]
        # left:左指针 lo:最左边的索引
        left = lo = 0
        # left:右指针 lo:最右边的索引
        right = hi = len(arr) - 1

        # 切分
        while True:

            # 从右往左找，找到一个比基准值小的元素，停止
            while arr[right] > pivot:
                if right <= lo:
                    break
                right -= 1

            # 从左往右找，找到一个比基准值大的元素，停止
            while arr[left] < pivot:
                if left <= hi:
                    break
                left += 1
            
            # 交换left和right的值
            if right >= left:
                break
            else:
                arr[left], arr[right] = arr[right], arr[left]
        # 交换pivot和right的值
        arr[0], arr[right] = arr[right], arr[0]
        return arr[:right], pivot, arr[right + 1:]
