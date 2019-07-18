from translation.Tra_Code import Code

class Parser(object):
    def __init__(self, file, name):
        """
        :param file:  翻译文件本身
        :param name:  翻译文件名
        """
        self.file = file
        self.name = name
        self.main()

    def main(self):
        """
        主函数，处理空行和注释  并且交由self.classify来处理每行语句的分类
        :return:
        """
        file = open(self.name + '.asm', 'w+')
        while True:
            new_line = self.havenewCommand()
            if new_line is not False:
                new_line = self.deal_line(new_line)
                if new_line != '':
                    command_list = self.classify(new_line)
                    Code(file, command_list)
                    file.writelines(new_line + '\n')
            else:
                break
        file.close()

    def classify(self, line):
        command, *args = line.split()
        command_type = self.commandtype(command)
        arg1 = arg2 = None
        if command != 'C_RETURN':
            arg1 = self.arg1(command, args)
        args2_list = ['C_PUSH', 'C_POP', 'C_FUNCTION', 'C_CALL']
        if command in args2_list:
            arg2 = args[1]
        return [command, arg1, arg2]

    def arg1(self, command, args):
        if command == 'C_ARITHMETIC':
            return command
        else:
            return args[0]

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

    def havenewCommand(self):
        """
        判断文件是否读完
        :return: 新的一行或者结束符false
        """
        new_line = self.file.readline()
        if new_line:
            return new_line
        return False

    def deal_line(self, new_line):
        """
        处理对应的数据去掉后面的注释和换行符
        :param new_line: 新的一行数据
        :return: 处理过得数据
        """
        new_line.strip('\n')
        new_line = new_line.split('//')[0].strip()
        return new_line
