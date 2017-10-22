"""
Given the positions of a white bishop and a black pawn on the standard chess board, determine whether the bishop can capture the pawn in one move.

The bishop has no restrictions in distance for each move, but is limited to diagonal movement.
"""


def bishopAndPawn(bishop, pawn):

    table_map = {
        "a": 1,
        "b": 2,
        "c": 3,
        "d": 4,
        "e": 5,
        "f": 6,
        "g": 7,
        "h": 8,
    }

    x1 = table_map[bishop[0]]
    y1 = int(bishop[1])

    x2 = table_map[pawn[0]]
    y2 = int(pawn[1])

    if y1 - y2 == 0 or x1 - x2 == 0:
        return False

    rise = float(y1 - y2)
    run = float(x1 - x2)

    slope = rise/run

    if abs(slope) == 1:
        return True
    else:
        return False


if __name__ == '__main__':
    print bishopAndPawn("b4", "d7")
