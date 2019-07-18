def code(command_list):
    command, arg1, arg2 = command_list
    if command == 'C_ARITHMETIC':
        return writeArithmetic(command)
    if command == 'C_PUSH' or command == 'C_POP':
        return segment(command, arg1, arg2)


def writeArithmetic(command):
    pass


def segment(command, arg1, arg2):
    pass

