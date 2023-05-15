def get_floor(instructions):
    floor = 0
    for instruction in instructions:
        if instruction == '(':
            floor += 1
        elif instruction == ')':
            floor -= 1
        else:
            raise ValueError(f'WTF? I got {instruction}')
    return floor


def get_basement(instructions):
    floor = 0
    for i,instruction in enumerate(instructions):
        if instruction == '(':
            floor += 1
        elif instruction == ')':
            floor -= 1
        else:
            raise ValueError(f'WTF? I got {instruction}')
        if floor == -1:
            return i + 1
    return None


if __name__ == '__main__':
    import sys
    if len(sys.argv) == 1 or sys.argv[1] == '0':
        assert get_floor('(())') == 0
        assert get_floor('()()') == 0
        assert get_floor('(((') == 3
        assert get_floor('(()(()(') == 3

        assert get_basement(')') == 1
        assert get_basement('()())') == 5
        print('All tests are OK')

    elif sys.argv[1] == '1':
        print(get_floor(open('input.txt').readline().strip()))

    elif sys.argv[1] == '2':
        print(get_basement(open('input.txt').readline().strip()))

    else:
        raise

