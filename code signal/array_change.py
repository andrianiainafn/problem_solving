def solution(a):
    i=0
    c=0
    while i < len(a)-1:
        if a[i] >= a[i+1]:
            a[i+1]+=1
            c+=1
            i-=1
        i+=1
    return c

def solution2(a):
    c=0
    for i in range(len(a)-1):
        d=0
        if a[i] >= a[i+1]:
            d = a[i] - a[i + 1] + 1
            a[i + 1] += d
        c+=d
    return c

if __name__ == '__main__':
    print(solution([-1000, 0, -2, 0]))
    print(solution2([-1000, 0, -2, 0]))