class MergeSort(object):
    # 归并排序
    # 时间复杂度：O(nlogn)

    @staticmethod
    def sort(arr):

        # 二分法思想，不断拆分直到为单个元素
        mid = len(arr) // 2
        left_arr = arr[0: mid]
        right_arr = arr[mid:]
        if len(left_arr) > 1:
            left_arr = MergeSort.sort(left_arr)
        if len(right_arr) > 1:
            right_arr = MergeSort.sort(right_arr)

        # 合并操作
        ret_arr = list()
        while left_arr and right_arr:
            # 比较两个尾数，取较大的一个
            if left_arr[-1] > right_arr[-1]:
                max_num = left_arr.pop()
            else:
                max_num = right_arr.pop()
            ret_arr.append(max_num)

        ret_arr.reverse()
        return (left_arr or right_arr) + ret_arr
