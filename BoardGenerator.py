from random import sample, randint
base = 3
side = base * base


def pattern(r, c):
    """Create pattern for baseline valid solution"""
    return (base * (r % base) + r // base + c) % side


def shuffle(s):
    """rows, cols, and numbers are randomized"""
    return sample(s, len(s))


def produce_board():
    """Produce board using randomized baseline pattern and remove values"""
    base_range = range(base)
    rows = [x * base + y for x in shuffle(base_range) for y in shuffle(base_range)]
    cols = [x * base + z for x in shuffle(base_range) for z in shuffle(base_range)]
    nums = shuffle(range(1, base * base + 1))

    board = [[nums[pattern(r, c)] for c in cols] for r in rows]

    for line in board:
        num_one = randint(0, 8)
        num_two = randint(0, 8)
        while abs(num_one - num_two) < 1:
            # make sure range is greater 1
            num_one = randint(0, 8)
            num_two = randint(0, 8)

        if num_one > num_two:
            for i in range(num_two, num_one):
                line[i] = 0
        elif num_two > num_one:
            for j in range(num_one, num_two):
                line[j] = 0

    return board

