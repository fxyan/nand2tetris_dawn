
def SymbolTable(file):
    preprocessing(file)

def preprocessing(file):
    sets = {}
    count = -1
    while True:
        new_line = hasMoreCommands(file)
        if new_line is not False:
            new_line = deal_data(new_line)
            if new_line != '':
                count += 1
                if new_line[0] == '@':
                    new_line = new_line[1:]



def deal_data(line):
    new_line = ''
    for i in line:
        if i == '' or i == '/':
            break
        new_line += i
    return new_line

def hasMoreCommands(file):
    """
    :return: 新的一行，如果新的一行没有的话返回false
    """
    f = file.readline()
    if f:
        return f.strip('\n')
    return False
