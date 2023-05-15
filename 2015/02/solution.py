def get_paper_area(dimensions_string):
    dimensions = [ int(item) for item in dimensions_string.split('x') ]
    s1 = dimensions[0] * dimensions[1]
    s2 = dimensions[1] * dimensions[2]
    s3 = dimensions[2] * dimensions[0]
    area = 2*s1 + 2*s2 + 2*s3 + min(s1, s2, s3)
    return area


def get_ribbon_length(dimensions_string):
    dimensions = [ int(item) for item in dimensions_string.split('x') ]
    dimensions.sort()
    wrap_length = 2 * dimensions[0] + 2 * dimensions[1]
    bow_length = dimensions[0] * dimensions[1] * dimensions[2]
    return wrap_length + bow_length


if __name__ == '__main__':
    import sys
    if len(sys.argv) == 1 or sys.argv[1] == '0':
        assert get_paper_area('2x3x4') == 58
        assert get_paper_area('1x1x10') == 43

        assert get_ribbon_length('2x3x4') == 34
        assert get_ribbon_length('1x1x10') == 14
        print('All tests are OK')

    elif sys.argv[1] == '1':
        print(sum(get_paper_area(dimensions.strip()) for dimensions in open('input.txt').readlines()))

    elif sys.argv[1] == '2':
        print(sum(get_ribbon_length(dimensions.strip()) for dimensions in open('input.txt').readlines()))

    else:
        raise

