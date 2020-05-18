from stack.stack_link import StackLink


class BracketsMatch(object):

    @staticmethod
    def is_match(check_str):
        '''
        检查给定字符串是否成对出现
        :param check_str:
        :return:
        '''

        stack = StackLink()
        for t_str in check_str:
            if t_str == '(':
                stack.push(t_str)
            elif t_str == ')':
                ret = stack.pop()
                if ret is None:
                    return False

        return True if stack.is_empty() else False
