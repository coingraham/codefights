def chessBoardCellColor(cell1, cell2):

    rise = list("ABCDEFGH")
    run = list("12345678")

    split_cell1 = list(cell1)
    split_cell2 = list(cell2)

    if (rise.index(split_cell1[0]) + rise.index(split_cell2[0]) + run.index(split_cell1[1]) + run.index(split_cell2[1])) % 2 == 0:
        return True

    return False

if __name__ == '__main__':
    print chessBoardCellColor("A1", "C3")