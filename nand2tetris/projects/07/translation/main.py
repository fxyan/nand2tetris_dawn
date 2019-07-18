from translation.Parser_code import Parser


def main():
    file_name = input()
    file = open(file_name)
    file_name = file_name.split('.')[0]
    Parser(file, file_name)
    file.close()


if __name__ == '__main__':
    # main()
    c = 'push 0 0 0'
    a, *b = c.split()
    print(a, *b)
