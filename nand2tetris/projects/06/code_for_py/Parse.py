from .Code import deal_with_c

class ParseCode(object):
    def __init__(self, file, name):
        """
        :param name: 获取到的asm文件
        """
        self.file = file
        self.name = name
        self.seta = {
            'SP': '0000000000000000'
            'LCL'
        }
        self.main()

    def main(self):
        """
        主流程
        :return:
        """
        file_name = self.name.split('.')[0] + '.hack'
        fn = open(file_name, 'w+')
        self.pre_deal()
        self.deal_while(fn)

        fn.close()

    def pre_deal(self):
        while True:
            new_line = self.hasMoreCommands()
            if new_line is not False:
                new_line = self.deal_data(new_line)
                if new_line != '':
                    line_type = self.commandType(new_line)
                    if line_type is not False:
                        if line_type == 'L_COMMAND' or line_type == 'A_COMMAND':
                            bin_data = self.symbol(new_line)
                        else:
                            bin_data = self.deal_c(new_line)
            else:
                break

    def deal_while(self, file):
        while True:
            new_line = self.hasMoreCommands()
            if new_line is not False:
                new_line = self.deal_data(new_line)
                if new_line != '':
                    line_type = self.commandType(new_line)
                    if line_type is not False:
                        if line_type == 'L_COMMAND' or line_type == 'A_COMMAND':
                            bin_data = self.symbol(new_line)
                        else:
                            bin_data = self.deal_c(new_line)
                        file.writelines(bin_data+'\n')
            else:
                break

    def symbol(self, line):
        """
        :param line: A指令
        :return: 返回对应的二进制数
        """
        line = bin(int(line[1:]))[2:]
        if len(line) < 16:
            difference = '0' * (16 - len(line)) + line
            return difference
        return line

    def deal_c(self, line):
        """
        :param line: C指令
        :return: 返回处理后的C指令
        """
        return deal_with_c(line)

    def deal_data(self, line):
        new_line = ''
        for i in line:
            if i == '' or i == '/':
                break
            new_line += i
        return new_line

    def hasMoreCommands(self):
        """
        :return: 新的一行，如果新的一行没有的话返回false
        """
        f = self.file.readline()
        if f:
            return f.strip('\n')
        return False

    def commandType(self, new_line):
        new_line = new_line.strip()
        print(new_line, type)
        if new_line == '' or new_line[:2] == '//':
            return False
        elif new_line[0] == '(':
            return 'L_COMMAND'
        elif new_line[0] == '@':
            return 'A_COMMAND'
        else:
            return 'C_COMMAND'

