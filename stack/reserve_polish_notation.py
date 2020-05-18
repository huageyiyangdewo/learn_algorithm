from stack.stack_link import StackLink


class ReservePolishNotation(object):

    @staticmethod
    def calculate(expression):
        '''
        计算逆波兰表达式的结果
        :param expression:
        :return:
        '''
        new_stack = StackLink()
        for exp in expression:
            if exp in ['+', '-', '*', '/']:
                o1 = new_stack.pop()
                o2 = new_stack.pop()
                if not o1 or not o2:
                    return False

                t_str = o2 + exp + o1
                ret = eval(t_str)
                new_stack.push(str(ret))
            else:
                new_stack.push(exp)

        return new_stack.pop()
