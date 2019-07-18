from code_for_py.Parse import ParseCode


def main():
    while True:
        a = input()
        if a == 'end':
            break
        f = open(a)
        ParseCode(f, a)


if __name__ == '__main__':
    main()
