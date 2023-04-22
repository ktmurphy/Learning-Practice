#! python3
# finds streaks of 6 Heads or 6 Tails in a row when coin flipped 10000 times.
import random


# create external counter
def experiment():
    counter = 0
    # loop 10000 times
    for y in range(10000):
        # created randomly generated list of Heads and Tails
        lst = []
        for x in range(100):
            if random.randint(0, 1) == 0:
                lst.append("H")
            else:
                lst.append("T")
            # find streaks, count
        for x in range(len(lst) - 6):
            if lst[x : x + 6] == ["H", "H", "H", "H", "H", "H"]:
                counter += 1
                break
            elif lst[x : x + 6] == ["T", "T", "T", "T", "T", "T"]:
                counter += 1
                break
            else:
                counter += 0
                break

        lst = 0

    return counter


print(experiment())
