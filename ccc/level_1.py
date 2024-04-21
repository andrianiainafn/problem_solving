def count_directions(paths):
    counts = [0, 0, 0, 0]
    for direction in paths:
        if direction == 'W':
            counts[0] += 1
        elif direction == 'D':
            counts[1] += 1
        elif direction == 'S':
            counts[2] += 1
        elif direction == 'A':
            counts[3] += 1
    return counts



with open('level_2.in', 'r') as f_source:
    content = f_source.read()

out = "level_2.out"

with open(out, 'w') as f_destination:
    f_destination.write(content)
