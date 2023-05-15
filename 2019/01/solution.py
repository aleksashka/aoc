def get_fuel_mass(mass):
    result = mass // 3 - 2
    return result


def get_total_fuel_mass(mass):
    unaccounted_fuel_mass = get_fuel_mass(mass)
    result = 0
    while True:
        if unaccounted_fuel_mass > 0:
            result += unaccounted_fuel_mass
            unaccounted_fuel_mass = get_fuel_mass(unaccounted_fuel_mass)
        else:
            break
    return result


if __name__ == '__main__':
    import sys
    if len(sys.argv) == 1 or sys.argv[1] == '0':
        assert get_fuel_mass(12) == 2
        assert get_fuel_mass(14) == 2
        assert get_fuel_mass(1969) == 654
        assert get_fuel_mass(100756) == 33583

        assert get_total_fuel_mass(14) == 2
        assert get_total_fuel_mass(1969) == 966
        assert get_total_fuel_mass(100756) == 50346
        print('All tests are OK')

    elif sys.argv[1] == '1':
        print(sum(get_fuel_mass(int(module_mass.strip())) for module_mass in open('input.txt')))

    elif sys.argv[1] == '2':
        print(sum(get_total_fuel_mass(int(module_mass.strip())) for module_mass in open('input.txt')))

    else:
        raise
