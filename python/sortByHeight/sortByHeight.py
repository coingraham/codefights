
def sortByHeight(a):

    layout = ["treeorman"] * len(a)
    man_list = []
    return_list = []

    for item in range(0, len(a)):
        if a[item] == -1:
            layout[item] = "tree"
        else:
            layout[item] = "man"
            man_list.append(a[item])

    man_list = [int(x) for x in man_list]
    man_list.sort()

    for place in layout:
        if place == "tree":
            return_list.append(-1)
        else:
            return_list.append(man_list.pop(0))

    return return_list


if __name__ == '__main__':
    print sortByHeight([-1, 150, 190, 170, -1, -1, 160, 180])