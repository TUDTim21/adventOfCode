from math import prod

ITEMS = 'ITEMS'
OPERATION_SIGN = 'OPERATION_SIGN'
OPERATION_VALUE = 'OPERATION_VALUE'
DIVISOR = 'DIVISOR'
TARGET_TRUE = 'TARGET_TRUE'
TARGET_FALSE = 'TARGET_FALSE'


def increase_worry_level(monkey: dict, id: int = 0):
    item = monkey[ITEMS][id]

    if monkey[OPERATION_SIGN] == '*':
        mult = item
        if monkey[OPERATION_VALUE] != 'old':
            mult = int(monkey[OPERATION_VALUE])

        monkey[ITEMS][id] *= mult


    else:
        monkey[ITEMS][id] += int(monkey[OPERATION_VALUE])


def control_worry_level(monkey: dict, mod=None, id: int = 0):
    if mod is None:
        monkey[ITEMS][id] //= 3
    else:
        monkey[ITEMS][id] %= mod


def is_divisible(monkey: dict, id: int = 0):
    return monkey[ITEMS][id] % monkey[DIVISOR] == 0


def move_item(monkey: dict, monkeys: list, is_divisible: bool, id: int = 0):
    item = monkey[ITEMS].pop(id)

    if is_divisible:
        target_monkey_index = monkey[TARGET_TRUE]
    else:
        target_monkey_index = monkey[TARGET_FALSE]

    monkeys[target_monkey_index][ITEMS].append(item)


def part1():
    solve(get_data('test11.txt'), 20, None)


def part2():
    monkeys = get_data('test11.txt')
    solve(monkeys, 9, prod([x[DIVISOR] for x in monkeys]))


def solve(monkeys: list, times: int, mod: int = None):
    inspection = [0 for _ in monkeys]

    for _ in range(times):
        for i, monkey in enumerate(monkeys):
            for _ in range(len(monkey[ITEMS])):
                inspection[i] += 1
                increase_worry_level(monkey)
                control_worry_level(monkey, mod)
                move_item(monkey, monkeys, is_divisible(monkey))
    print(monkeys)
    print(prod(sorted(inspection, reverse=True)[:2]))


def get_data(path: str) -> list:
    monkeys = []
    lines = open(path, 'r').read().strip().split('\n')
    index = -1
    for anchor in range(1, len(lines), 7):
        index += 1
        operation = lines[anchor + 1].split(' ')[-2:]
        dt = {
            ITEMS: list(map(int, lines[anchor].replace(', ', ',').split(' ')[-1].split(','))),
            OPERATION_SIGN: operation[0],
            OPERATION_VALUE: operation[1],
            DIVISOR: int(lines[anchor + 2].split(' ')[-1]),
            TARGET_TRUE: int(lines[anchor + 3].split(' ')[-1]),
            TARGET_FALSE: int(lines[anchor + 4].split(' ')[-1]),
        }
        monkeys.append(dt)
    return monkeys


if __name__ == '__main__':
    part1()
    part2()