def solution(a, b):
    c = 0
    if a == b:
        return True
    for i in range(len(a)):
        if a[i] not in b or b[i] not in a:
            return False
        if a[i] != b[i]:
            c += 1
        if c > 2:
            return False
    return True


def solution2(a, b):
    if a == b:
        return True
    d = [(x, y) for x, y in zip(a, b) if x != y]
    return len(d) == 2 and d[0][::-1] == d[1]


if __name__ == '__main__':
    print(solution([1, 2, 3], [1, 2, 3]))
