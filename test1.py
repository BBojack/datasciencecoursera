import itertools


def count_wins(dice1, dice2):
    assert len(dice1) == 6 and len(dice2) == 6
    dice1_wins, dice2_wins = 0, 0
    num_rounds = 36
    # write your code here
    pair = itertools.product(dice1, dice2)
    for item in pair:
        if item[0] > item[1]:
            dice1_wins += 1
        elif item[0] < item[1]:
            dice2_wins += 1
    return (dice1_wins, dice2_wins)


def find_the_best_dice(dices):
    assert all(len(dice) == 6 for dice in dices)

    # write your code here
    # use your implementation of count_wins method if necessary
    for i in range(len(dices)):
        count = 0
        for j in range(len(dices)):
            result = count_wins(dices[i], dices[j])
            if result[0] > result[1]:
                count += 1
        if count == len(dices) - 1:
            return i
    return -1


def find_counter(index, dices):
    for j in range(len(dices)):
        if index != j:
            compar_result = count_wins(dices[index], dices[j])
            if compar_result[0] < compar_result[1]:
                return j


def compute_strategy(dices):
    assert all(len(dice) == 6 for dice in dices)

    strategy = dict()
    strategy["choose_first"] = True
    strategy["first_dice"] = 0
    for i in range(len(dices)):
        strategy[i] = (i + 1) % len(dices)

    # write your code here
    best_dice = find_the_best_dice(dices)
    if best_dice != -1:
        strategy["first_dice"] = best_dice
    else:
        strategy["choose_first"] = False
        for i in range(len(dices)):
            strategy[i] = find_counter(i, dices)

    return strategy


print(compute_strategy([[1, 2, 5, 6, 7, 8],[2, 2, 4, 5, 8, 9],[2, 3, 4, 5, 6, 10]]))
