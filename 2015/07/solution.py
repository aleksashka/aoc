def logic_gates(instruction_lines):
    result = {}
    for instruction_line in instruction_lines.splitlines():
        ins = instruction_line.split()
        breakpoint()
        if len(ins) == 3:
            # 123 -> x
            # y -> x
            result[ins[2]] = int(ins[0]) if ins[0].isdecimal() else result[ins[0]]
        elif len(ins) == 4:
            # NOT x -> h
            result[ins[3]] = 0xFFFF - (
                int(ins[1]) if ins[1].isdecimal() else result[ins[1]]
            )
        elif len(ins) == 5:
            # x AND y -> d
            # 1 AND 2 -> d
            # x OR y -> e
            # x LSHIFT 2 -> f
            # y RSHIFT 2 -> g
            num1 = int(ins[0]) if ins[0].isdecimal() else result[ins[0]]
            num2 = int(ins[2]) if ins[2].isdecimal() else result[ins[2]]
            if ins[1] == 'AND':
                num3 = num1 & num2
            elif ins[1] == 'OR':
                num3 = num1 | num2
            elif ins[1] == 'LSHIFT':
                num3 = num1 << num2
            elif ins[1] == 'RSHIFT':
                num3 = num1 >> num2
            result[ins[4]] = num3
        else:
            raise
    return result


def task_2():
    pass


if __name__ == "__main__":
    import sys

    if len(sys.argv) == 1 or sys.argv[1] == "0":
        instructions = """123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i"""
        result = {
            "d": 72,
            "e": 507,
            "f": 492,
            "g": 114,
            "h": 65412,
            "i": 65079,
            "x": 123,
            "y": 456,
        }

        assert logic_gates("123 -> x") == {"x": 123}
        assert logic_gates("123 -> x\nNOT x -> h") == {"x": 123, "h": 65412}
        assert logic_gates(instructions) == result
        assert task_2() == None
        print("All tests are OK")

    elif sys.argv[1] == "1":
        print(logic_gates(open("input.txt").read())['a'])

    elif sys.argv[1] == "2":
        print("No task 2 to run")

    else:
        raise
