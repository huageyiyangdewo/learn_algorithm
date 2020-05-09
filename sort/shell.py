class ShellSort(object):
    '''
    （1）希尔排序（shell sort）这个排序方法又称为缩小增量排序，是1959年D·L·Shell提出来的。
    该方法的基本思想是：设待排序元素序列有n个元素，首先取一个整数increment（小于n）作为间隔
    将全部元素分为increment个子序列，所有距离为increment的元素放在同一个子序列中，
    在每一个子序列中分别实行直接插入排序。然后缩小间隔increment，重复上述子序列划分和排序工作。
    直到最后取increment=1，将所有元素放在同一个子序列中排序为止。
    （2）由于开始时，increment的取值较大，每个子序列中的元素较少，排序速度较快，到排序后期increment取值逐渐变小，
    子序列中元素个数逐渐增多，但由于前面工作的基础，大多数元素已经基本有序，所以排序速度仍然很快。
    时间复杂度：O(n^2)
    '''

    @staticmethod
    def sort(arr):

        arr_length = len(arr)
        h = 1
        # 增长量h的确定规则
        while h < (arr_length / 2):
            h = 2 * h + 1

        # h的减少量
        reduction = h // 2
        # 循环次数
        for i in range(h, 0, -reduction):
            # 找到待插入元素
            for j in range(i, arr_length):
                # 把待插入的元素插入到有序列表里面去,
                # 这里的有序列表指的是:从j开始往前推，所有距离为i的元素，终止元素为0
                for z in range(j, 0, -i):
                    if arr[z] < arr[z-i]:
                        arr[z], arr[z-i] = arr[z-i], arr[z]
                    else:
                        break

    @staticmethod
    def sort_better(arr):
        b = len(arr)  # 列表长度
        gap = b // 2  # 初始步长设置为总长度的一半
        while gap >= 1:
            for i in range(b):
                j = i
                # 两个作用： j>=gap -> 找到待插入的元素
                # arr[j - gap] > arr[j] -> 与前面排好序的列表比较
                while j >= gap and arr[j - gap] > arr[j]:  # 在每一组里面进行直接插入排序
                    arr[j], arr[j - gap] = arr[j - gap], arr[j]
                    j -= gap
            gap = gap // 2  # 更新步长
