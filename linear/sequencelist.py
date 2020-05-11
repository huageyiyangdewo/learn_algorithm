class SequenceList(object):
    '''顺序表'''

    def __init__(self, size=8):
        # 初始化顺序表
        self.max = size
        # 记录当前顺序表中的元素个数
        self.num = 0
        # 构建一个固定大小的列表
        self.data = [None] * self.max

    def clear(self):
        # 将一个线性表置为空表
        self.num = 0

    def is_empty(self):
        # 判断当前线性表是否为空表
        return self.num == 0

    def is_full(self):
        # 判断线性表是否为满
        return self.num == self.max

    def length(self):
        # 获取线性表的长度
        return self.num

    def get(self, index):
        # 获取线性表中某一位置的值
        if not isinstance(index, int):
            raise TypeError
        if 0 <= index < self.max:
            return self.data[index]
        else:
            raise IndexError

    def set(self, index, value):
        # 修改线性表中某一位置的值
        if not isinstance(index, int):
            raise TypeError

        if 0 <= index < self.max:
            self.data[index] = value
        else:
            raise IndexError

    def append(self, value):
        # 在表尾插入一个元素
        if self.num >= self.max:
            self.data = self.resize(self.max * 2)
            self.max = self.max * 2
        self.data[self.num] = value
        self.num += 1

    # 在表中任意位置插入一个元素
    def insert(self, index, value):
        if not isinstance(index, int):
            raise IndexError

        if self.num >= self.max:
            self.data = self.resize(self.max * 2)
            self.max = self.max * 2

        if 0 <= index < self.max:
            for i in range(self.num, index, -1):
                self.data[i] = self.data[i - 1]
            self.data[index] = value
            self.num += 1
        else:
            raise IndexError

    # 删除表中某一位置的值
    def remove(self, index):
        if not isinstance(index, int):
            raise IndexError

        if 0 <= index < self.num:
            for i in range(index, self.num):
                self.data[i] = self.data[i + 1]
            self.num -= 1

            if self.num < self.max / 4:
                self.data = self.resize(int(self.max * 0.5))
                self.max = int(self.max * 0.5)
        else:
            raise IndexError

    def resize(self, new_size):
        # 动态扩充顺序表
        new_data = [None] * new_size
        for i in range(self.num):
            new_data[i] = self.data[i]
        return new_data

    # 销毁线性表
    def destroy(self):
        self.__init__()

    # 遍历
    def travel(self):
        for i in range(self.num):
            print(self.data[i])

    def index_of(self, t):
        # 查找t元素第一次出现的位置
        for i in range(self.num):
            if self.data[i] == t:
                return i

        return -1
