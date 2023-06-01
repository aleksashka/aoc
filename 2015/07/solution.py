def task_1():
    pass


def task_2():
    pass


if __name__ == '__main__':
    import sys
    if len(sys.argv) == 1 or sys.argv[1] == '0':
        assert task_2() == None
        assert task_2() == None
        print('All tests are OK')

    elif sys.argv[1] == '1':
        print('No task 1 to run')

    elif sys.argv[1] == '2':
        print('No task 2 to run')

    else:
        raise

