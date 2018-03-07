from itertools import permutations


def calc_move(order, bottles):
    c1 = bottles[order[0]]
    c2 = bottles[order[1]]
    c3 = bottles[order[2]]
    move1 = int(c1[1]) + int(c1[2])
    move2 = int(c2[0]) + int(c2[2])
    move3 = int(c3[0]) + int(c3[1])
    return move1 + move2 + move3


def get_min_move(bottles):
    min_move = 2147483649 # 2^31 + 1
    best_order = ''
    for order in permutations('BCG', 3):
        move = calc_move(order, bottles)
        if move < min_move:
            min_move = move
            best_order = order
    return best_order, min_move


def get_bottles(bottles):
    bottles = {
        'B': (bottles[0], bottles[3], bottles[6]),
        'G': (bottles[1], bottles[4], bottles[7]),
        'C': (bottles[2], bottles[5], bottles[8])
    }
    order, move = get_min_move(bottles)
    print(''.join(order), move)


def main():
    while True:
        try:
            line = input().split()
            get_bottles(line)
        except EOFError:
            break


main()
