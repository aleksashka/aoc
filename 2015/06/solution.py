def parse_instruction_line(instruction_line):
    if instruction_line.startswith('toggle'):
        action = 'toggle'
    else:
        action = ' '.join(instruction_line.split()[:2])
    start, _, end = instruction_line.split()[-3:]
    start = tuple(int(value) for value in start.split(','))
    end = tuple(int(value) for value in end.split(','))
    return action, start, end

def count_lit_lights_task_1(instruction_lines, size_x=1000, size_y=1000):
    lights = { (x, y):0 for x in range(size_x) for y in range(size_y) }
    for instruction_line in instruction_lines.splitlines():
        action, start, end = parse_instruction_line(instruction_line)
        toggle = False
        if action == 'turn on':
            data = 1
        elif action == 'turn off':
            data = 0
        elif action == 'toggle':
            toggle = True
        else:
            raise
        for x in range(start[0], end[0]+1):
            for y in range(start[1], end[1]+1):
                if toggle:
                    lights[(x, y)] = 1 - lights[(x, y)]
                else:
                    lights[(x, y)] = data
    return sum(lights.values())


def count_lit_lights_task_2(instruction_lines, size_x=1000, size_y=1000):
    lights = { (x, y):0 for x in range(size_x) for y in range(size_y) }
    for instruction_line in instruction_lines.splitlines():
        action, start, end = parse_instruction_line(instruction_line)
        print(action, end=' ', flush=True)
        for x in range(start[0], end[0]+1):
            for y in range(start[1], end[1]+1):
                if action == 'turn on':
                    lights[(x, y)] += 1
                elif action == 'turn off':
                    lights[(x, y)] = max(0, lights[(x, y)]-1)
                elif action == 'toggle':
                    lights[(x, y)] += 2
                else:
                    raise
    print()
    return sum(lights.values())


if __name__ == '__main__':
    import sys
    if len(sys.argv) == 1 or sys.argv[1] == '0':
        assert count_lit_lights_task_1('turn on 0,0 through 2,2', 3, 3) == 9
        assert count_lit_lights_task_1('turn on 0,0 through 2,2\nturn off 0,0 through 0,2', 3, 3) == 6
        assert count_lit_lights_task_1('turn on 0,0 through 2,2\nturn off 0,0 through 0,2\ntoggle 0,0 through 2,0', 3, 3) == 5
        assert count_lit_lights_task_2('turn on 0,0 through 0,0') == 1
        assert count_lit_lights_task_2('toggle 0,0 through 999,999') == 2_000_000
        print('All tests are OK')

    elif sys.argv[1] == '1':
        import time
        start_time = time.time()
        print(count_lit_lights_task_1(open('input.txt').read()))
        print(f'{round(time.time()- start_time, 2)} seconds')

    elif sys.argv[1] == '2':
        print(count_lit_lights_task_2(open('input.txt').read()))

    else:
        raise

