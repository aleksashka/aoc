def deliver_presents(instructions):
    current_house = [0, 0]
    houses = {}
    houses.setdefault(tuple(current_house), 1)
    for instruction in instructions:
        if instruction == '^':  # North: x, y+1
            current_house[1] += 1
            houses[tuple(current_house)] = houses.get(tuple(current_house), 0) + 1
        elif instruction == 'v':  # South: x, y-1
            current_house[1] -= 1
            houses[tuple(current_house)] = houses.get(tuple(current_house), 0) + 1
        elif instruction == '<':  # West: x-1, y
            current_house[0] -= 1
            houses[tuple(current_house)] = houses.get(tuple(current_house), 0) + 1
        elif instruction == '>':  # East: x+1, y
            current_house[0] += 1
            houses[tuple(current_house)] = houses.get(tuple(current_house), 0) + 1
        else:
            raise
    return(len(houses))


def deliver_presents_2(instructions):
    current_santa_house = [0, 0]
    current_robo_house = [0, 0]
    houses = {}
    houses.setdefault(tuple(current_santa_house), 2)
    for i,instruction in enumerate(instructions):
        if instruction == '^':  # North: x, y+1
            if i % 2 == 0:
                current_santa_house[1] += 1
                current_house = current_santa_house
            else:
                current_robo_house[1] += 1
                current_house = current_robo_house
            houses[tuple(current_house)] = houses.get(tuple(current_house), 0) + 1
        elif instruction == 'v':  # South: x, y-1
            if i % 2 == 0:
                current_santa_house[1] -= 1
                current_house = current_santa_house
            else:
                current_robo_house[1] -= 1
                current_house = current_robo_house
            houses[tuple(current_house)] = houses.get(tuple(current_house), 0) + 1
        elif instruction == '<':  # West: x-1, y
            if i % 2 == 0:
                current_santa_house[0] -= 1
                current_house = current_santa_house
            else:
                current_robo_house[0] -= 1
                current_house = current_robo_house
            houses[tuple(current_house)] = houses.get(tuple(current_house), 0) + 1
        elif instruction == '>':  # East: x+1, y
            if i % 2 == 0:
                current_santa_house[0] += 1
                current_house = current_santa_house
            else:
                current_robo_house[0] += 1
                current_house = current_robo_house
            houses[tuple(current_house)] = houses.get(tuple(current_house), 0) + 1
        else:
            raise
    return(len(houses))


if __name__ == '__main__':
    import sys
    if len(sys.argv) == 1 or sys.argv[1] == '0':
        assert deliver_presents('>') == 2
        assert deliver_presents('^>v<') == 4
        assert deliver_presents('^v^v^v^v^v') == 2
        assert deliver_presents_2('^v') == 3
        assert deliver_presents_2('^>v<') == 3
        assert deliver_presents_2('^v^v^v^v^v') == 11
        print('All tests are OK')

    elif sys.argv[1] == '1':
        print(deliver_presents(open('input.txt').readline().strip()))

    elif sys.argv[1] == '2':
        print(deliver_presents_2(open('input.txt').readline().strip()))

    else:
        raise

