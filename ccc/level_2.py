def calculate_lawn_size(path):
    min_x = 0
    max_x = 0
    min_y = 0
    max_y = 0
    x = 0
    y = 0

    for step in path:
        if step == 'W':
            y += 1
            max_y = max(max_y, y)
        elif step == 'A':
            x -= 1
            min_x = min(min_x, x)
            # print(x)
            # print(min_x)
        elif step == 'S':
            y -= 1
            min_y = min(min_y, y)
        elif step == 'D':
            x += 1
            max_x = max(max_x, x)
    # print(min_x)
    width = max_x - min_x + 1
    height = max_y - min_y + 1
    print(path.count("A") +1)
    print(path.count("W") +1)

    return width, height


def main():
    with open('level2/level2_example.txt', 'r') as file:
        N = int(file.readline())
        paths = [file.readline().strip() for _ in range(N)]

    lawn_sizes = []
    for path in paths:
        width, height = calculate_lawn_size(path)
        lawn_sizes.append((width, height))

    for size in lawn_sizes:
        print(f"{size[0]} {size[1]}")


if __name__ == "__main__":
    main()