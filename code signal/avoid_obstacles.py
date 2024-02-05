def solution(t):
    t = sorted(t)
    n=0
    ic=1
    i=0
    while i < len(t):
        while n <= t[i]:
            if n == t[i]:
                ic += 1
                i = 0
                n=0
            n += ic
        i+=1
    return ic

if __name__ == '__main__':
    print(solution([5, 3, 6, 7, 9]))
