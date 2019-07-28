from code_for_py.Code import deal_with_c
from SymbolTable import Symbol_Table


class ParseCode(object):
    def __init__(self, pre_file, file, name):
        """
        :param name: 获取到的asm文件
        """
        self.pre_file = pre_file
        self.file = file
        self.name = name
        self.count_raw = 0
        self.count = 16
        self.symbol = Symbol_Table()
        self.pre_main()
        self.main()

    def pre_main(self):
        self.pre_deal_while()

    def main(self):
        """
        主流程
        :return:
        """
        file_name = self.name.split('.')[0] + '.hack'
        fn = open(file_name, 'w+')
        # 第二遍
        self.deal_while(fn)
        fn.close()

    def pre_deal_while(self):
        for i in range(2):
            while True:
                new_line = self.hasMoreCommands(self.pre_file)
                print('({})'.format(new_line))
                if new_line is not None:
                    # 去注释
                    new_line = self.deal_data(new_line)
                    if new_line != '':
                        print('({})'.format(new_line))
                        line_type = self.commandType(new_line)
                        if line_type is not False and i == 0:
                            if line_type == 'L_COMMAND':
                                self.symbol_p(new_line)
                                self.count_raw -= 1
                        else:
                            if line_type == 'A_COMMAND':
                                self.symbol_p(new_line)
                        self.count_raw += 1
                else:
                    break
            self.pre_file.seek(0)
        self.pre_file.close()

    def deal_while(self, file):
        # 逻辑和上面一样
        while True:
            new_line = self.hasMoreCommands(self.file)
            if new_line is not None:
                new_line = self.deal_data(new_line)
                if new_line != '':
                    line_type = self.commandType(new_line)
                    if line_type is not False:
                        if line_type == 'A_COMMAND':
                            bin_data = self.get_symbol(new_line)
                        elif line_type == 'L_COMMAND':
                            continue
                        else:
                            bin_data = self.deal_c(new_line)
                        file.writelines(bin_data+'\n')
            else:
                break

    def symbol_p(self, line):
        """
        :param line: A指令
        :return: 返回对应的二进制数
        """
        print(line)
        if line[0] == '@':
            line = line[1:]
            if self.symbol.GerAddress(line) is None:
                if line[0] >= '0' and line[0] <= '9':
                    difference = bin(int(line))[2:]
                    if len(difference) < 16:
                        difference = '0' * (16 - len(difference)) + difference
                    self.symbol.addEntry(line, difference)
                else:
                    # if self.symbol.GerAddress(line) is None:
                    difference = bin(self.count)[2:]
                    self.count += 1
                    if len(difference) < 16:
                        difference = '0' * (16 - len(difference)) + difference
                    self.symbol.addEntry(line, difference)
        else:
            line = line[1:-1]
            if self.symbol.GerAddress(line) is None:
                if line[0] >= '0' and line[0] <= '9':
                    difference = bin(int(line[1:]))[2:]
                    if len(difference) < 16:
                        difference = '0' * (16 - len(difference)) + difference
                    self.symbol.addEntry(line, difference)
                else:
                    difference = bin(self.count_raw)[2:]
                    print('self.count_raw', difference, self.count_raw)
                    if len(difference) < 16:
                        difference = '0' * (16 - len(difference)) + difference
                    self.symbol.addEntry(line, difference)

    def get_symbol(self, line):
        if line[0] == '@':
            line = line[1:]
            return self.symbol.GerAddress(line)

    def deal_c(self, line):
        """
        :param line: C指令
        :return: 返回处理后的C指令
        """
        return deal_with_c(line)

    def deal_data(self, line):
        """
        :param line: 新的一行的数据
        :return: 过滤掉注释
        """
        line.strip()
        new_line = ''
        for i in line:
            if i == ' ' or i == '/':
                break
            new_line += i
        return new_line

    def hasMoreCommands(self, file):
        """
        :return: 新的一行，如果新的一行没有的话返回false
        """
        for line in file:
            return line.strip().strip('\n')

    def commandType(self, new_line):
        new_line = new_line.strip()
        if new_line == '' or new_line[:2] == '//':
            return False
        if new_line[0] == '(':
            return 'L_COMMAND'
        elif new_line[0] == '@':
            return 'A_COMMAND'
        else:
            return 'C_COMMAND'

