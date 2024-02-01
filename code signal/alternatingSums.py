def solution(a):
    res =[0, 0]
    for i in range(len(a)) :
        if i % 2 == 0 :
            res[0] += a[i]
        else:
            res[1] += a[i]
    return res

if __name__ == '__main__':
    print(solution([50, 60, 60, 45, 70]))