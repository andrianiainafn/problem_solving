def is_valid_path(lawn, path):
    tree_position = None
    for i in range(len(lawn)):
        for j in range(len(lawn[0])):
            if lawn[i][j] == 'X':
                tree_position = (i, j)
                break
        if tree_position:
            break
    visited = set()
    x, y = 1, 0
    visited.add((x, y))
    def is_valid_cell(x, y):
        return  (x, y) not in visited
    for step in path:
        if step == 'W':
            if is_valid_cell(x, y + 1):
                y += 1
                visited.add((x, y))
            else:
                return "INVALID"
        elif step == 'A':
            if is_valid_cell(x - 1, y):
                x -= 1
                visited.add((x, y))
            else:
                return "INVALID"
        elif step == 'S':
            if is_valid_cell(x, y - 1):
                y -= 1
                visited.add((x, y))
            else:
                return "INVALID"
        elif step == 'D':
            if is_valid_cell(x + 1, y):
                x += 1
                visited.add((x, y))
            else:
                return "INVALID"
    return "VALID"


def main():
    validity = is_valid_path(['..X..', '.....', '.....'], "ASSDWDSDWWDSS")
    print(validity)

if __name__ == "__main__":
    main()
