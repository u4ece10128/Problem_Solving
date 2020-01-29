import random


def random_walk(n):
    """
    Retunr coordinates x, y after random walk
    :param n: Number blocks to walk
    :return: tuple (x, y) - coordinates information
    """
    x, y = 0, 0
    for block_id in range(n):
        (dx, dy) = random.choice([(0, 1), (1, 0), (-1, 0), (0, -1)])
        x += dx
        y += dy
    return x, y

if __name__ == "__main__":

    # monte carlo simulation
    number_walks = 20000

    for walk_length in range(1, 51):
        no_transport = 0
        for i in range(number_walks):
            walk = random_walk(walk_length)
            distance = abs(walk[0]) + abs(walk[1])
            if distance <= 5:
                no_transport += 1
        percent_no_transport = float(no_transport) / number_walks
        print("Walk Size: ", walk_length, "% of no_transport : ", 100*percent_no_transport)
