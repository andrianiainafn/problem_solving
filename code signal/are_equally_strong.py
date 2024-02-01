def solution(yl,yr,fl,fr):
    return (yl == fl and yr == fr) or (yl == fr and yr == fl)


if __name__ == '__main__':
    print(solution(10,15,5,20))