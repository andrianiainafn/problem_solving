def solution(a):
    m=0
    for i in range(len(a)-1):
        if a[i] > a[i+1]:
            d = a[i] - a[i + 1]
        elif a[i] <= a[i+1]:
            d = a[i + 1] - a[i]
        if d > m :
            m=d
    return  m

if __name__ == '__main__':
    print(solution([2, 4, 1, 0]))