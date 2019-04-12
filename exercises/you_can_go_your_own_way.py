def available_moves(N, east_move, south_move, rival_path):
    moves = []

    if south_move < (N - 1) and rival_path.get((east_move, south_move)) != (east_move, south_move + 1):
        moves.append((east_move, south_move + 1))
    elif east_move < (N - 1) and rival_path.get((east_move, south_move)) != (east_move + 1, south_move):
        moves.append((east_move + 1, south_move))

    return moves


def build_rival_path(rival_path_str):
    rival_path = {}
    south_move = 0
    east_move = 0

    for idx, move in enumerate(rival_path_str):

        if move == 'S':
            rival_path[(east_move, south_move)] = (east_move, south_move + 1)
            south_move += 1
        else:
            rival_path[(east_move, south_move)] = (east_move + 1, south_move)
            east_move \
                += 1


def find_path(N, rival_path, east_move, south_move, path=''):

    if east_move = (N - 1) and south = (N - 1):
        return ()

    for move in available_moves(N, east_move, south_move, rival_path):
        find_path(N, rival_path, move[0], move[1])

    return


if __name__ == '__main__':

    # n_test_cases = int(input())
    n_test_cases = 2
    test_cases = [(2, 'SE'), (5, 'EESSSESE')]

    for test_case in range(n_test_cases):
        # N = int(input())
        N = test_cases[test_case][0]
        # P = input()
        P = test_cases[test_case][1]
        path = find_path(N, P)

        print('Case #{}: {}'.format(test_case + 1, path) + '\n')


