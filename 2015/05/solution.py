def is_nice(string):
    if sum(string.count(letter) for letter in 'aeiou') < 3:
        return False
    if not any(string[i] == string[i+1] for i in range(len(string)-1)):
        return False
    if any(string.find(pattern) != -1 for pattern in ('ab', 'cd', 'pq', 'xy')):
        return False
    return True


def is_nice_v2(string):
    if all(string.find(string[i:i+2], i+2) == -1 for i in range(len(string) - 2)):
        return False
    if all(string[i] != string[i+2] for i in range(len(string) - 2)):
        return False
    return True


if __name__ == '__main__':
    import sys
    if len(sys.argv) == 1 or sys.argv[1] == '0':
        assert is_nice('ugknbfddgicrmopn') == True
        assert is_nice('aaa') == True
        assert is_nice('jchzalrnumimnmhp') == False
        assert is_nice('haegwjzuvuyypxyu') == False
        assert is_nice('dvszwmarrgswjxmb') == False

        assert is_nice_v2('qjhvhtzxzqqjkmpb') == True
        assert is_nice_v2('xxyxx') == True
        assert is_nice_v2('uurcxstgmygtbstg') == False
        assert is_nice_v2('ieodomkazucvgmuy') == False
        print('All tests are OK')

    elif sys.argv[1] == '1':
        print(sum(is_nice(line.strip()) for line in open('input.txt').readlines()))

    elif sys.argv[1] == '2':
        print(sum(is_nice_v2(line.strip()) for line in open('input.txt').readlines()))

    else:
        raise

