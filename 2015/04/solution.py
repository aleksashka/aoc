import hashlib


def get_number_for_specific_hash(key, zeroes=5):
    n = 1
    while n < 1_000_000_000:
        if hashlib.md5(f'{key}{n}'.encode()).hexdigest()[:zeroes] == '0'*zeroes:
            return n
        n += 1


def func2():
    pass


if __name__ == '__main__':
    import sys
    if len(sys.argv) == 1 or sys.argv[1] == '0':
        assert get_number_for_specific_hash('abcdef') == 609043
        assert get_number_for_specific_hash('pqrstuv') == 1048970
        print('All tests are OK')

    elif sys.argv[1] == '1':
        print(get_number_for_specific_hash('bgvyzdsv'))

    elif sys.argv[1] == '2':
        print(get_number_for_specific_hash('bgvyzdsv', 6))

    else:
        raise

