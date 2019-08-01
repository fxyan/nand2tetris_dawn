from Parser import Parser


def main():
    file_name = input()
    file = open(file_name)
    file_name = file_name.split('.')[0]
    print(file_name)
    Parser(file, file_name)
    file.close()


if __name__ == '__main__':
    main()
