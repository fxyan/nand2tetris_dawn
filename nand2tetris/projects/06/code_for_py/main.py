from Parse import ParseCode


def main():
    while True:
        a = input()
        if a == 'end':
            break
        f1 = open(a)
        f2 = open(a)
        ParseCode(f1, f2, a)
        # ParseCode(f1, f2, a)


if __name__ == '__main__':
    main()
