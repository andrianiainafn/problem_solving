def solution(picture):
    border = ['*' for _ in range(len(picture[0]) + 2)]
    picture = ['*' + i + '*' for i in picture]
    picture.append(''.join(border))
    picture.insert(0, ''.join(border))
    return picture


if __name__ == '__main__':
    print(solution(["abc", "ded"]))
