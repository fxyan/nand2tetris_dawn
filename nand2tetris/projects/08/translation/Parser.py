from CodewWrite import Code


class Parser(object):
    def __init__(self, file, name):
        """
        :param file:  翻译文件本身
        :param name:  翻译文件名
        """
        self.file = file
        self.name = name
        self.args2_list = ['C_PUSH', 'C_POP', 'C_FUNCTION', 'C_CALL']
        self.main()

    def main(self):
        """
        主函数，处理空行和注释  并且交由self.classify来处理每行语句的分类
        :return:
        """
        file = open(self.name + '.asm', 'w+')
        while True:
            new_line = self.havenewCommand(self.file)
            print('1({})'.format(new_line))
            if new_line is not None:
                new_line = self.deal_line(new_line)
                if new_line != '':
                    print('2({})'.format(new_line))
                    command, *args = new_line.split()
                    command_type = self.commandtype(command)
                    arg1 = arg2 = None
                    if command_type != 'C_RETURN':
                        arg1 = self.arg1(command_type, args)
                    if command_type in self.args2_list or command_type == 'C_FUNCTION':
                        arg2 = self.arg2(args)
                    code = Code(command_type, command, arg1, arg2, self.name)
                    new_line = code.deal_type()
                    print('line({})'.format(new_line))
                    # return [command_type, arg1, arg2]
                    file.writelines(new_line)
            else:
                break
        file.close()

    def arg1(self, command, args):
        if command == 'C_ARITHMETIC':
            return command
        else:
            return args[0]

    def arg2(self, args):
        return args[1]

    def commandtype(self, command):
        """
        :param command: 语句类型
        :return: 返回对应语句类型的标识
        """
        count_list = ['add', 'sub', 'neg', 'eq', 'gt', 'lt', 'and', 'or', 'not']
        if command in count_list:
            return 'C_ARITHMETIC'
        elif command == 'push':
            return 'C_PUSH'
        elif command == 'pop':
            return 'C_POP'
        elif command == 'label':
            return 'C_LABEL'
        elif command == 'goto':
            return 'C_GOTO'
        elif command == 'if-goto':
            return 'C_IF'
        elif command == 'function':
            return 'C_FUNCTION'
        elif command == 'return':
            return 'C_RETURN'
        elif command == 'call':
            return 'C_CALL'

    def havenewCommand(self, file):
        """
        判断文件是否读完
        :return: 新的一行或者结束符false
        """
        for line in file:
            return line.strip().strip('\n')

    def deal_line(self, new_line):
        """
        处理对应的数据去掉后面的注释和换行符
        :param new_line: 新的一行数据
        :return: 处理过得数据
        """
        new_line = new_line.split('//')[0].strip()
        return new_line


def test_line():
    c = Parser('xx', 'uu')
    print('({})'.format(c.deal_line('//fe4wfew')))
    print('({})'.format(c.deal_line('    //ewf')))
    print('({})'.format(c.deal_line('fejwiojfioew')))


if __name__ == '__main__':
    """
    运行测试的时候将类中的self.main()注释掉
    """
    # test_line()