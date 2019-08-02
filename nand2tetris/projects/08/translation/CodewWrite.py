class Code():
    def __init__(self, command_type, command, args1, args2, file_name):
        self.pushTemplate = '@SP\nA=M\nM=D\n@SP\nM=M+1\n'
        self.index = 0
        self.return_index = 0
        self.command_type = command_type
        self.command = command
        self.args1 = args1
        self.args2 = args2
        self.file_name = file_name

    def deal_type(self):
        if self.command_type == 'C_PUSH' or self.command_type == 'C_POP':
            return self.WritePushPop()
        elif self.command == 'label':
            return self.WriteLabel()
        elif self.command == 'goto':
            return self.WriteGoto()
        elif self.command == 'if-goto':
            return self.WriteIf()
        elif self.command == 'function':
            return self.WriteFunction()
        elif self.command == 'return':
            return self.WriteReturn()
        elif self.command == 'call':
            pass
            # return self.writeCall()
        else:
            print('debug{}'.format(self.command_type))
            return self.WriteArithmetic()

    def WriteArithmetic(self):
        if self.command == 'add':
            return '@SP\nM=M-1\nA=M\nD=M\n@SP\nM=M-1\nA=M\nM=D+M\n@SP\nM=M+1\n'
        elif self.command == 'sub':
            return '@SP\nM=M-1\nA=M\nD=M\n@SP\nM=M-1\nA=M\nM=M-D\n@SP\nM=M+1\n'
        elif self.command == 'neg':
            return '@SP\nM=M-1\nA=M\nM=-M\n@SP\nM=M+1\n'
        elif self.command == 'and':
            return '@SP\nM=M-1\nA=M\nD=M\n@SP\nM=M-1\nA=M\nM=M&D\n@SP\nM=M+1\n'
        elif self.command == 'or':
            return '@SP\nM=M-1\nA=M\nD=M\n@SP\nM=M-1\nA=M\nM=M|D\n@SP\nM=M+1\n'
        elif self.command == 'not':
            return '@SP\nM=M-1\nA=M\nM=!M\n@SP\nM=M+1\n'
        elif self.command == 'eq':
            return self.create_judgement_string('JEQ')
        elif self.command == 'gt':
            return self.create_judgement_string('JGT')
        elif self.command == 'lt':
            return self.create_judgement_string('JLT')

    def create_judgement_string(self, judge):
        res = '@SP\r\n' + 'AM=M-1\r\n' + 'D=M\r\n'+ 'A=A-1\r\n' + 'D=M-D\r\n' + '@TRUE' + str(self.index) + '\r\n'+ \
              'D;' + judge + '\r\n' + '@SP\r\n' + 'AM=M-1\r\n' + 'M=0\r\n' + '@SP\r\n' + 'M=M+1\r\n' + \
              '@CONTINUE' + str(self.index) + '\r\n' + '0;JMP\r\n' + '(TRUE' + str(self.index) + ')\r\n' + '@SP\r\n' + 'AM=M-1\r\n' + \
              'M=1\r\n' + '@SP\r\n' + 'M=M+1\r\n' + '(CONTINUE' + str(self.index) + ')\r\n'
        self.index += 1
        return res

    def WritePushPop(self):
        res = None
        print('code ({}  {}  {}  {})'.format(self.command, self.command_type, self.args1, self.args2))
        if self.command_type == 'C_PUSH':
            if self.args1 == 'local':
                res = '@LCL\nD=M\n@{}\nA=A+D\nD=M\n'.format(self.args2) + self.pushTemplate
            elif self.args1 == 'static':
                res = '@{}.{}\nD=M\n'.format(self.file_name, self.args2) + self.pushTemplate
            elif self.args1 == 'constant':
                res = '@'+ self.args2 + '\nD=A\n' + self.pushTemplate
            elif self.args1 == 'argument':
                res = '@ARG\nD=M\n@{}\nA=A+D\nD=M\n'.format(self.args2) + self.pushTemplate
            elif self.args1 == 'this':
                res = '@THIS\nD=M\n@{}\nA=A+D\nD=M\n'.format(self.args2) + self.pushTemplate
            elif self.args1 == 'that':
                res = '@THAT\nD=M\n@{}\nA=A+D\nD=M\n'.format(self.args2) + self.pushTemplate
            elif self.args1 == 'pointer':
                if self.args2 == '0':
                    res = '@THIS\nD=M\n' + self.pushTemplate
                else:
                    res = '@THAT\nD=M\n' + self.pushTemplate
            elif self.args1 == 'temp':
                res = '@5\nD=A\n@{}\nA=A+D\nD=M\n'.format(self.args2) + self.pushTemplate
        else:
            if self.args1 == 'local':
                res = '@SP\nM=M-1\nA=M\nD=M\n@LCL\nA=M\n'
                for i in range(0, int(self.args2)):
                    res += 'A=A+1\n'
                res += 'M=D\n'
            elif self.args1 == 'argument':
                res = '@SP\nM=M-1\nA=M\nD=M\n@ARG\nA=M\n'
                for i in range(0, int(self.args2)):
                    res += 'A=A+1\n'
                res += 'M=D\n'
            elif self.args1 == 'this':
                res = '@SP\nM=M-1\nA=M\nD=M\n@THIS\nA=M\n'
                for i in range(0, int(self.args2)):
                    res += 'A=A+1\n'
                res += 'M=D\n'
            elif self.args1 == 'that':
                res = '@SP\nM=M-1\nA=M\nD=M\n@THAT\nA=M\n'
                for i in range(0, int(self.args2)):
                    res += 'A=A+1\n'
                res += 'M=D\n'
            elif self.args1 == 'pointer':
                res = '@SP\nM=M-1\nA=M\nD=M\n'
                if self.args2 == '0':
                    res += '@3\n'
                else:
                    res += '@4\n'
                res += 'M=D\n'
            elif self.args1 == 'static':
                res = '@SP\nM=M-1\nA=M\nD=M\n@{}.{}\nM=D\n'.format(self.file_name, self.args2)
            elif self.args1 == 'temp':
                res = '@SP\nM=M-1\nA=M\nD=M\n@5\n'
                for i in range(0, int(self.args2)):
                    res += 'A=A+1\n'
                res += 'M=D\n'
        return res

    def WriteInit(self):
        res = '@256\nD=A\n@SP\nM=D\n'
        res += self.WriteCall('Sys.init', 0)
        return res

    def WriteLabel(self):
        return '({})\n'.format(self.args1)

    def WriteGoto(self):
        res = '@{}\n0;JMP\n'.format(self.args1)
        return res

    def WriteIf(self):
        res = '@SP\nM=M-1\n@SP\nA=M\nD=M\n@{}\nD;JNE\n'.format(self.args1)
        return res

    def WriteCall(self, functionName, numArgs):
        res = '@return_address{}\nD=A\n@SP\nA=M\nM=D\n@SP\nM=M+1\n'.format(self.return_index)
        res += '@LCL\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n'
        res += '@ARG\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n'
        res += '@THIS\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n'
        res += '@THAT\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n'
        res += '@{}\nD=A\n@5\nD=D+A\n@SP\nD=M-D\n@ARG\nM=D\n'.format(numArgs)
        res += '@SP\nD=M\n@LCL\nM=D\n'
        res += self.WriteGoto()
        res += '(return-address{})\n'.format(self.return_index)
        self.return_index += 1


    def WriteReturn(self):
        res = '@LCL\nD=M\n@13\nM=D\n'
        res += '@5\nD=A\n@13\nD=M-D\nA=D\nD=M\n@14\nM=D\n'
        res += '@SP\nM=M-1\n@SP\nA=M\nD=M\n@ARG\nA=M\nM=D\n'
        res += '@ARG\nD=M\n@SP\nM=D+1\n'
        res += '@13\nA=M\nA=A-1\nD=M\n@THAT\nM=D\n'
        res += '@2\nD=A\n@13\nA=M\nA=A-D\nD=M\n@THIS\nM=D\n'
        res += '@3\nD=A\n@13\nA=M\nA=A-D\nD=M\n@ARG\nM=D\n'
        res += '@4\nD=A\n@13\nA=M\nA=A-D\nD=M\n@LCL\nM=D\n'
        res += 	'@14\nA=M\n"0;JMP\n'
        return res

    def WriteFunction(self):
        res = '({}\n)'.format(self.args1)
        for i in range(int(self.args2)):
            res += '@0\nD=A\n' + self.pushTemplate
        return res


